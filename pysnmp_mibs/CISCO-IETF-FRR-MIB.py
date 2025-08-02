_AA='cmplsFrrNotifGroupRev1'
_A9='cmplsFrrNotifGroup'
_A8='cmplsFrrUnProtected'
_A7='deprecated'
_A6='cmplsFrrFacRouteProtectingTunProtectionType'
_A5='cmplsFrrFacRouteProtectingTunResvBw'
_A4='cmplsFrrFacRouteProtectedTunStatus'
_A3='cmplsFrrLogEventReasonString'
_A2='cmplsFrrLogEventDuration'
_A1='cmplsFrrLogEventType'
_A0='cmplsFrrLogInterface'
_z='cmplsFrrLogEventTime'
_y='cmplsFrrConstRowStatus'
_x='cmplsFrrConstHopLimit'
_w='cmplsFrrConstExclAllAffinity'
_v='cmplsFrrConstInclAllAffinity'
_u='cmplsFrrConstInclAnyAffinity'
_t='cmplsFrrConstHoldingPrio'
_s='cmplsFrrConstSetupPrio'
_r='cmplsFrrNotifMaxRate'
_q='cmplsFrrLogTableCurrEntries'
_p='cmplsFrrLogTableMaxEntries'
_o='cmplsFrrNotifsEnabled'
_n='cmplsFrrActProtectedLSPs'
_m='cmplsFrrActProtectedTuns'
_l='cmplsFrrConfProtectingTuns'
_k='cmplsFrrActProtectedIfs'
_j='cmplsFrrNumOfConfIfs'
_i='cmplsFrrSwitchover'
_h='cmplsFrrDetourOriginating'
_g='cmplsFrrDetourOutgoing'
_f='cmplsFrrDetourIncoming'
_e='cmplsFrrFacRouteProtectedTunEgressLSRId'
_d='cmplsFrrFacRouteProtectedTunIngressLSRId'
_c='cmplsFrrFacRouteProtectedTunInstance'
_b='cmplsFrrFacRouteProtectedTunIndex'
_a='cmplsFrrFacRouteProtectingTunIndex'
_Z='cmplsFrrFacRouteProtectedIfIndex'
_Y='cmplsFrrLogIndex'
_X='cmplsFrrConstTunnelInstance'
_W='cmplsFrrConstTunnelIndex'
_V='cmplsFrrConstIfIndex'
_U='TruthValue'
_T='MplsBitRate'
_S='OctetString'
_R='cmplsFrrFacRouteDBGroup'
_Q='cmplsFrrLogGroup'
_P='cmplsFrrConstGroup'
_O='cmplsFrrScalarGroup'
_N='cmplsFrrProtected'
_M='cmplsFrrConstProtectionMethod'
_L='cmplsFrrConstNumProtectedTunOnIf'
_K='cmplsFrrConstNumProtectingTunOnIf'
_J='cmplsFrrConstBandwidth'
_I='read-write'
_H='MplsTunnelAffinity'
_G='Integer32'
_F='read-create'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='CISCO-IETF-FRR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
MplsBitRate,MplsLsrIdentifier,MplsTunnelAffinity,MplsTunnelIndex,MplsTunnelInstanceIndex=mibBuilder.importSymbols('MPLS-TC-STD-MIB',_T,'MplsLsrIdentifier',_H,'MplsTunnelIndex','MplsTunnelInstanceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_U)
cmplsFrrMIB=ModuleIdentity((1,3,6,1,4,1,9,10,98))
if mibBuilder.loadTexts:cmplsFrrMIB.setRevisions(('2008-04-29 12:00','2002-11-05 12:00','2002-11-01 12:00','2002-03-22 12:00'))
class MplsFrrDetourIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CmplsFrrNotif_ObjectIdentity=ObjectIdentity
cmplsFrrNotif=_CmplsFrrNotif_ObjectIdentity((1,3,6,1,4,1,9,10,98,0))
_CmplsFrrScalars_ObjectIdentity=ObjectIdentity
cmplsFrrScalars=_CmplsFrrScalars_ObjectIdentity((1,3,6,1,4,1,9,10,98,1))
class _CmplsFrrDetourIncoming_Type(Unsigned32):defaultValue=0
_CmplsFrrDetourIncoming_Type.__name__=_D
_CmplsFrrDetourIncoming_Object=MibScalar
cmplsFrrDetourIncoming=_CmplsFrrDetourIncoming_Object((1,3,6,1,4,1,9,10,98,1,1),_CmplsFrrDetourIncoming_Type())
cmplsFrrDetourIncoming.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrDetourIncoming.setStatus(_B)
class _CmplsFrrDetourOutgoing_Type(Unsigned32):defaultValue=0
_CmplsFrrDetourOutgoing_Type.__name__=_D
_CmplsFrrDetourOutgoing_Object=MibScalar
cmplsFrrDetourOutgoing=_CmplsFrrDetourOutgoing_Object((1,3,6,1,4,1,9,10,98,1,2),_CmplsFrrDetourOutgoing_Type())
cmplsFrrDetourOutgoing.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrDetourOutgoing.setStatus(_B)
class _CmplsFrrDetourOriginating_Type(Unsigned32):defaultValue=0
_CmplsFrrDetourOriginating_Type.__name__=_D
_CmplsFrrDetourOriginating_Object=MibScalar
cmplsFrrDetourOriginating=_CmplsFrrDetourOriginating_Object((1,3,6,1,4,1,9,10,98,1,3),_CmplsFrrDetourOriginating_Type())
cmplsFrrDetourOriginating.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrDetourOriginating.setStatus(_B)
class _CmplsFrrSwitchover_Type(Unsigned32):defaultValue=0
_CmplsFrrSwitchover_Type.__name__=_D
_CmplsFrrSwitchover_Object=MibScalar
cmplsFrrSwitchover=_CmplsFrrSwitchover_Object((1,3,6,1,4,1,9,10,98,1,4),_CmplsFrrSwitchover_Type())
cmplsFrrSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrSwitchover.setStatus(_B)
class _CmplsFrrNumOfConfIfs_Type(Unsigned32):defaultValue=0
_CmplsFrrNumOfConfIfs_Type.__name__=_D
_CmplsFrrNumOfConfIfs_Object=MibScalar
cmplsFrrNumOfConfIfs=_CmplsFrrNumOfConfIfs_Object((1,3,6,1,4,1,9,10,98,1,5),_CmplsFrrNumOfConfIfs_Type())
cmplsFrrNumOfConfIfs.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrNumOfConfIfs.setStatus(_B)
class _CmplsFrrActProtectedIfs_Type(Unsigned32):defaultValue=0
_CmplsFrrActProtectedIfs_Type.__name__=_D
_CmplsFrrActProtectedIfs_Object=MibScalar
cmplsFrrActProtectedIfs=_CmplsFrrActProtectedIfs_Object((1,3,6,1,4,1,9,10,98,1,6),_CmplsFrrActProtectedIfs_Type())
cmplsFrrActProtectedIfs.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrActProtectedIfs.setStatus(_B)
class _CmplsFrrConfProtectingTuns_Type(Unsigned32):defaultValue=0
_CmplsFrrConfProtectingTuns_Type.__name__=_D
_CmplsFrrConfProtectingTuns_Object=MibScalar
cmplsFrrConfProtectingTuns=_CmplsFrrConfProtectingTuns_Object((1,3,6,1,4,1,9,10,98,1,7),_CmplsFrrConfProtectingTuns_Type())
cmplsFrrConfProtectingTuns.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrConfProtectingTuns.setStatus(_B)
class _CmplsFrrActProtectedTuns_Type(Unsigned32):defaultValue=0
_CmplsFrrActProtectedTuns_Type.__name__=_D
_CmplsFrrActProtectedTuns_Object=MibScalar
cmplsFrrActProtectedTuns=_CmplsFrrActProtectedTuns_Object((1,3,6,1,4,1,9,10,98,1,8),_CmplsFrrActProtectedTuns_Type())
cmplsFrrActProtectedTuns.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrActProtectedTuns.setStatus(_B)
class _CmplsFrrActProtectedLSPs_Type(Unsigned32):defaultValue=0
_CmplsFrrActProtectedLSPs_Type.__name__=_D
_CmplsFrrActProtectedLSPs_Object=MibScalar
cmplsFrrActProtectedLSPs=_CmplsFrrActProtectedLSPs_Object((1,3,6,1,4,1,9,10,98,1,9),_CmplsFrrActProtectedLSPs_Type())
cmplsFrrActProtectedLSPs.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrActProtectedLSPs.setStatus(_B)
class _CmplsFrrConstProtectionMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('oneToOneBackup',0),('facilityBackup',1)))
_CmplsFrrConstProtectionMethod_Type.__name__=_G
_CmplsFrrConstProtectionMethod_Object=MibScalar
cmplsFrrConstProtectionMethod=_CmplsFrrConstProtectionMethod_Object((1,3,6,1,4,1,9,10,98,1,10),_CmplsFrrConstProtectionMethod_Type())
cmplsFrrConstProtectionMethod.setMaxAccess(_I)
if mibBuilder.loadTexts:cmplsFrrConstProtectionMethod.setStatus(_B)
class _CmplsFrrNotifsEnabled_Type(TruthValue):defaultValue=2
_CmplsFrrNotifsEnabled_Type.__name__=_U
_CmplsFrrNotifsEnabled_Object=MibScalar
cmplsFrrNotifsEnabled=_CmplsFrrNotifsEnabled_Object((1,3,6,1,4,1,9,10,98,1,11),_CmplsFrrNotifsEnabled_Type())
cmplsFrrNotifsEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:cmplsFrrNotifsEnabled.setStatus(_B)
class _CmplsFrrLogTableMaxEntries_Type(Unsigned32):defaultValue=0
_CmplsFrrLogTableMaxEntries_Type.__name__=_D
_CmplsFrrLogTableMaxEntries_Object=MibScalar
cmplsFrrLogTableMaxEntries=_CmplsFrrLogTableMaxEntries_Object((1,3,6,1,4,1,9,10,98,1,12),_CmplsFrrLogTableMaxEntries_Type())
cmplsFrrLogTableMaxEntries.setMaxAccess(_I)
if mibBuilder.loadTexts:cmplsFrrLogTableMaxEntries.setStatus(_B)
_CmplsFrrLogTableCurrEntries_Type=Counter32
_CmplsFrrLogTableCurrEntries_Object=MibScalar
cmplsFrrLogTableCurrEntries=_CmplsFrrLogTableCurrEntries_Object((1,3,6,1,4,1,9,10,98,1,13),_CmplsFrrLogTableCurrEntries_Type())
cmplsFrrLogTableCurrEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrLogTableCurrEntries.setStatus(_B)
class _CmplsFrrNotifMaxRate_Type(Unsigned32):defaultValue=0
_CmplsFrrNotifMaxRate_Type.__name__=_D
_CmplsFrrNotifMaxRate_Object=MibScalar
cmplsFrrNotifMaxRate=_CmplsFrrNotifMaxRate_Object((1,3,6,1,4,1,9,10,98,1,14),_CmplsFrrNotifMaxRate_Type())
cmplsFrrNotifMaxRate.setMaxAccess(_I)
if mibBuilder.loadTexts:cmplsFrrNotifMaxRate.setStatus(_B)
_CmplsFrrObjects_ObjectIdentity=ObjectIdentity
cmplsFrrObjects=_CmplsFrrObjects_ObjectIdentity((1,3,6,1,4,1,9,10,98,2))
_CmplsFrrGeneralObjects_ObjectIdentity=ObjectIdentity
cmplsFrrGeneralObjects=_CmplsFrrGeneralObjects_ObjectIdentity((1,3,6,1,4,1,9,10,98,2,1))
_CmplsFrrConstTable_Object=MibTable
cmplsFrrConstTable=_CmplsFrrConstTable_Object((1,3,6,1,4,1,9,10,98,2,1,1))
if mibBuilder.loadTexts:cmplsFrrConstTable.setStatus(_B)
_CmplsFrrConstEntry_Object=MibTableRow
cmplsFrrConstEntry=_CmplsFrrConstEntry_Object((1,3,6,1,4,1,9,10,98,2,1,1,1))
cmplsFrrConstEntry.setIndexNames((0,_A,_V),(0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:cmplsFrrConstEntry.setStatus(_B)
_CmplsFrrConstIfIndex_Type=InterfaceIndexOrZero
_CmplsFrrConstIfIndex_Object=MibTableColumn
cmplsFrrConstIfIndex=_CmplsFrrConstIfIndex_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,1),_CmplsFrrConstIfIndex_Type())
cmplsFrrConstIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cmplsFrrConstIfIndex.setStatus(_B)
_CmplsFrrConstTunnelIndex_Type=MplsTunnelIndex
_CmplsFrrConstTunnelIndex_Object=MibTableColumn
cmplsFrrConstTunnelIndex=_CmplsFrrConstTunnelIndex_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,2),_CmplsFrrConstTunnelIndex_Type())
cmplsFrrConstTunnelIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cmplsFrrConstTunnelIndex.setStatus(_B)
_CmplsFrrConstTunnelInstance_Type=MplsTunnelInstanceIndex
_CmplsFrrConstTunnelInstance_Object=MibTableColumn
cmplsFrrConstTunnelInstance=_CmplsFrrConstTunnelInstance_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,3),_CmplsFrrConstTunnelInstance_Type())
cmplsFrrConstTunnelInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:cmplsFrrConstTunnelInstance.setStatus(_B)
class _CmplsFrrConstSetupPrio_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CmplsFrrConstSetupPrio_Type.__name__=_D
_CmplsFrrConstSetupPrio_Object=MibTableColumn
cmplsFrrConstSetupPrio=_CmplsFrrConstSetupPrio_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,4),_CmplsFrrConstSetupPrio_Type())
cmplsFrrConstSetupPrio.setMaxAccess(_F)
if mibBuilder.loadTexts:cmplsFrrConstSetupPrio.setStatus(_B)
class _CmplsFrrConstHoldingPrio_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CmplsFrrConstHoldingPrio_Type.__name__=_D
_CmplsFrrConstHoldingPrio_Object=MibTableColumn
cmplsFrrConstHoldingPrio=_CmplsFrrConstHoldingPrio_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,5),_CmplsFrrConstHoldingPrio_Type())
cmplsFrrConstHoldingPrio.setMaxAccess(_F)
if mibBuilder.loadTexts:cmplsFrrConstHoldingPrio.setStatus(_B)
class _CmplsFrrConstInclAnyAffinity_Type(MplsTunnelAffinity):defaultValue=0
_CmplsFrrConstInclAnyAffinity_Type.__name__=_H
_CmplsFrrConstInclAnyAffinity_Object=MibTableColumn
cmplsFrrConstInclAnyAffinity=_CmplsFrrConstInclAnyAffinity_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,6),_CmplsFrrConstInclAnyAffinity_Type())
cmplsFrrConstInclAnyAffinity.setMaxAccess(_F)
if mibBuilder.loadTexts:cmplsFrrConstInclAnyAffinity.setStatus(_B)
class _CmplsFrrConstInclAllAffinity_Type(MplsTunnelAffinity):defaultValue=0
_CmplsFrrConstInclAllAffinity_Type.__name__=_H
_CmplsFrrConstInclAllAffinity_Object=MibTableColumn
cmplsFrrConstInclAllAffinity=_CmplsFrrConstInclAllAffinity_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,7),_CmplsFrrConstInclAllAffinity_Type())
cmplsFrrConstInclAllAffinity.setMaxAccess(_F)
if mibBuilder.loadTexts:cmplsFrrConstInclAllAffinity.setStatus(_B)
class _CmplsFrrConstExclAllAffinity_Type(MplsTunnelAffinity):defaultValue=0
_CmplsFrrConstExclAllAffinity_Type.__name__=_H
_CmplsFrrConstExclAllAffinity_Object=MibTableColumn
cmplsFrrConstExclAllAffinity=_CmplsFrrConstExclAllAffinity_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,8),_CmplsFrrConstExclAllAffinity_Type())
cmplsFrrConstExclAllAffinity.setMaxAccess(_F)
if mibBuilder.loadTexts:cmplsFrrConstExclAllAffinity.setStatus(_B)
class _CmplsFrrConstHopLimit_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CmplsFrrConstHopLimit_Type.__name__=_D
_CmplsFrrConstHopLimit_Object=MibTableColumn
cmplsFrrConstHopLimit=_CmplsFrrConstHopLimit_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,9),_CmplsFrrConstHopLimit_Type())
cmplsFrrConstHopLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:cmplsFrrConstHopLimit.setStatus(_B)
class _CmplsFrrConstBandwidth_Type(MplsBitRate):defaultValue=1
_CmplsFrrConstBandwidth_Type.__name__=_T
_CmplsFrrConstBandwidth_Object=MibTableColumn
cmplsFrrConstBandwidth=_CmplsFrrConstBandwidth_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,10),_CmplsFrrConstBandwidth_Type())
cmplsFrrConstBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cmplsFrrConstBandwidth.setStatus(_B)
_CmplsFrrConstRowStatus_Type=RowStatus
_CmplsFrrConstRowStatus_Object=MibTableColumn
cmplsFrrConstRowStatus=_CmplsFrrConstRowStatus_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,11),_CmplsFrrConstRowStatus_Type())
cmplsFrrConstRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cmplsFrrConstRowStatus.setStatus(_B)
_CmplsFrrConstNumProtectingTunOnIf_Type=Gauge32
_CmplsFrrConstNumProtectingTunOnIf_Object=MibTableColumn
cmplsFrrConstNumProtectingTunOnIf=_CmplsFrrConstNumProtectingTunOnIf_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,12),_CmplsFrrConstNumProtectingTunOnIf_Type())
cmplsFrrConstNumProtectingTunOnIf.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrConstNumProtectingTunOnIf.setStatus(_B)
_CmplsFrrConstNumProtectedTunOnIf_Type=Gauge32
_CmplsFrrConstNumProtectedTunOnIf_Object=MibTableColumn
cmplsFrrConstNumProtectedTunOnIf=_CmplsFrrConstNumProtectedTunOnIf_Object((1,3,6,1,4,1,9,10,98,2,1,1,1,13),_CmplsFrrConstNumProtectedTunOnIf_Type())
cmplsFrrConstNumProtectedTunOnIf.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrConstNumProtectedTunOnIf.setStatus(_B)
_CmplsFrrLogTable_Object=MibTable
cmplsFrrLogTable=_CmplsFrrLogTable_Object((1,3,6,1,4,1,9,10,98,2,1,2))
if mibBuilder.loadTexts:cmplsFrrLogTable.setStatus(_B)
_CmplsFrrLogEntry_Object=MibTableRow
cmplsFrrLogEntry=_CmplsFrrLogEntry_Object((1,3,6,1,4,1,9,10,98,2,1,2,1))
cmplsFrrLogEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:cmplsFrrLogEntry.setStatus(_B)
_CmplsFrrLogIndex_Type=Unsigned32
_CmplsFrrLogIndex_Object=MibTableColumn
cmplsFrrLogIndex=_CmplsFrrLogIndex_Object((1,3,6,1,4,1,9,10,98,2,1,2,1,1),_CmplsFrrLogIndex_Type())
cmplsFrrLogIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cmplsFrrLogIndex.setStatus(_B)
_CmplsFrrLogEventTime_Type=TimeStamp
_CmplsFrrLogEventTime_Object=MibTableColumn
cmplsFrrLogEventTime=_CmplsFrrLogEventTime_Object((1,3,6,1,4,1,9,10,98,2,1,2,1,2),_CmplsFrrLogEventTime_Type())
cmplsFrrLogEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrLogEventTime.setStatus(_B)
_CmplsFrrLogInterface_Type=InterfaceIndexOrZero
_CmplsFrrLogInterface_Object=MibTableColumn
cmplsFrrLogInterface=_CmplsFrrLogInterface_Object((1,3,6,1,4,1,9,10,98,2,1,2,1,3),_CmplsFrrLogInterface_Type())
cmplsFrrLogInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrLogInterface.setStatus(_B)
class _CmplsFrrLogEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('protected',2)))
_CmplsFrrLogEventType_Type.__name__=_G
_CmplsFrrLogEventType_Object=MibTableColumn
cmplsFrrLogEventType=_CmplsFrrLogEventType_Object((1,3,6,1,4,1,9,10,98,2,1,2,1,4),_CmplsFrrLogEventType_Type())
cmplsFrrLogEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrLogEventType.setStatus(_B)
_CmplsFrrLogEventDuration_Type=TimeTicks
_CmplsFrrLogEventDuration_Object=MibTableColumn
cmplsFrrLogEventDuration=_CmplsFrrLogEventDuration_Object((1,3,6,1,4,1,9,10,98,2,1,2,1,5),_CmplsFrrLogEventDuration_Type())
cmplsFrrLogEventDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrLogEventDuration.setStatus(_B)
class _CmplsFrrLogEventReasonString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_CmplsFrrLogEventReasonString_Type.__name__=_S
_CmplsFrrLogEventReasonString_Object=MibTableColumn
cmplsFrrLogEventReasonString=_CmplsFrrLogEventReasonString_Object((1,3,6,1,4,1,9,10,98,2,1,2,1,6),_CmplsFrrLogEventReasonString_Type())
cmplsFrrLogEventReasonString.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrLogEventReasonString.setStatus(_B)
_CmplsFrr1to1Objects_ObjectIdentity=ObjectIdentity
cmplsFrr1to1Objects=_CmplsFrr1to1Objects_ObjectIdentity((1,3,6,1,4,1,9,10,98,2,2))
_CmplsFrrFacObjects_ObjectIdentity=ObjectIdentity
cmplsFrrFacObjects=_CmplsFrrFacObjects_ObjectIdentity((1,3,6,1,4,1,9,10,98,2,3))
_CmplsFrrFacRouteDBTable_Object=MibTable
cmplsFrrFacRouteDBTable=_CmplsFrrFacRouteDBTable_Object((1,3,6,1,4,1,9,10,98,2,3,1))
if mibBuilder.loadTexts:cmplsFrrFacRouteDBTable.setStatus(_B)
_CmplsFrrFacRouteDBEntry_Object=MibTableRow
cmplsFrrFacRouteDBEntry=_CmplsFrrFacRouteDBEntry_Object((1,3,6,1,4,1,9,10,98,2,3,1,1))
cmplsFrrFacRouteDBEntry.setIndexNames((0,_A,_Z),(0,_A,_a),(0,_A,_b),(0,_A,_c),(0,_A,_d),(0,_A,_e))
if mibBuilder.loadTexts:cmplsFrrFacRouteDBEntry.setStatus(_B)
_CmplsFrrFacRouteProtectedIfIndex_Type=InterfaceIndex
_CmplsFrrFacRouteProtectedIfIndex_Object=MibTableColumn
cmplsFrrFacRouteProtectedIfIndex=_CmplsFrrFacRouteProtectedIfIndex_Object((1,3,6,1,4,1,9,10,98,2,3,1,1,1),_CmplsFrrFacRouteProtectedIfIndex_Type())
cmplsFrrFacRouteProtectedIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cmplsFrrFacRouteProtectedIfIndex.setStatus(_B)
_CmplsFrrFacRouteProtectingTunIndex_Type=MplsTunnelIndex
_CmplsFrrFacRouteProtectingTunIndex_Object=MibTableColumn
cmplsFrrFacRouteProtectingTunIndex=_CmplsFrrFacRouteProtectingTunIndex_Object((1,3,6,1,4,1,9,10,98,2,3,1,1,2),_CmplsFrrFacRouteProtectingTunIndex_Type())
cmplsFrrFacRouteProtectingTunIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cmplsFrrFacRouteProtectingTunIndex.setStatus(_B)
_CmplsFrrFacRouteProtectedTunIndex_Type=MplsTunnelIndex
_CmplsFrrFacRouteProtectedTunIndex_Object=MibTableColumn
cmplsFrrFacRouteProtectedTunIndex=_CmplsFrrFacRouteProtectedTunIndex_Object((1,3,6,1,4,1,9,10,98,2,3,1,1,3),_CmplsFrrFacRouteProtectedTunIndex_Type())
cmplsFrrFacRouteProtectedTunIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cmplsFrrFacRouteProtectedTunIndex.setStatus(_B)
_CmplsFrrFacRouteProtectedTunInstance_Type=MplsTunnelInstanceIndex
_CmplsFrrFacRouteProtectedTunInstance_Object=MibTableColumn
cmplsFrrFacRouteProtectedTunInstance=_CmplsFrrFacRouteProtectedTunInstance_Object((1,3,6,1,4,1,9,10,98,2,3,1,1,4),_CmplsFrrFacRouteProtectedTunInstance_Type())
cmplsFrrFacRouteProtectedTunInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:cmplsFrrFacRouteProtectedTunInstance.setStatus(_B)
_CmplsFrrFacRouteProtectedTunIngressLSRId_Type=MplsLsrIdentifier
_CmplsFrrFacRouteProtectedTunIngressLSRId_Object=MibTableColumn
cmplsFrrFacRouteProtectedTunIngressLSRId=_CmplsFrrFacRouteProtectedTunIngressLSRId_Object((1,3,6,1,4,1,9,10,98,2,3,1,1,5),_CmplsFrrFacRouteProtectedTunIngressLSRId_Type())
cmplsFrrFacRouteProtectedTunIngressLSRId.setMaxAccess(_E)
if mibBuilder.loadTexts:cmplsFrrFacRouteProtectedTunIngressLSRId.setStatus(_B)
_CmplsFrrFacRouteProtectedTunEgressLSRId_Type=MplsLsrIdentifier
_CmplsFrrFacRouteProtectedTunEgressLSRId_Object=MibTableColumn
cmplsFrrFacRouteProtectedTunEgressLSRId=_CmplsFrrFacRouteProtectedTunEgressLSRId_Object((1,3,6,1,4,1,9,10,98,2,3,1,1,6),_CmplsFrrFacRouteProtectedTunEgressLSRId_Type())
cmplsFrrFacRouteProtectedTunEgressLSRId.setMaxAccess(_E)
if mibBuilder.loadTexts:cmplsFrrFacRouteProtectedTunEgressLSRId.setStatus(_B)
class _CmplsFrrFacRouteProtectedTunStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('ready',2),('partial',3)))
_CmplsFrrFacRouteProtectedTunStatus_Type.__name__=_G
_CmplsFrrFacRouteProtectedTunStatus_Object=MibTableColumn
cmplsFrrFacRouteProtectedTunStatus=_CmplsFrrFacRouteProtectedTunStatus_Object((1,3,6,1,4,1,9,10,98,2,3,1,1,7),_CmplsFrrFacRouteProtectedTunStatus_Type())
cmplsFrrFacRouteProtectedTunStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrFacRouteProtectedTunStatus.setStatus(_B)
_CmplsFrrFacRouteProtectingTunResvBw_Type=MplsBitRate
_CmplsFrrFacRouteProtectingTunResvBw_Object=MibTableColumn
cmplsFrrFacRouteProtectingTunResvBw=_CmplsFrrFacRouteProtectingTunResvBw_Object((1,3,6,1,4,1,9,10,98,2,3,1,1,8),_CmplsFrrFacRouteProtectingTunResvBw_Type())
cmplsFrrFacRouteProtectingTunResvBw.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsFrrFacRouteProtectingTunResvBw.setStatus(_B)
class _CmplsFrrFacRouteProtectingTunProtectionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('linkProtection',0),('nodeProtection',1)))
_CmplsFrrFacRouteProtectingTunProtectionType_Type.__name__=_G
_CmplsFrrFacRouteProtectingTunProtectionType_Object=MibTableColumn
cmplsFrrFacRouteProtectingTunProtectionType=_CmplsFrrFacRouteProtectingTunProtectionType_Object((1,3,6,1,4,1,9,10,98,2,3,1,1,9),_CmplsFrrFacRouteProtectingTunProtectionType_Type())
cmplsFrrFacRouteProtectingTunProtectionType.setMaxAccess(_F)
if mibBuilder.loadTexts:cmplsFrrFacRouteProtectingTunProtectionType.setStatus(_B)
_CmplsFrrConformance_ObjectIdentity=ObjectIdentity
cmplsFrrConformance=_CmplsFrrConformance_ObjectIdentity((1,3,6,1,4,1,9,10,98,3))
_CmplsFrrGroups_ObjectIdentity=ObjectIdentity
cmplsFrrGroups=_CmplsFrrGroups_ObjectIdentity((1,3,6,1,4,1,9,10,98,3,1))
_CmplsFrrCompliances_ObjectIdentity=ObjectIdentity
cmplsFrrCompliances=_CmplsFrrCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,98,3,2))
cmplsFrrScalarGroup=ObjectGroup((1,3,6,1,4,1,9,10,98,3,1,1))
cmplsFrrScalarGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_M),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:cmplsFrrScalarGroup.setStatus(_B)
cmplsFrrConstGroup=ObjectGroup((1,3,6,1,4,1,9,10,98,3,1,2))
cmplsFrrConstGroup.setObjects(*((_A,_M),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_J),(_A,_y),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cmplsFrrConstGroup.setStatus(_B)
cmplsFrrLogGroup=ObjectGroup((1,3,6,1,4,1,9,10,98,3,1,4))
cmplsFrrLogGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:cmplsFrrLogGroup.setStatus(_B)
cmplsFrrFacRouteDBGroup=ObjectGroup((1,3,6,1,4,1,9,10,98,3,1,6))
cmplsFrrFacRouteDBGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:cmplsFrrFacRouteDBGroup.setStatus(_B)
cmplsFrrProtected=NotificationType((1,3,6,1,4,1,9,10,98,0,1))
cmplsFrrProtected.setObjects(*((_A,_K),(_A,_L),(_A,_J)))
if mibBuilder.loadTexts:cmplsFrrProtected.setStatus(_B)
cmplsFrrUnProtected=NotificationType((1,3,6,1,4,1,9,10,98,0,2))
cmplsFrrUnProtected.setObjects(*((_A,_K),(_A,_L),(_A,_J)))
if mibBuilder.loadTexts:cmplsFrrUnProtected.setStatus(_B)
cmplsFrrNotifGroup=NotificationGroup((1,3,6,1,4,1,9,10,98,3,1,7))
cmplsFrrNotifGroup.setObjects((_A,_N))
if mibBuilder.loadTexts:cmplsFrrNotifGroup.setStatus(_A7)
cmplsFrrNotifGroupRev1=NotificationGroup((1,3,6,1,4,1,9,10,98,3,1,8))
cmplsFrrNotifGroupRev1.setObjects(*((_A,_N),(_A,_A8)))
if mibBuilder.loadTexts:cmplsFrrNotifGroupRev1.setStatus(_B)
cmplsFrrModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,98,3,2,1))
cmplsFrrModuleCompliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_A9)))
if mibBuilder.loadTexts:cmplsFrrModuleCompliance.setStatus(_A7)
cmplsFrrModuleComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,98,3,2,2))
cmplsFrrModuleComplianceRev1.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_AA)))
if mibBuilder.loadTexts:cmplsFrrModuleComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'MplsFrrDetourIndex':MplsFrrDetourIndex,'cmplsFrrMIB':cmplsFrrMIB,'cmplsFrrNotif':cmplsFrrNotif,_N:cmplsFrrProtected,_A8:cmplsFrrUnProtected,'cmplsFrrScalars':cmplsFrrScalars,_f:cmplsFrrDetourIncoming,_g:cmplsFrrDetourOutgoing,_h:cmplsFrrDetourOriginating,_i:cmplsFrrSwitchover,_j:cmplsFrrNumOfConfIfs,_k:cmplsFrrActProtectedIfs,_l:cmplsFrrConfProtectingTuns,_m:cmplsFrrActProtectedTuns,_n:cmplsFrrActProtectedLSPs,_M:cmplsFrrConstProtectionMethod,_o:cmplsFrrNotifsEnabled,_p:cmplsFrrLogTableMaxEntries,_q:cmplsFrrLogTableCurrEntries,_r:cmplsFrrNotifMaxRate,'cmplsFrrObjects':cmplsFrrObjects,'cmplsFrrGeneralObjects':cmplsFrrGeneralObjects,'cmplsFrrConstTable':cmplsFrrConstTable,'cmplsFrrConstEntry':cmplsFrrConstEntry,_V:cmplsFrrConstIfIndex,_W:cmplsFrrConstTunnelIndex,_X:cmplsFrrConstTunnelInstance,_s:cmplsFrrConstSetupPrio,_t:cmplsFrrConstHoldingPrio,_u:cmplsFrrConstInclAnyAffinity,_v:cmplsFrrConstInclAllAffinity,_w:cmplsFrrConstExclAllAffinity,_x:cmplsFrrConstHopLimit,_J:cmplsFrrConstBandwidth,_y:cmplsFrrConstRowStatus,_K:cmplsFrrConstNumProtectingTunOnIf,_L:cmplsFrrConstNumProtectedTunOnIf,'cmplsFrrLogTable':cmplsFrrLogTable,'cmplsFrrLogEntry':cmplsFrrLogEntry,_Y:cmplsFrrLogIndex,_z:cmplsFrrLogEventTime,_A0:cmplsFrrLogInterface,_A1:cmplsFrrLogEventType,_A2:cmplsFrrLogEventDuration,_A3:cmplsFrrLogEventReasonString,'cmplsFrr1to1Objects':cmplsFrr1to1Objects,'cmplsFrrFacObjects':cmplsFrrFacObjects,'cmplsFrrFacRouteDBTable':cmplsFrrFacRouteDBTable,'cmplsFrrFacRouteDBEntry':cmplsFrrFacRouteDBEntry,_Z:cmplsFrrFacRouteProtectedIfIndex,_a:cmplsFrrFacRouteProtectingTunIndex,_b:cmplsFrrFacRouteProtectedTunIndex,_c:cmplsFrrFacRouteProtectedTunInstance,_d:cmplsFrrFacRouteProtectedTunIngressLSRId,_e:cmplsFrrFacRouteProtectedTunEgressLSRId,_A4:cmplsFrrFacRouteProtectedTunStatus,_A5:cmplsFrrFacRouteProtectingTunResvBw,_A6:cmplsFrrFacRouteProtectingTunProtectionType,'cmplsFrrConformance':cmplsFrrConformance,'cmplsFrrGroups':cmplsFrrGroups,_O:cmplsFrrScalarGroup,_P:cmplsFrrConstGroup,_Q:cmplsFrrLogGroup,_R:cmplsFrrFacRouteDBGroup,_A9:cmplsFrrNotifGroup,_AA:cmplsFrrNotifGroupRev1,'cmplsFrrCompliances':cmplsFrrCompliances,'cmplsFrrModuleCompliance':cmplsFrrModuleCompliance,'cmplsFrrModuleComplianceRev1':cmplsFrrModuleComplianceRev1})