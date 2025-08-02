_Y='tptZphaNotifyNewState'
_X='tptZphaNotifySegmentName'
_W='tptZphaNotifyTimeStamp'
_V='tptZphaNotifyDeviceID'
_U='tptPerfProtNotifyMissedAlerts'
_T='tptPerfProtNotifyDuration'
_S='tptPerfProtNotifyLossThreshold'
_R='tptPerfProtNotifyPacketLoss'
_Q='tptPerfProtNotifyPhase'
_P='tptPerfProtNotifyTimeStamp'
_O='tptPerfProtNotifyDeviceID'
_N='tptTrhaNotifyNewState'
_M='tptTrhaNotifyTimeStamp'
_L='tptTrhaNotifyDeviceID'
_K='tptIhaNotifyFaultCause'
_J='tptIhaNotifyFaultState'
_I='tptIhaNotifyTimeStamp'
_H='tptIhaNotifyDeviceID'
_G='highAvailZeroPowerIndex'
_F='unknown'
_E='normal'
_D='OctetString'
_C='TPT-HIGH-AVAIL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
EnabledOrNot,=mibBuilder.importSymbols('TPT-PORT-CONFIG-MIB','EnabledOrNot')
tpt_tpa_eventsV2,tpt_tpa_objs,tpt_tpa_unkparams=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-eventsV2','tpt-tpa-objs','tpt-tpa-unkparams')
tpt_high_avail_objs=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,6))
if mibBuilder.loadTexts:tpt_high_avail_objs.setRevisions(('2016-09-08 18:54','2016-05-25 18:54'))
class FaultState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),('fallback',1)))
class FaultCause(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('none',0),('suspended-task',1),('out-of-memory',2),('hardware-breakpoint',3),('tse-failure',4),('watchdog-timeout',5),('user-reset',6),('user-fallback',7),('threshold-failure',8),('software-watchdog-timeout',9),('oam-fault',10),('hard-disk-disable',11),('initialization-failure',12),('internal-link-failure',13),('multiple-fan-failures',14),('packet-egress-integrity',15),('stack-master',16),('waiting-on-stack',17),('spike-reboot-or-halt',18),('process-error',19),('low-health-score',20)))
class ConnectionState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('not-connected',0),('unresponsive',1),('connected',2)))
class PerfProtPhase(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('entering',1),('continuing',2),('exiting',3)))
class ZphaState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),('ips-bypass',1)))
class ZphaAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_E,1),('bypass',2)))
class ZphaMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_F,0),('single',2),('multi',3)))
class ZphaPresent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('absent',0),('present',1)))
_HighAvailTimeStamp_Type=Unsigned32
_HighAvailTimeStamp_Object=MibScalar
highAvailTimeStamp=_HighAvailTimeStamp_Object((1,3,6,1,4,1,10734,3,3,2,6,1),_HighAvailTimeStamp_Type())
highAvailTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailTimeStamp.setStatus(_A)
_HighAvailFaultState_Type=FaultState
_HighAvailFaultState_Object=MibScalar
highAvailFaultState=_HighAvailFaultState_Object((1,3,6,1,4,1,10734,3,3,2,6,2),_HighAvailFaultState_Type())
highAvailFaultState.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailFaultState.setStatus(_A)
_HighAvailFaultCause_Type=FaultCause
_HighAvailFaultCause_Object=MibScalar
highAvailFaultCause=_HighAvailFaultCause_Object((1,3,6,1,4,1,10734,3,3,2,6,3),_HighAvailFaultCause_Type())
highAvailFaultCause.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailFaultCause.setStatus(_A)
_HighAvailThresholdEnabled_Type=EnabledOrNot
_HighAvailThresholdEnabled_Object=MibScalar
highAvailThresholdEnabled=_HighAvailThresholdEnabled_Object((1,3,6,1,4,1,10734,3,3,2,6,4),_HighAvailThresholdEnabled_Type())
highAvailThresholdEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailThresholdEnabled.setStatus(_A)
_HighAvailThresholdPercent_Type=Integer32
_HighAvailThresholdPercent_Object=MibScalar
highAvailThresholdPercent=_HighAvailThresholdPercent_Object((1,3,6,1,4,1,10734,3,3,2,6,5),_HighAvailThresholdPercent_Type())
highAvailThresholdPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailThresholdPercent.setStatus(_A)
_HighAvailEnabled_Type=EnabledOrNot
_HighAvailEnabled_Object=MibScalar
highAvailEnabled=_HighAvailEnabled_Object((1,3,6,1,4,1,10734,3,3,2,6,6),_HighAvailEnabled_Type())
highAvailEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailEnabled.setStatus(_A)
_HighAvailTransparentState_Type=ConnectionState
_HighAvailTransparentState_Object=MibScalar
highAvailTransparentState=_HighAvailTransparentState_Object((1,3,6,1,4,1,10734,3,3,2,6,7),_HighAvailTransparentState_Type())
highAvailTransparentState.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailTransparentState.setStatus(_A)
_HighAvailTransparentEnabled_Type=EnabledOrNot
_HighAvailTransparentEnabled_Object=MibScalar
highAvailTransparentEnabled=_HighAvailTransparentEnabled_Object((1,3,6,1,4,1,10734,3,3,2,6,8),_HighAvailTransparentEnabled_Type())
highAvailTransparentEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailTransparentEnabled.setStatus(_A)
class _HighAvailTransparentPartner_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HighAvailTransparentPartner_Type.__name__=_D
_HighAvailTransparentPartner_Object=MibScalar
highAvailTransparentPartner=_HighAvailTransparentPartner_Object((1,3,6,1,4,1,10734,3,3,2,6,9),_HighAvailTransparentPartner_Type())
highAvailTransparentPartner.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailTransparentPartner.setStatus(_A)
_HighAvailZeroPowerState_Type=ZphaState
_HighAvailZeroPowerState_Object=MibScalar
highAvailZeroPowerState=_HighAvailZeroPowerState_Object((1,3,6,1,4,1,10734,3,3,2,6,10),_HighAvailZeroPowerState_Type())
highAvailZeroPowerState.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailZeroPowerState.setStatus(_A)
_HighAvailZeroPowerQuantity_Type=Unsigned32
_HighAvailZeroPowerQuantity_Object=MibScalar
highAvailZeroPowerQuantity=_HighAvailZeroPowerQuantity_Object((1,3,6,1,4,1,10734,3,3,2,6,11),_HighAvailZeroPowerQuantity_Type())
highAvailZeroPowerQuantity.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailZeroPowerQuantity.setStatus(_A)
_HighAvailZeroPowerTable_Object=MibTable
highAvailZeroPowerTable=_HighAvailZeroPowerTable_Object((1,3,6,1,4,1,10734,3,3,2,6,12))
if mibBuilder.loadTexts:highAvailZeroPowerTable.setStatus(_A)
_HighAvailZeroPowerEntry_Object=MibTableRow
highAvailZeroPowerEntry=_HighAvailZeroPowerEntry_Object((1,3,6,1,4,1,10734,3,3,2,6,12,1))
highAvailZeroPowerEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:highAvailZeroPowerEntry.setStatus(_A)
_HighAvailZeroPowerIndex_Type=Unsigned32
_HighAvailZeroPowerIndex_Object=MibTableColumn
highAvailZeroPowerIndex=_HighAvailZeroPowerIndex_Object((1,3,6,1,4,1,10734,3,3,2,6,12,1,1),_HighAvailZeroPowerIndex_Type())
highAvailZeroPowerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:highAvailZeroPowerIndex.setStatus(_A)
class _HighAvailZeroPowerSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HighAvailZeroPowerSegment_Type.__name__=_D
_HighAvailZeroPowerSegment_Object=MibTableColumn
highAvailZeroPowerSegment=_HighAvailZeroPowerSegment_Object((1,3,6,1,4,1,10734,3,3,2,6,12,1,2),_HighAvailZeroPowerSegment_Type())
highAvailZeroPowerSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailZeroPowerSegment.setStatus(_A)
_HighAvailZeroPowerActive_Type=ZphaState
_HighAvailZeroPowerActive_Object=MibTableColumn
highAvailZeroPowerActive=_HighAvailZeroPowerActive_Object((1,3,6,1,4,1,10734,3,3,2,6,12,1,3),_HighAvailZeroPowerActive_Type())
highAvailZeroPowerActive.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailZeroPowerActive.setStatus(_A)
_HighAvailZeroPowerAction_Type=ZphaAction
_HighAvailZeroPowerAction_Object=MibTableColumn
highAvailZeroPowerAction=_HighAvailZeroPowerAction_Object((1,3,6,1,4,1,10734,3,3,2,6,12,1,4),_HighAvailZeroPowerAction_Type())
highAvailZeroPowerAction.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailZeroPowerAction.setStatus(_A)
_HighAvailZeroPowerMode_Type=ZphaMode
_HighAvailZeroPowerMode_Object=MibTableColumn
highAvailZeroPowerMode=_HighAvailZeroPowerMode_Object((1,3,6,1,4,1,10734,3,3,2,6,12,1,5),_HighAvailZeroPowerMode_Type())
highAvailZeroPowerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailZeroPowerMode.setStatus(_A)
_HighAvailZeroPowerPresence_Type=ZphaPresent
_HighAvailZeroPowerPresence_Object=MibScalar
highAvailZeroPowerPresence=_HighAvailZeroPowerPresence_Object((1,3,6,1,4,1,10734,3,3,2,6,13),_HighAvailZeroPowerPresence_Type())
highAvailZeroPowerPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:highAvailZeroPowerPresence.setStatus(_A)
class _TptIhaNotifyDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptIhaNotifyDeviceID_Type.__name__=_D
_TptIhaNotifyDeviceID_Object=MibScalar
tptIhaNotifyDeviceID=_TptIhaNotifyDeviceID_Object((1,3,6,1,4,1,10734,3,3,3,1,81),_TptIhaNotifyDeviceID_Type())
tptIhaNotifyDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:tptIhaNotifyDeviceID.setStatus(_A)
_TptIhaNotifyTimeStamp_Type=Unsigned32
_TptIhaNotifyTimeStamp_Object=MibScalar
tptIhaNotifyTimeStamp=_TptIhaNotifyTimeStamp_Object((1,3,6,1,4,1,10734,3,3,3,1,82),_TptIhaNotifyTimeStamp_Type())
tptIhaNotifyTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:tptIhaNotifyTimeStamp.setStatus(_A)
_TptIhaNotifyFaultState_Type=FaultState
_TptIhaNotifyFaultState_Object=MibScalar
tptIhaNotifyFaultState=_TptIhaNotifyFaultState_Object((1,3,6,1,4,1,10734,3,3,3,1,83),_TptIhaNotifyFaultState_Type())
tptIhaNotifyFaultState.setMaxAccess(_B)
if mibBuilder.loadTexts:tptIhaNotifyFaultState.setStatus(_A)
_TptIhaNotifyFaultCause_Type=FaultCause
_TptIhaNotifyFaultCause_Object=MibScalar
tptIhaNotifyFaultCause=_TptIhaNotifyFaultCause_Object((1,3,6,1,4,1,10734,3,3,3,1,84),_TptIhaNotifyFaultCause_Type())
tptIhaNotifyFaultCause.setMaxAccess(_B)
if mibBuilder.loadTexts:tptIhaNotifyFaultCause.setStatus(_A)
class _TptTrhaNotifyDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptTrhaNotifyDeviceID_Type.__name__=_D
_TptTrhaNotifyDeviceID_Object=MibScalar
tptTrhaNotifyDeviceID=_TptTrhaNotifyDeviceID_Object((1,3,6,1,4,1,10734,3,3,3,1,86),_TptTrhaNotifyDeviceID_Type())
tptTrhaNotifyDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:tptTrhaNotifyDeviceID.setStatus(_A)
_TptTrhaNotifyTimeStamp_Type=Unsigned32
_TptTrhaNotifyTimeStamp_Object=MibScalar
tptTrhaNotifyTimeStamp=_TptTrhaNotifyTimeStamp_Object((1,3,6,1,4,1,10734,3,3,3,1,87),_TptTrhaNotifyTimeStamp_Type())
tptTrhaNotifyTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:tptTrhaNotifyTimeStamp.setStatus(_A)
_TptTrhaNotifyNewState_Type=ConnectionState
_TptTrhaNotifyNewState_Object=MibScalar
tptTrhaNotifyNewState=_TptTrhaNotifyNewState_Object((1,3,6,1,4,1,10734,3,3,3,1,88),_TptTrhaNotifyNewState_Type())
tptTrhaNotifyNewState.setMaxAccess(_B)
if mibBuilder.loadTexts:tptTrhaNotifyNewState.setStatus(_A)
class _TptPerfProtNotifyDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptPerfProtNotifyDeviceID_Type.__name__=_D
_TptPerfProtNotifyDeviceID_Object=MibScalar
tptPerfProtNotifyDeviceID=_TptPerfProtNotifyDeviceID_Object((1,3,6,1,4,1,10734,3,3,3,1,141),_TptPerfProtNotifyDeviceID_Type())
tptPerfProtNotifyDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:tptPerfProtNotifyDeviceID.setStatus(_A)
_TptPerfProtNotifyTimeStamp_Type=Unsigned32
_TptPerfProtNotifyTimeStamp_Object=MibScalar
tptPerfProtNotifyTimeStamp=_TptPerfProtNotifyTimeStamp_Object((1,3,6,1,4,1,10734,3,3,3,1,142),_TptPerfProtNotifyTimeStamp_Type())
tptPerfProtNotifyTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:tptPerfProtNotifyTimeStamp.setStatus(_A)
_TptPerfProtNotifyPhase_Type=PerfProtPhase
_TptPerfProtNotifyPhase_Object=MibScalar
tptPerfProtNotifyPhase=_TptPerfProtNotifyPhase_Object((1,3,6,1,4,1,10734,3,3,3,1,143),_TptPerfProtNotifyPhase_Type())
tptPerfProtNotifyPhase.setMaxAccess(_B)
if mibBuilder.loadTexts:tptPerfProtNotifyPhase.setStatus(_A)
_TptPerfProtNotifyPacketLoss_Type=Unsigned32
_TptPerfProtNotifyPacketLoss_Object=MibScalar
tptPerfProtNotifyPacketLoss=_TptPerfProtNotifyPacketLoss_Object((1,3,6,1,4,1,10734,3,3,3,1,144),_TptPerfProtNotifyPacketLoss_Type())
tptPerfProtNotifyPacketLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:tptPerfProtNotifyPacketLoss.setStatus(_A)
_TptPerfProtNotifyLossThreshold_Type=Unsigned32
_TptPerfProtNotifyLossThreshold_Object=MibScalar
tptPerfProtNotifyLossThreshold=_TptPerfProtNotifyLossThreshold_Object((1,3,6,1,4,1,10734,3,3,3,1,145),_TptPerfProtNotifyLossThreshold_Type())
tptPerfProtNotifyLossThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tptPerfProtNotifyLossThreshold.setStatus(_A)
_TptPerfProtNotifyDuration_Type=Unsigned32
_TptPerfProtNotifyDuration_Object=MibScalar
tptPerfProtNotifyDuration=_TptPerfProtNotifyDuration_Object((1,3,6,1,4,1,10734,3,3,3,1,146),_TptPerfProtNotifyDuration_Type())
tptPerfProtNotifyDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:tptPerfProtNotifyDuration.setStatus(_A)
_TptPerfProtNotifyMissedAlerts_Type=Counter64
_TptPerfProtNotifyMissedAlerts_Object=MibScalar
tptPerfProtNotifyMissedAlerts=_TptPerfProtNotifyMissedAlerts_Object((1,3,6,1,4,1,10734,3,3,3,1,147),_TptPerfProtNotifyMissedAlerts_Type())
tptPerfProtNotifyMissedAlerts.setMaxAccess(_B)
if mibBuilder.loadTexts:tptPerfProtNotifyMissedAlerts.setStatus(_A)
class _TptZphaNotifyDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptZphaNotifyDeviceID_Type.__name__=_D
_TptZphaNotifyDeviceID_Object=MibScalar
tptZphaNotifyDeviceID=_TptZphaNotifyDeviceID_Object((1,3,6,1,4,1,10734,3,3,3,1,161),_TptZphaNotifyDeviceID_Type())
tptZphaNotifyDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:tptZphaNotifyDeviceID.setStatus(_A)
_TptZphaNotifyTimeStamp_Type=Unsigned32
_TptZphaNotifyTimeStamp_Object=MibScalar
tptZphaNotifyTimeStamp=_TptZphaNotifyTimeStamp_Object((1,3,6,1,4,1,10734,3,3,3,1,162),_TptZphaNotifyTimeStamp_Type())
tptZphaNotifyTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:tptZphaNotifyTimeStamp.setStatus(_A)
class _TptZphaNotifySegmentName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_TptZphaNotifySegmentName_Type.__name__=_D
_TptZphaNotifySegmentName_Object=MibScalar
tptZphaNotifySegmentName=_TptZphaNotifySegmentName_Object((1,3,6,1,4,1,10734,3,3,3,1,163),_TptZphaNotifySegmentName_Type())
tptZphaNotifySegmentName.setMaxAccess(_B)
if mibBuilder.loadTexts:tptZphaNotifySegmentName.setStatus(_A)
_TptZphaNotifyNewState_Type=ZphaState
_TptZphaNotifyNewState_Object=MibScalar
tptZphaNotifyNewState=_TptZphaNotifyNewState_Object((1,3,6,1,4,1,10734,3,3,3,1,164),_TptZphaNotifyNewState_Type())
tptZphaNotifyNewState.setMaxAccess(_B)
if mibBuilder.loadTexts:tptZphaNotifyNewState.setStatus(_A)
tptIhaNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,15))
tptIhaNotify.setObjects(*((_C,_H),(_C,_I),(_C,_J),(_C,_K)))
if mibBuilder.loadTexts:tptIhaNotify.setStatus(_A)
tptTrhaNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,18))
tptTrhaNotify.setObjects(*((_C,_L),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:tptTrhaNotify.setStatus(_A)
tptPerfProtNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,21))
tptPerfProtNotify.setObjects(*((_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_S),(_C,_T),(_C,_U)))
if mibBuilder.loadTexts:tptPerfProtNotify.setStatus(_A)
tptZphaNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,24))
tptZphaNotify.setObjects(*((_C,_V),(_C,_W),(_C,_X),(_C,_Y)))
if mibBuilder.loadTexts:tptZphaNotify.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FaultState':FaultState,'FaultCause':FaultCause,'ConnectionState':ConnectionState,'PerfProtPhase':PerfProtPhase,'ZphaState':ZphaState,'ZphaAction':ZphaAction,'ZphaMode':ZphaMode,'ZphaPresent':ZphaPresent,'tpt-high-avail-objs':tpt_high_avail_objs,'highAvailTimeStamp':highAvailTimeStamp,'highAvailFaultState':highAvailFaultState,'highAvailFaultCause':highAvailFaultCause,'highAvailThresholdEnabled':highAvailThresholdEnabled,'highAvailThresholdPercent':highAvailThresholdPercent,'highAvailEnabled':highAvailEnabled,'highAvailTransparentState':highAvailTransparentState,'highAvailTransparentEnabled':highAvailTransparentEnabled,'highAvailTransparentPartner':highAvailTransparentPartner,'highAvailZeroPowerState':highAvailZeroPowerState,'highAvailZeroPowerQuantity':highAvailZeroPowerQuantity,'highAvailZeroPowerTable':highAvailZeroPowerTable,'highAvailZeroPowerEntry':highAvailZeroPowerEntry,_G:highAvailZeroPowerIndex,'highAvailZeroPowerSegment':highAvailZeroPowerSegment,'highAvailZeroPowerActive':highAvailZeroPowerActive,'highAvailZeroPowerAction':highAvailZeroPowerAction,'highAvailZeroPowerMode':highAvailZeroPowerMode,'highAvailZeroPowerPresence':highAvailZeroPowerPresence,'tptIhaNotify':tptIhaNotify,'tptTrhaNotify':tptTrhaNotify,'tptPerfProtNotify':tptPerfProtNotify,'tptZphaNotify':tptZphaNotify,_H:tptIhaNotifyDeviceID,_I:tptIhaNotifyTimeStamp,_J:tptIhaNotifyFaultState,_K:tptIhaNotifyFaultCause,_L:tptTrhaNotifyDeviceID,_M:tptTrhaNotifyTimeStamp,_N:tptTrhaNotifyNewState,_O:tptPerfProtNotifyDeviceID,_P:tptPerfProtNotifyTimeStamp,_Q:tptPerfProtNotifyPhase,_R:tptPerfProtNotifyPacketLoss,_S:tptPerfProtNotifyLossThreshold,_T:tptPerfProtNotifyDuration,_U:tptPerfProtNotifyMissedAlerts,_V:tptZphaNotifyDeviceID,_W:tptZphaNotifyTimeStamp,_X:tptZphaNotifySegmentName,_Y:tptZphaNotifyNewState})