_AE='alaPimdmConfigMIBGroup'
_AD='alaPimsmDebugMIBGroup'
_AC='alaPimsmConfigMIBGroup'
_AB='alaPimdmRedundantStatus'
_AA='alaPimdmBfdStatus'
_A9='alaPimdmV6AdminStatus'
_A8='alaPimdmStateRefreshLimitInterval'
_A7='alaPimdmStateRefreshTimeToLive'
_A6='alaPimdmAdminStatus'
_A5='alaPimsmDebugAll'
_A4='alaPimsmDebugMisc'
_A3='alaPimsmDebugIpmrm'
_A2='alaPimsmDebugTm'
_A1='alaPimsmDebugInit'
_A0='alaPimsmDebugMip'
_z='alaPimsmDebugSpt'
_y='alaPimsmDebugIgmp'
_x='alaPimsmDebugTime'
_w='alaPimsmDebugAssert'
_v='alaPimsmDebugJoinPrune'
_u='alaPimsmDebugRoute'
_t='alaPimsmDebugCRP'
_s='alaPimsmDebugBootstrap'
_r='alaPimsmDebugNbr'
_q='alaPimsmDebugHello'
_p='alaPimsmDebugError'
_o='alaPimsmDebugLevel'
_n='alaPimsmV6BidirStatus'
_m='alaPimsmBidirPeriodicInterval'
_l='alaPimsmBidirStatus'
_k='alaPimsmBfdStatus'
_j='alaPimsmV6RPSwitchover'
_i='alaPimsmV6SPTConfig'
_h='alaPimsmV6AdminStatus'
_g='alaPimsmRPThreshold'
_f='alaPimsmAdminSPTConfig'
_e='alaPimsmStaticRPRowStatus'
_d='alaPimsmAdminStaticRPConfig'
_c='alaPimsmRegisterSuppressionTimeout'
_b='alaPimsmOldRegisterMessageSupport'
_a='alaPimsmProbeTime'
_Z='alaPimsmMaxRPs'
_Y='alaPimsmDataTimeout'
_X='alaPimsmAdminCRPPriority'
_W='alaPimsmAdminCRPAddress'
_V='alaPimsmCRPInterval'
_U='alaPimsmCRPExpiryTime'
_T='alaPimsmAdminBSRPriority'
_S='alaPimsmAdminBSRHashmasklen'
_R='alaPimsmAdminBSRAddress'
_Q='alaPimsmAdminStatus'
_P='alaPimsmStaticRPAddress'
_O='alaPimsmStaticRPGroupMask'
_N='alaPimsmStaticRPGroupAddress'
_M='read-only'
_L='TimeTicks'
_K='IpAddress'
_J='not-accessible'
_I='seconds'
_H='obsolete'
_G='deprecated'
_F='current'
_E='disable'
_D='enable'
_C='read-write'
_B='Integer32'
_A='ALCATEL-IND1-PIM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Pim,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1Pim')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,_K,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_L,'Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1PIMMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,1))
if mibBuilder.loadTexts:alcatelIND1PIMMIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1PIMMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1PIMMIBObjects=_AlcatelIND1PIMMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1))
_AlaPimsmGlobalConfig_ObjectIdentity=ObjectIdentity
alaPimsmGlobalConfig=_AlaPimsmGlobalConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1))
class _AlaPimsmAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmAdminStatus_Type.__name__=_B
_AlaPimsmAdminStatus_Object=MibScalar
alaPimsmAdminStatus=_AlaPimsmAdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,1),_AlaPimsmAdminStatus_Type())
alaPimsmAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmAdminStatus.setStatus(_F)
_AlaPimsmAdminBSRAddress_Type=IpAddress
_AlaPimsmAdminBSRAddress_Object=MibScalar
alaPimsmAdminBSRAddress=_AlaPimsmAdminBSRAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,2),_AlaPimsmAdminBSRAddress_Type())
alaPimsmAdminBSRAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:alaPimsmAdminBSRAddress.setStatus(_H)
class _AlaPimsmAdminBSRHashmasklen_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AlaPimsmAdminBSRHashmasklen_Type.__name__=_B
_AlaPimsmAdminBSRHashmasklen_Object=MibScalar
alaPimsmAdminBSRHashmasklen=_AlaPimsmAdminBSRHashmasklen_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,3),_AlaPimsmAdminBSRHashmasklen_Type())
alaPimsmAdminBSRHashmasklen.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmAdminBSRHashmasklen.setStatus(_H)
class _AlaPimsmAdminBSRPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaPimsmAdminBSRPriority_Type.__name__=_B
_AlaPimsmAdminBSRPriority_Object=MibScalar
alaPimsmAdminBSRPriority=_AlaPimsmAdminBSRPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,4),_AlaPimsmAdminBSRPriority_Type())
alaPimsmAdminBSRPriority.setMaxAccess(_M)
if mibBuilder.loadTexts:alaPimsmAdminBSRPriority.setStatus(_H)
class _AlaPimsmCRPExpiryTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_AlaPimsmCRPExpiryTime_Type.__name__=_B
_AlaPimsmCRPExpiryTime_Object=MibScalar
alaPimsmCRPExpiryTime=_AlaPimsmCRPExpiryTime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,5),_AlaPimsmCRPExpiryTime_Type())
alaPimsmCRPExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmCRPExpiryTime.setStatus(_H)
if mibBuilder.loadTexts:alaPimsmCRPExpiryTime.setUnits(_I)
class _AlaPimsmCRPInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_AlaPimsmCRPInterval_Type.__name__=_B
_AlaPimsmCRPInterval_Object=MibScalar
alaPimsmCRPInterval=_AlaPimsmCRPInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,6),_AlaPimsmCRPInterval_Type())
alaPimsmCRPInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmCRPInterval.setStatus(_H)
class _AlaPimsmAdminCRPAddress_Type(IpAddress):defaultHexValue='00000000'
_AlaPimsmAdminCRPAddress_Type.__name__=_K
_AlaPimsmAdminCRPAddress_Object=MibScalar
alaPimsmAdminCRPAddress=_AlaPimsmAdminCRPAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,7),_AlaPimsmAdminCRPAddress_Type())
alaPimsmAdminCRPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmAdminCRPAddress.setStatus(_H)
class _AlaPimsmAdminCRPPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaPimsmAdminCRPPriority_Type.__name__=_B
_AlaPimsmAdminCRPPriority_Object=MibScalar
alaPimsmAdminCRPPriority=_AlaPimsmAdminCRPPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,8),_AlaPimsmAdminCRPPriority_Type())
alaPimsmAdminCRPPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmAdminCRPPriority.setStatus(_H)
class _AlaPimsmDataTimeout_Type(Integer32):defaultValue=210;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_AlaPimsmDataTimeout_Type.__name__=_B
_AlaPimsmDataTimeout_Object=MibScalar
alaPimsmDataTimeout=_AlaPimsmDataTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,9),_AlaPimsmDataTimeout_Type())
alaPimsmDataTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDataTimeout.setStatus(_H)
if mibBuilder.loadTexts:alaPimsmDataTimeout.setUnits(_I)
class _AlaPimsmMaxRPs_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AlaPimsmMaxRPs_Type.__name__=_B
_AlaPimsmMaxRPs_Object=MibScalar
alaPimsmMaxRPs=_AlaPimsmMaxRPs_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,10),_AlaPimsmMaxRPs_Type())
alaPimsmMaxRPs.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmMaxRPs.setStatus(_F)
class _AlaPimsmProbeTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_AlaPimsmProbeTime_Type.__name__=_B
_AlaPimsmProbeTime_Object=MibScalar
alaPimsmProbeTime=_AlaPimsmProbeTime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,11),_AlaPimsmProbeTime_Type())
alaPimsmProbeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmProbeTime.setStatus(_F)
if mibBuilder.loadTexts:alaPimsmProbeTime.setUnits(_I)
class _AlaPimsmOldRegisterMessageSupport_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('header',1),('full',2)))
_AlaPimsmOldRegisterMessageSupport_Type.__name__=_B
_AlaPimsmOldRegisterMessageSupport_Object=MibScalar
alaPimsmOldRegisterMessageSupport=_AlaPimsmOldRegisterMessageSupport_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,12),_AlaPimsmOldRegisterMessageSupport_Type())
alaPimsmOldRegisterMessageSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmOldRegisterMessageSupport.setStatus(_F)
class _AlaPimsmRegisterSuppressionTimeout_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_AlaPimsmRegisterSuppressionTimeout_Type.__name__=_B
_AlaPimsmRegisterSuppressionTimeout_Object=MibScalar
alaPimsmRegisterSuppressionTimeout=_AlaPimsmRegisterSuppressionTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,13),_AlaPimsmRegisterSuppressionTimeout_Type())
alaPimsmRegisterSuppressionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmRegisterSuppressionTimeout.setStatus(_H)
if mibBuilder.loadTexts:alaPimsmRegisterSuppressionTimeout.setUnits(_I)
class _AlaPimsmAdminStaticRPConfig_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmAdminStaticRPConfig_Type.__name__=_B
_AlaPimsmAdminStaticRPConfig_Object=MibScalar
alaPimsmAdminStaticRPConfig=_AlaPimsmAdminStaticRPConfig_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,14),_AlaPimsmAdminStaticRPConfig_Type())
alaPimsmAdminStaticRPConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmAdminStaticRPConfig.setStatus(_H)
_AlaPimsmStaticRPTable_Object=MibTable
alaPimsmStaticRPTable=_AlaPimsmStaticRPTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,15))
if mibBuilder.loadTexts:alaPimsmStaticRPTable.setStatus(_H)
_AlaPimsmStaticRPEntry_Object=MibTableRow
alaPimsmStaticRPEntry=_AlaPimsmStaticRPEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,15,1))
alaPimsmStaticRPEntry.setIndexNames((0,_A,_N),(0,_A,_O),(0,_A,_P))
if mibBuilder.loadTexts:alaPimsmStaticRPEntry.setStatus(_H)
_AlaPimsmStaticRPGroupAddress_Type=IpAddress
_AlaPimsmStaticRPGroupAddress_Object=MibTableColumn
alaPimsmStaticRPGroupAddress=_AlaPimsmStaticRPGroupAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,15,1,1),_AlaPimsmStaticRPGroupAddress_Type())
alaPimsmStaticRPGroupAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:alaPimsmStaticRPGroupAddress.setStatus(_H)
_AlaPimsmStaticRPGroupMask_Type=IpAddress
_AlaPimsmStaticRPGroupMask_Object=MibTableColumn
alaPimsmStaticRPGroupMask=_AlaPimsmStaticRPGroupMask_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,15,1,2),_AlaPimsmStaticRPGroupMask_Type())
alaPimsmStaticRPGroupMask.setMaxAccess(_J)
if mibBuilder.loadTexts:alaPimsmStaticRPGroupMask.setStatus(_H)
_AlaPimsmStaticRPAddress_Type=IpAddress
_AlaPimsmStaticRPAddress_Object=MibTableColumn
alaPimsmStaticRPAddress=_AlaPimsmStaticRPAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,15,1,3),_AlaPimsmStaticRPAddress_Type())
alaPimsmStaticRPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:alaPimsmStaticRPAddress.setStatus(_H)
_AlaPimsmStaticRPRowStatus_Type=RowStatus
_AlaPimsmStaticRPRowStatus_Object=MibTableColumn
alaPimsmStaticRPRowStatus=_AlaPimsmStaticRPRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,15,1,4),_AlaPimsmStaticRPRowStatus_Type())
alaPimsmStaticRPRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:alaPimsmStaticRPRowStatus.setStatus(_H)
class _AlaPimsmAdminSPTConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmAdminSPTConfig_Type.__name__=_B
_AlaPimsmAdminSPTConfig_Object=MibScalar
alaPimsmAdminSPTConfig=_AlaPimsmAdminSPTConfig_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,16),_AlaPimsmAdminSPTConfig_Type())
alaPimsmAdminSPTConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmAdminSPTConfig.setStatus(_F)
class _AlaPimsmRPThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlaPimsmRPThreshold_Type.__name__=_B
_AlaPimsmRPThreshold_Object=MibScalar
alaPimsmRPThreshold=_AlaPimsmRPThreshold_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,17),_AlaPimsmRPThreshold_Type())
alaPimsmRPThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmRPThreshold.setStatus(_F)
class _AlaPimsmV6AdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmV6AdminStatus_Type.__name__=_B
_AlaPimsmV6AdminStatus_Object=MibScalar
alaPimsmV6AdminStatus=_AlaPimsmV6AdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,18),_AlaPimsmV6AdminStatus_Type())
alaPimsmV6AdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmV6AdminStatus.setStatus(_F)
class _AlaPimsmV6SPTConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmV6SPTConfig_Type.__name__=_B
_AlaPimsmV6SPTConfig_Object=MibScalar
alaPimsmV6SPTConfig=_AlaPimsmV6SPTConfig_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,19),_AlaPimsmV6SPTConfig_Type())
alaPimsmV6SPTConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmV6SPTConfig.setStatus(_F)
class _AlaPimsmV6RPSwitchover_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmV6RPSwitchover_Type.__name__=_B
_AlaPimsmV6RPSwitchover_Object=MibScalar
alaPimsmV6RPSwitchover=_AlaPimsmV6RPSwitchover_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,20),_AlaPimsmV6RPSwitchover_Type())
alaPimsmV6RPSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmV6RPSwitchover.setStatus(_F)
class _AlaPimsmBfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmBfdStatus_Type.__name__=_B
_AlaPimsmBfdStatus_Object=MibScalar
alaPimsmBfdStatus=_AlaPimsmBfdStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,21),_AlaPimsmBfdStatus_Type())
alaPimsmBfdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmBfdStatus.setStatus(_F)
class _AlaPimsmBidirStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmBidirStatus_Type.__name__=_B
_AlaPimsmBidirStatus_Object=MibScalar
alaPimsmBidirStatus=_AlaPimsmBidirStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,22),_AlaPimsmBidirStatus_Type())
alaPimsmBidirStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmBidirStatus.setStatus(_F)
class _AlaPimsmBidirPeriodicInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_AlaPimsmBidirPeriodicInterval_Type.__name__=_B
_AlaPimsmBidirPeriodicInterval_Object=MibScalar
alaPimsmBidirPeriodicInterval=_AlaPimsmBidirPeriodicInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,23),_AlaPimsmBidirPeriodicInterval_Type())
alaPimsmBidirPeriodicInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmBidirPeriodicInterval.setStatus(_F)
if mibBuilder.loadTexts:alaPimsmBidirPeriodicInterval.setUnits(_I)
class _AlaPimsmV6BidirStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmV6BidirStatus_Type.__name__=_B
_AlaPimsmV6BidirStatus_Object=MibScalar
alaPimsmV6BidirStatus=_AlaPimsmV6BidirStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,1,24),_AlaPimsmV6BidirStatus_Type())
alaPimsmV6BidirStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmV6BidirStatus.setStatus(_F)
_AlaPimsmDebugConfig_ObjectIdentity=ObjectIdentity
alaPimsmDebugConfig=_AlaPimsmDebugConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2))
class _AlaPimsmDebugLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaPimsmDebugLevel_Type.__name__=_B
_AlaPimsmDebugLevel_Object=MibScalar
alaPimsmDebugLevel=_AlaPimsmDebugLevel_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,1),_AlaPimsmDebugLevel_Type())
alaPimsmDebugLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugLevel.setStatus(_G)
class _AlaPimsmDebugError_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugError_Type.__name__=_B
_AlaPimsmDebugError_Object=MibScalar
alaPimsmDebugError=_AlaPimsmDebugError_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,2),_AlaPimsmDebugError_Type())
alaPimsmDebugError.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugError.setStatus(_G)
class _AlaPimsmDebugHello_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugHello_Type.__name__=_B
_AlaPimsmDebugHello_Object=MibScalar
alaPimsmDebugHello=_AlaPimsmDebugHello_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,3),_AlaPimsmDebugHello_Type())
alaPimsmDebugHello.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugHello.setStatus(_G)
class _AlaPimsmDebugNbr_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugNbr_Type.__name__=_B
_AlaPimsmDebugNbr_Object=MibScalar
alaPimsmDebugNbr=_AlaPimsmDebugNbr_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,4),_AlaPimsmDebugNbr_Type())
alaPimsmDebugNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugNbr.setStatus(_G)
class _AlaPimsmDebugBootstrap_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugBootstrap_Type.__name__=_B
_AlaPimsmDebugBootstrap_Object=MibScalar
alaPimsmDebugBootstrap=_AlaPimsmDebugBootstrap_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,5),_AlaPimsmDebugBootstrap_Type())
alaPimsmDebugBootstrap.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugBootstrap.setStatus(_G)
class _AlaPimsmDebugCRP_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugCRP_Type.__name__=_B
_AlaPimsmDebugCRP_Object=MibScalar
alaPimsmDebugCRP=_AlaPimsmDebugCRP_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,6),_AlaPimsmDebugCRP_Type())
alaPimsmDebugCRP.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugCRP.setStatus(_G)
class _AlaPimsmDebugRoute_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugRoute_Type.__name__=_B
_AlaPimsmDebugRoute_Object=MibScalar
alaPimsmDebugRoute=_AlaPimsmDebugRoute_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,7),_AlaPimsmDebugRoute_Type())
alaPimsmDebugRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugRoute.setStatus(_G)
class _AlaPimsmDebugJoinPrune_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugJoinPrune_Type.__name__=_B
_AlaPimsmDebugJoinPrune_Object=MibScalar
alaPimsmDebugJoinPrune=_AlaPimsmDebugJoinPrune_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,8),_AlaPimsmDebugJoinPrune_Type())
alaPimsmDebugJoinPrune.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugJoinPrune.setStatus(_G)
class _AlaPimsmDebugAssert_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugAssert_Type.__name__=_B
_AlaPimsmDebugAssert_Object=MibScalar
alaPimsmDebugAssert=_AlaPimsmDebugAssert_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,9),_AlaPimsmDebugAssert_Type())
alaPimsmDebugAssert.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugAssert.setStatus(_G)
class _AlaPimsmDebugTime_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugTime_Type.__name__=_B
_AlaPimsmDebugTime_Object=MibScalar
alaPimsmDebugTime=_AlaPimsmDebugTime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,10),_AlaPimsmDebugTime_Type())
alaPimsmDebugTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugTime.setStatus(_G)
class _AlaPimsmDebugIgmp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugIgmp_Type.__name__=_B
_AlaPimsmDebugIgmp_Object=MibScalar
alaPimsmDebugIgmp=_AlaPimsmDebugIgmp_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,11),_AlaPimsmDebugIgmp_Type())
alaPimsmDebugIgmp.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugIgmp.setStatus(_G)
class _AlaPimsmDebugSpt_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugSpt_Type.__name__=_B
_AlaPimsmDebugSpt_Object=MibScalar
alaPimsmDebugSpt=_AlaPimsmDebugSpt_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,12),_AlaPimsmDebugSpt_Type())
alaPimsmDebugSpt.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugSpt.setStatus(_G)
class _AlaPimsmDebugMip_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugMip_Type.__name__=_B
_AlaPimsmDebugMip_Object=MibScalar
alaPimsmDebugMip=_AlaPimsmDebugMip_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,13),_AlaPimsmDebugMip_Type())
alaPimsmDebugMip.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugMip.setStatus(_G)
class _AlaPimsmDebugInit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugInit_Type.__name__=_B
_AlaPimsmDebugInit_Object=MibScalar
alaPimsmDebugInit=_AlaPimsmDebugInit_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,14),_AlaPimsmDebugInit_Type())
alaPimsmDebugInit.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugInit.setStatus(_G)
class _AlaPimsmDebugTm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugTm_Type.__name__=_B
_AlaPimsmDebugTm_Object=MibScalar
alaPimsmDebugTm=_AlaPimsmDebugTm_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,15),_AlaPimsmDebugTm_Type())
alaPimsmDebugTm.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugTm.setStatus(_G)
class _AlaPimsmDebugIpmrm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugIpmrm_Type.__name__=_B
_AlaPimsmDebugIpmrm_Object=MibScalar
alaPimsmDebugIpmrm=_AlaPimsmDebugIpmrm_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,16),_AlaPimsmDebugIpmrm_Type())
alaPimsmDebugIpmrm.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugIpmrm.setStatus(_G)
class _AlaPimsmDebugMisc_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugMisc_Type.__name__=_B
_AlaPimsmDebugMisc_Object=MibScalar
alaPimsmDebugMisc=_AlaPimsmDebugMisc_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,17),_AlaPimsmDebugMisc_Type())
alaPimsmDebugMisc.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugMisc.setStatus(_G)
class _AlaPimsmDebugAll_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimsmDebugAll_Type.__name__=_B
_AlaPimsmDebugAll_Object=MibScalar
alaPimsmDebugAll=_AlaPimsmDebugAll_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,2,18),_AlaPimsmDebugAll_Type())
alaPimsmDebugAll.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimsmDebugAll.setStatus(_G)
_AlaPimdmGlobalConfig_ObjectIdentity=ObjectIdentity
alaPimdmGlobalConfig=_AlaPimdmGlobalConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,3))
class _AlaPimdmAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimdmAdminStatus_Type.__name__=_B
_AlaPimdmAdminStatus_Object=MibScalar
alaPimdmAdminStatus=_AlaPimdmAdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,3,1),_AlaPimdmAdminStatus_Type())
alaPimdmAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimdmAdminStatus.setStatus(_F)
class _AlaPimdmStateRefreshTimeToLive_Type(Integer32):defaultValue=16
_AlaPimdmStateRefreshTimeToLive_Type.__name__=_B
_AlaPimdmStateRefreshTimeToLive_Object=MibScalar
alaPimdmStateRefreshTimeToLive=_AlaPimdmStateRefreshTimeToLive_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,3,2),_AlaPimdmStateRefreshTimeToLive_Type())
alaPimdmStateRefreshTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimdmStateRefreshTimeToLive.setStatus(_F)
class _AlaPimdmStateRefreshLimitInterval_Type(TimeTicks):defaultValue=0
_AlaPimdmStateRefreshLimitInterval_Type.__name__=_L
_AlaPimdmStateRefreshLimitInterval_Object=MibScalar
alaPimdmStateRefreshLimitInterval=_AlaPimdmStateRefreshLimitInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,3,3),_AlaPimdmStateRefreshLimitInterval_Type())
alaPimdmStateRefreshLimitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimdmStateRefreshLimitInterval.setStatus(_F)
class _AlaPimdmV6AdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimdmV6AdminStatus_Type.__name__=_B
_AlaPimdmV6AdminStatus_Object=MibScalar
alaPimdmV6AdminStatus=_AlaPimdmV6AdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,3,4),_AlaPimdmV6AdminStatus_Type())
alaPimdmV6AdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimdmV6AdminStatus.setStatus(_F)
class _AlaPimdmBfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimdmBfdStatus_Type.__name__=_B
_AlaPimdmBfdStatus_Object=MibScalar
alaPimdmBfdStatus=_AlaPimdmBfdStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,3,5),_AlaPimdmBfdStatus_Type())
alaPimdmBfdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimdmBfdStatus.setStatus(_F)
class _AlaPimdmRedundantStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlaPimdmRedundantStatus_Type.__name__=_B
_AlaPimdmRedundantStatus_Object=MibScalar
alaPimdmRedundantStatus=_AlaPimdmRedundantStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,1,3,6),_AlaPimdmRedundantStatus_Type())
alaPimdmRedundantStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimdmRedundantStatus.setStatus(_F)
_AlcatelIND1PIMMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1PIMMIBConformance=_AlcatelIND1PIMMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,2))
_AlcatelIND1PIMMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1PIMMIBCompliances=_AlcatelIND1PIMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,2,1))
_AlcatelIND1PIMMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1PIMMIBGroups=_AlcatelIND1PIMMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,2,2))
alaPimsmConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,2,2,1))
alaPimsmConfigMIBGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:alaPimsmConfigMIBGroup.setStatus(_F)
alaPimsmDebugMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,2,2,2))
alaPimsmDebugMIBGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:alaPimsmDebugMIBGroup.setStatus(_F)
alaPimdmConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,2,2,3))
alaPimdmConfigMIBGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:alaPimdmConfigMIBGroup.setStatus(_F)
alaPimsmCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,2,1,1))
alaPimsmCompliance.setObjects(*((_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:alaPimsmCompliance.setStatus(_F)
alaPimdmCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,6,1,2,1,2))
alaPimdmCompliance.setObjects((_A,_AE))
if mibBuilder.loadTexts:alaPimdmCompliance.setStatus(_F)
mibBuilder.exportSymbols(_A,**{'alcatelIND1PIMMIB':alcatelIND1PIMMIB,'alcatelIND1PIMMIBObjects':alcatelIND1PIMMIBObjects,'alaPimsmGlobalConfig':alaPimsmGlobalConfig,_Q:alaPimsmAdminStatus,_R:alaPimsmAdminBSRAddress,_S:alaPimsmAdminBSRHashmasklen,_T:alaPimsmAdminBSRPriority,_U:alaPimsmCRPExpiryTime,_V:alaPimsmCRPInterval,_W:alaPimsmAdminCRPAddress,_X:alaPimsmAdminCRPPriority,_Y:alaPimsmDataTimeout,_Z:alaPimsmMaxRPs,_a:alaPimsmProbeTime,_b:alaPimsmOldRegisterMessageSupport,_c:alaPimsmRegisterSuppressionTimeout,_d:alaPimsmAdminStaticRPConfig,'alaPimsmStaticRPTable':alaPimsmStaticRPTable,'alaPimsmStaticRPEntry':alaPimsmStaticRPEntry,_N:alaPimsmStaticRPGroupAddress,_O:alaPimsmStaticRPGroupMask,_P:alaPimsmStaticRPAddress,_e:alaPimsmStaticRPRowStatus,_f:alaPimsmAdminSPTConfig,_g:alaPimsmRPThreshold,_h:alaPimsmV6AdminStatus,_i:alaPimsmV6SPTConfig,_j:alaPimsmV6RPSwitchover,_k:alaPimsmBfdStatus,_l:alaPimsmBidirStatus,_m:alaPimsmBidirPeriodicInterval,_n:alaPimsmV6BidirStatus,'alaPimsmDebugConfig':alaPimsmDebugConfig,_o:alaPimsmDebugLevel,_p:alaPimsmDebugError,_q:alaPimsmDebugHello,_r:alaPimsmDebugNbr,_s:alaPimsmDebugBootstrap,_t:alaPimsmDebugCRP,_u:alaPimsmDebugRoute,_v:alaPimsmDebugJoinPrune,_w:alaPimsmDebugAssert,_x:alaPimsmDebugTime,_y:alaPimsmDebugIgmp,_z:alaPimsmDebugSpt,_A0:alaPimsmDebugMip,_A1:alaPimsmDebugInit,_A2:alaPimsmDebugTm,_A3:alaPimsmDebugIpmrm,_A4:alaPimsmDebugMisc,_A5:alaPimsmDebugAll,'alaPimdmGlobalConfig':alaPimdmGlobalConfig,_A6:alaPimdmAdminStatus,_A7:alaPimdmStateRefreshTimeToLive,_A8:alaPimdmStateRefreshLimitInterval,_A9:alaPimdmV6AdminStatus,_AA:alaPimdmBfdStatus,_AB:alaPimdmRedundantStatus,'alcatelIND1PIMMIBConformance':alcatelIND1PIMMIBConformance,'alcatelIND1PIMMIBCompliances':alcatelIND1PIMMIBCompliances,'alaPimsmCompliance':alaPimsmCompliance,'alaPimdmCompliance':alaPimdmCompliance,'alcatelIND1PIMMIBGroups':alcatelIND1PIMMIBGroups,_AC:alaPimsmConfigMIBGroup,_AD:alaPimsmDebugMIBGroup,_AE:alaPimdmConfigMIBGroup})