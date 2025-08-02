_Ad='fspfDatabaseGroupRev2'
_Ac='fspfDatabaseGroupRev1'
_Ab='fspfGenericGroup'
_Aa='fspfNbrStateChangeNotify'
_AZ='fspfLsrExternal'
_AY='fspfTotalCheckSum'
_AX='fspfIfRowStatus'
_AW='fspfIfSetToDefault'
_AV='fspfIfCreateTime'
_AU='fspfIfAdminStatus'
_AT='fspfIfNbrPortIndex'
_AS='fspfIfInactivityExpirations'
_AR='fspfIfErrorRxPkts'
_AQ='fspfIfRetransmittedLsuTxPkts'
_AP='fspfIfHelloRxPkts'
_AO='fspfIfHelloTxPkts'
_AN='fspfIfLsaTxPkts'
_AM='fspfIfLsuTxPkts'
_AL='fspfIfLsaRxPkts'
_AK='fspfIfLsuRxPkts'
_AJ='fspfIfRetransmitInterval'
_AI='fspfIfDeadInterval'
_AH='fspfIfHelloInterval'
_AG='fspfIfCost'
_AF='fspfLinkIndex'
_AE='FspfRegionId'
_AD='TruthValue'
_AC='notifyVsanIndex'
_AB='fspfDatabaseGroup'
_AA='fspfLinkNumber'
_A9='fspfLsrNumber'
_A8='fspfIfPrevNbrState'
_A7='fspfIfNbrDomainId'
_A6='fspfIfNbrState'
_A5='fspfNbrStateChangeNotifyEnable'
_A4='fspfRowStatus'
_A3='fspfSetToDefault'
_A2='fspfOperStatus'
_A1='fspfAdminStatus'
_A0='fspfCreateTime'
_z='fspfLsrs'
_y='fspfErrorRxPkts'
_x='fspfRetransmittedLsuTxPkts'
_w='fspfHelloRxPkts'
_v='fspfHelloTxPkts'
_u='fspfLsaTxPkts'
_t='fspfLsuTxPkts'
_s='fspfLsaRxPkts'
_r='fspfLsuRxPkts'
_q='fspfChecksumErrors'
_p='fspfSpfComputations'
_o='fspfMaxAgeCount'
_n='fspfMaxAge'
_m='fspfLsRefreshTime'
_l='fspfMinLsInterval'
_k='fspfMinLsArrival'
_j='fspfSpfHoldTime'
_i='fspfSpfDelay'
_h='fspfRegionId'
_g='not-accessible'
_f='fspfLsrType'
_e='fspfLsrDomainId'
_d='MilliSeconds'
_c='ifIndex'
_b='IF-MIB'
_a='fspfGenericGroupRev1'
_Z='fspfLinkCost'
_Y='fspfLinkType'
_X='fspfLinkNbrPortIndex'
_W='fspfLinkPortIndex'
_V='fspfLinkNbrDomainId'
_U='fspfLsrLinks'
_T='fspfLsrCheckSum'
_S='fspfLsrIncarnationNumber'
_R='fspfLsrAge'
_Q='fspfLsrAdvDomainId'
_P='fspfDomainId'
_O='down'
_N='CiscoMilliSeconds'
_M='fspfNotificationGroup'
_L='fspfIfGroup'
_K='Seconds'
_J='vsanIndex'
_I='TimeIntervalSec'
_H='deprecated'
_G='CISCO-VSAN-MIB'
_F='Integer32'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='current'
_A='CISCO-FSPF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
DomainId,DomainIdOrZero=mibBuilder.importSymbols('CISCO-ST-TC','DomainId','DomainIdOrZero')
CiscoMilliSeconds,TimeIntervalMin,TimeIntervalSec=mibBuilder.importSymbols('CISCO-TC',_N,'TimeIntervalMin',_I)
notifyVsanIndex,vsanIndex=mibBuilder.importSymbols(_G,_AC,_J)
ifIndex,=mibBuilder.importSymbols(_b,_c)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_AD)
ciscoFspfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,287))
if mibBuilder.loadTexts:ciscoFspfMIB.setRevisions(('2003-10-08 00:00','2003-04-13 00:00','2003-02-21 00:00','2002-11-21 00:00','2002-11-01 00:00','2002-10-04 00:00'))
class FspfRegionId(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class FspfLsrType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class FspfLinkType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class FspfInterfaceState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),('init',2),('dbExchange',3),('dbAckwait',4),('dbWait',5),('full',6)))
class LastCreationTime(TextualConvention,TimeTicks):status=_B
_FspfConfiguration_ObjectIdentity=ObjectIdentity
fspfConfiguration=_FspfConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,287,1))
_FspfTable_Object=MibTable
fspfTable=_FspfTable_Object((1,3,6,1,4,1,9,9,287,1,1))
if mibBuilder.loadTexts:fspfTable.setStatus(_B)
_FspfEntry_Object=MibTableRow
fspfEntry=_FspfEntry_Object((1,3,6,1,4,1,9,9,287,1,1,1))
fspfEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:fspfEntry.setStatus(_B)
class _FspfRegionId_Type(FspfRegionId):defaultValue=0
_FspfRegionId_Type.__name__=_AE
_FspfRegionId_Object=MibTableColumn
fspfRegionId=_FspfRegionId_Object((1,3,6,1,4,1,9,9,287,1,1,1,1),_FspfRegionId_Type())
fspfRegionId.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfRegionId.setStatus(_B)
_FspfDomainId_Type=DomainId
_FspfDomainId_Object=MibTableColumn
fspfDomainId=_FspfDomainId_Object((1,3,6,1,4,1,9,9,287,1,1,1,2),_FspfDomainId_Type())
fspfDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfDomainId.setStatus(_B)
_FspfSpfDelay_Type=TimeIntervalSec
_FspfSpfDelay_Object=MibTableColumn
fspfSpfDelay=_FspfSpfDelay_Object((1,3,6,1,4,1,9,9,287,1,1,1,3),_FspfSpfDelay_Type())
fspfSpfDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfSpfDelay.setStatus(_B)
if mibBuilder.loadTexts:fspfSpfDelay.setUnits(_K)
class _FspfSpfHoldTime_Type(CiscoMilliSeconds):defaultValue=0;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FspfSpfHoldTime_Type.__name__=_N
_FspfSpfHoldTime_Object=MibTableColumn
fspfSpfHoldTime=_FspfSpfHoldTime_Object((1,3,6,1,4,1,9,9,287,1,1,1,4),_FspfSpfHoldTime_Type())
fspfSpfHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfSpfHoldTime.setStatus(_B)
if mibBuilder.loadTexts:fspfSpfHoldTime.setUnits(_d)
class _FspfMinLsArrival_Type(CiscoMilliSeconds):defaultValue=1000;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FspfMinLsArrival_Type.__name__=_N
_FspfMinLsArrival_Object=MibTableColumn
fspfMinLsArrival=_FspfMinLsArrival_Object((1,3,6,1,4,1,9,9,287,1,1,1,5),_FspfMinLsArrival_Type())
fspfMinLsArrival.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfMinLsArrival.setStatus(_B)
if mibBuilder.loadTexts:fspfMinLsArrival.setUnits(_d)
class _FspfMinLsInterval_Type(CiscoMilliSeconds):defaultValue=5000;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FspfMinLsInterval_Type.__name__=_N
_FspfMinLsInterval_Object=MibTableColumn
fspfMinLsInterval=_FspfMinLsInterval_Object((1,3,6,1,4,1,9,9,287,1,1,1,6),_FspfMinLsInterval_Type())
fspfMinLsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfMinLsInterval.setStatus(_B)
if mibBuilder.loadTexts:fspfMinLsInterval.setUnits(_d)
_FspfLsRefreshTime_Type=TimeIntervalMin
_FspfLsRefreshTime_Object=MibTableColumn
fspfLsRefreshTime=_FspfLsRefreshTime_Object((1,3,6,1,4,1,9,9,287,1,1,1,7),_FspfLsRefreshTime_Type())
fspfLsRefreshTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsRefreshTime.setStatus(_B)
if mibBuilder.loadTexts:fspfLsRefreshTime.setUnits('Minutes')
_FspfMaxAge_Type=TimeIntervalMin
_FspfMaxAge_Object=MibTableColumn
fspfMaxAge=_FspfMaxAge_Object((1,3,6,1,4,1,9,9,287,1,1,1,8),_FspfMaxAge_Type())
fspfMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfMaxAge.setStatus(_B)
if mibBuilder.loadTexts:fspfMaxAge.setUnits('Minutes')
_FspfMaxAgeCount_Type=Counter32
_FspfMaxAgeCount_Object=MibTableColumn
fspfMaxAgeCount=_FspfMaxAgeCount_Object((1,3,6,1,4,1,9,9,287,1,1,1,9),_FspfMaxAgeCount_Type())
fspfMaxAgeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfMaxAgeCount.setStatus(_B)
_FspfSpfComputations_Type=Counter32
_FspfSpfComputations_Object=MibTableColumn
fspfSpfComputations=_FspfSpfComputations_Object((1,3,6,1,4,1,9,9,287,1,1,1,10),_FspfSpfComputations_Type())
fspfSpfComputations.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfSpfComputations.setStatus(_B)
_FspfChecksumErrors_Type=Counter32
_FspfChecksumErrors_Object=MibTableColumn
fspfChecksumErrors=_FspfChecksumErrors_Object((1,3,6,1,4,1,9,9,287,1,1,1,11),_FspfChecksumErrors_Type())
fspfChecksumErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfChecksumErrors.setStatus(_B)
_FspfLsuRxPkts_Type=Counter32
_FspfLsuRxPkts_Object=MibTableColumn
fspfLsuRxPkts=_FspfLsuRxPkts_Object((1,3,6,1,4,1,9,9,287,1,1,1,12),_FspfLsuRxPkts_Type())
fspfLsuRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsuRxPkts.setStatus(_B)
_FspfLsaRxPkts_Type=Counter32
_FspfLsaRxPkts_Object=MibTableColumn
fspfLsaRxPkts=_FspfLsaRxPkts_Object((1,3,6,1,4,1,9,9,287,1,1,1,13),_FspfLsaRxPkts_Type())
fspfLsaRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsaRxPkts.setStatus(_B)
_FspfLsuTxPkts_Type=Counter32
_FspfLsuTxPkts_Object=MibTableColumn
fspfLsuTxPkts=_FspfLsuTxPkts_Object((1,3,6,1,4,1,9,9,287,1,1,1,14),_FspfLsuTxPkts_Type())
fspfLsuTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsuTxPkts.setStatus(_B)
_FspfLsaTxPkts_Type=Counter32
_FspfLsaTxPkts_Object=MibTableColumn
fspfLsaTxPkts=_FspfLsaTxPkts_Object((1,3,6,1,4,1,9,9,287,1,1,1,15),_FspfLsaTxPkts_Type())
fspfLsaTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsaTxPkts.setStatus(_B)
_FspfHelloTxPkts_Type=Counter32
_FspfHelloTxPkts_Object=MibTableColumn
fspfHelloTxPkts=_FspfHelloTxPkts_Object((1,3,6,1,4,1,9,9,287,1,1,1,16),_FspfHelloTxPkts_Type())
fspfHelloTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfHelloTxPkts.setStatus(_B)
_FspfHelloRxPkts_Type=Counter32
_FspfHelloRxPkts_Object=MibTableColumn
fspfHelloRxPkts=_FspfHelloRxPkts_Object((1,3,6,1,4,1,9,9,287,1,1,1,17),_FspfHelloRxPkts_Type())
fspfHelloRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfHelloRxPkts.setStatus(_B)
_FspfRetransmittedLsuTxPkts_Type=Counter32
_FspfRetransmittedLsuTxPkts_Object=MibTableColumn
fspfRetransmittedLsuTxPkts=_FspfRetransmittedLsuTxPkts_Object((1,3,6,1,4,1,9,9,287,1,1,1,18),_FspfRetransmittedLsuTxPkts_Type())
fspfRetransmittedLsuTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfRetransmittedLsuTxPkts.setStatus(_B)
_FspfErrorRxPkts_Type=Counter32
_FspfErrorRxPkts_Object=MibTableColumn
fspfErrorRxPkts=_FspfErrorRxPkts_Object((1,3,6,1,4,1,9,9,287,1,1,1,19),_FspfErrorRxPkts_Type())
fspfErrorRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfErrorRxPkts.setStatus(_B)
_FspfLsrs_Type=Gauge32
_FspfLsrs_Object=MibTableColumn
fspfLsrs=_FspfLsrs_Object((1,3,6,1,4,1,9,9,287,1,1,1,20),_FspfLsrs_Type())
fspfLsrs.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsrs.setStatus(_B)
_FspfCreateTime_Type=LastCreationTime
_FspfCreateTime_Object=MibTableColumn
fspfCreateTime=_FspfCreateTime_Object((1,3,6,1,4,1,9,9,287,1,1,1,21),_FspfCreateTime_Type())
fspfCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfCreateTime.setStatus(_B)
class _FspfAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_O,2)))
_FspfAdminStatus_Type.__name__=_F
_FspfAdminStatus_Object=MibTableColumn
fspfAdminStatus=_FspfAdminStatus_Object((1,3,6,1,4,1,9,9,287,1,1,1,22),_FspfAdminStatus_Type())
fspfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfAdminStatus.setStatus(_B)
class _FspfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_O,2)))
_FspfOperStatus_Type.__name__=_F
_FspfOperStatus_Object=MibTableColumn
fspfOperStatus=_FspfOperStatus_Object((1,3,6,1,4,1,9,9,287,1,1,1,23),_FspfOperStatus_Type())
fspfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfOperStatus.setStatus(_B)
class _FspfSetToDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('noOp',2)))
_FspfSetToDefault_Type.__name__=_F
_FspfSetToDefault_Object=MibTableColumn
fspfSetToDefault=_FspfSetToDefault_Object((1,3,6,1,4,1,9,9,287,1,1,1,24),_FspfSetToDefault_Type())
fspfSetToDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfSetToDefault.setStatus(_B)
_FspfRowStatus_Type=RowStatus
_FspfRowStatus_Object=MibTableColumn
fspfRowStatus=_FspfRowStatus_Object((1,3,6,1,4,1,9,9,287,1,1,1,25),_FspfRowStatus_Type())
fspfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfRowStatus.setStatus(_B)
_FspfTotalCheckSum_Type=Unsigned32
_FspfTotalCheckSum_Object=MibTableColumn
fspfTotalCheckSum=_FspfTotalCheckSum_Object((1,3,6,1,4,1,9,9,287,1,1,1,26),_FspfTotalCheckSum_Type())
fspfTotalCheckSum.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfTotalCheckSum.setStatus(_B)
_FspfIfTable_Object=MibTable
fspfIfTable=_FspfIfTable_Object((1,3,6,1,4,1,9,9,287,1,2))
if mibBuilder.loadTexts:fspfIfTable.setStatus(_B)
_FspfIfEntry_Object=MibTableRow
fspfIfEntry=_FspfIfEntry_Object((1,3,6,1,4,1,9,9,287,1,2,1))
fspfIfEntry.setIndexNames((0,_G,_J),(0,_b,_c))
if mibBuilder.loadTexts:fspfIfEntry.setStatus(_B)
class _FspfIfCost_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FspfIfCost_Type.__name__=_E
_FspfIfCost_Object=MibTableColumn
fspfIfCost=_FspfIfCost_Object((1,3,6,1,4,1,9,9,287,1,2,1,1),_FspfIfCost_Type())
fspfIfCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfIfCost.setStatus(_B)
class _FspfIfHelloInterval_Type(TimeIntervalSec):defaultValue=20;subtypeSpec=TimeIntervalSec.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FspfIfHelloInterval_Type.__name__=_I
_FspfIfHelloInterval_Object=MibTableColumn
fspfIfHelloInterval=_FspfIfHelloInterval_Object((1,3,6,1,4,1,9,9,287,1,2,1,2),_FspfIfHelloInterval_Type())
fspfIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfIfHelloInterval.setStatus(_B)
if mibBuilder.loadTexts:fspfIfHelloInterval.setUnits(_K)
class _FspfIfDeadInterval_Type(TimeIntervalSec):defaultValue=80;subtypeSpec=TimeIntervalSec.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,65535))
_FspfIfDeadInterval_Type.__name__=_I
_FspfIfDeadInterval_Object=MibTableColumn
fspfIfDeadInterval=_FspfIfDeadInterval_Object((1,3,6,1,4,1,9,9,287,1,2,1,3),_FspfIfDeadInterval_Type())
fspfIfDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfIfDeadInterval.setStatus(_B)
if mibBuilder.loadTexts:fspfIfDeadInterval.setUnits(_K)
class _FspfIfRetransmitInterval_Type(TimeIntervalSec):defaultValue=5;subtypeSpec=TimeIntervalSec.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FspfIfRetransmitInterval_Type.__name__=_I
_FspfIfRetransmitInterval_Object=MibTableColumn
fspfIfRetransmitInterval=_FspfIfRetransmitInterval_Object((1,3,6,1,4,1,9,9,287,1,2,1,4),_FspfIfRetransmitInterval_Type())
fspfIfRetransmitInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfIfRetransmitInterval.setStatus(_B)
if mibBuilder.loadTexts:fspfIfRetransmitInterval.setUnits(_K)
_FspfIfLsuRxPkts_Type=Counter32
_FspfIfLsuRxPkts_Object=MibTableColumn
fspfIfLsuRxPkts=_FspfIfLsuRxPkts_Object((1,3,6,1,4,1,9,9,287,1,2,1,5),_FspfIfLsuRxPkts_Type())
fspfIfLsuRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfLsuRxPkts.setStatus(_B)
_FspfIfLsaRxPkts_Type=Counter32
_FspfIfLsaRxPkts_Object=MibTableColumn
fspfIfLsaRxPkts=_FspfIfLsaRxPkts_Object((1,3,6,1,4,1,9,9,287,1,2,1,6),_FspfIfLsaRxPkts_Type())
fspfIfLsaRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfLsaRxPkts.setStatus(_B)
_FspfIfLsuTxPkts_Type=Counter32
_FspfIfLsuTxPkts_Object=MibTableColumn
fspfIfLsuTxPkts=_FspfIfLsuTxPkts_Object((1,3,6,1,4,1,9,9,287,1,2,1,7),_FspfIfLsuTxPkts_Type())
fspfIfLsuTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfLsuTxPkts.setStatus(_B)
_FspfIfLsaTxPkts_Type=Counter32
_FspfIfLsaTxPkts_Object=MibTableColumn
fspfIfLsaTxPkts=_FspfIfLsaTxPkts_Object((1,3,6,1,4,1,9,9,287,1,2,1,8),_FspfIfLsaTxPkts_Type())
fspfIfLsaTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfLsaTxPkts.setStatus(_B)
_FspfIfHelloTxPkts_Type=Counter32
_FspfIfHelloTxPkts_Object=MibTableColumn
fspfIfHelloTxPkts=_FspfIfHelloTxPkts_Object((1,3,6,1,4,1,9,9,287,1,2,1,9),_FspfIfHelloTxPkts_Type())
fspfIfHelloTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfHelloTxPkts.setStatus(_B)
_FspfIfHelloRxPkts_Type=Counter32
_FspfIfHelloRxPkts_Object=MibTableColumn
fspfIfHelloRxPkts=_FspfIfHelloRxPkts_Object((1,3,6,1,4,1,9,9,287,1,2,1,10),_FspfIfHelloRxPkts_Type())
fspfIfHelloRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfHelloRxPkts.setStatus(_B)
_FspfIfRetransmittedLsuTxPkts_Type=Counter32
_FspfIfRetransmittedLsuTxPkts_Object=MibTableColumn
fspfIfRetransmittedLsuTxPkts=_FspfIfRetransmittedLsuTxPkts_Object((1,3,6,1,4,1,9,9,287,1,2,1,11),_FspfIfRetransmittedLsuTxPkts_Type())
fspfIfRetransmittedLsuTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfRetransmittedLsuTxPkts.setStatus(_B)
_FspfIfErrorRxPkts_Type=Counter32
_FspfIfErrorRxPkts_Object=MibTableColumn
fspfIfErrorRxPkts=_FspfIfErrorRxPkts_Object((1,3,6,1,4,1,9,9,287,1,2,1,12),_FspfIfErrorRxPkts_Type())
fspfIfErrorRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfErrorRxPkts.setStatus(_B)
_FspfIfInactivityExpirations_Type=Counter32
_FspfIfInactivityExpirations_Object=MibTableColumn
fspfIfInactivityExpirations=_FspfIfInactivityExpirations_Object((1,3,6,1,4,1,9,9,287,1,2,1,13),_FspfIfInactivityExpirations_Type())
fspfIfInactivityExpirations.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfInactivityExpirations.setStatus(_B)
_FspfIfNbrState_Type=FspfInterfaceState
_FspfIfNbrState_Object=MibTableColumn
fspfIfNbrState=_FspfIfNbrState_Object((1,3,6,1,4,1,9,9,287,1,2,1,14),_FspfIfNbrState_Type())
fspfIfNbrState.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfNbrState.setStatus(_B)
_FspfIfNbrDomainId_Type=DomainIdOrZero
_FspfIfNbrDomainId_Object=MibTableColumn
fspfIfNbrDomainId=_FspfIfNbrDomainId_Object((1,3,6,1,4,1,9,9,287,1,2,1,15),_FspfIfNbrDomainId_Type())
fspfIfNbrDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfNbrDomainId.setStatus(_B)
class _FspfIfNbrPortIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FspfIfNbrPortIndex_Type.__name__=_E
_FspfIfNbrPortIndex_Object=MibTableColumn
fspfIfNbrPortIndex=_FspfIfNbrPortIndex_Object((1,3,6,1,4,1,9,9,287,1,2,1,16),_FspfIfNbrPortIndex_Type())
fspfIfNbrPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfNbrPortIndex.setStatus(_B)
class _FspfIfAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_O,2)))
_FspfIfAdminStatus_Type.__name__=_F
_FspfIfAdminStatus_Object=MibTableColumn
fspfIfAdminStatus=_FspfIfAdminStatus_Object((1,3,6,1,4,1,9,9,287,1,2,1,17),_FspfIfAdminStatus_Type())
fspfIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfIfAdminStatus.setStatus(_B)
_FspfIfCreateTime_Type=LastCreationTime
_FspfIfCreateTime_Object=MibTableColumn
fspfIfCreateTime=_FspfIfCreateTime_Object((1,3,6,1,4,1,9,9,287,1,2,1,18),_FspfIfCreateTime_Type())
fspfIfCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfIfCreateTime.setStatus(_B)
class _FspfIfSetToDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('noOp',2)))
_FspfIfSetToDefault_Type.__name__=_F
_FspfIfSetToDefault_Object=MibTableColumn
fspfIfSetToDefault=_FspfIfSetToDefault_Object((1,3,6,1,4,1,9,9,287,1,2,1,19),_FspfIfSetToDefault_Type())
fspfIfSetToDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfIfSetToDefault.setStatus(_B)
_FspfIfRowStatus_Type=RowStatus
_FspfIfRowStatus_Object=MibTableColumn
fspfIfRowStatus=_FspfIfRowStatus_Object((1,3,6,1,4,1,9,9,287,1,2,1,20),_FspfIfRowStatus_Type())
fspfIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fspfIfRowStatus.setStatus(_B)
class _FspfNbrStateChangeNotifyEnable_Type(TruthValue):defaultValue=2
_FspfNbrStateChangeNotifyEnable_Type.__name__=_AD
_FspfNbrStateChangeNotifyEnable_Object=MibScalar
fspfNbrStateChangeNotifyEnable=_FspfNbrStateChangeNotifyEnable_Object((1,3,6,1,4,1,9,9,287,1,3),_FspfNbrStateChangeNotifyEnable_Type())
fspfNbrStateChangeNotifyEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:fspfNbrStateChangeNotifyEnable.setStatus(_B)
_FspfIfPrevNbrState_Type=FspfInterfaceState
_FspfIfPrevNbrState_Object=MibScalar
fspfIfPrevNbrState=_FspfIfPrevNbrState_Object((1,3,6,1,4,1,9,9,287,1,4),_FspfIfPrevNbrState_Type())
fspfIfPrevNbrState.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:fspfIfPrevNbrState.setStatus(_B)
_FspfDatabase_ObjectIdentity=ObjectIdentity
fspfDatabase=_FspfDatabase_ObjectIdentity((1,3,6,1,4,1,9,9,287,2))
_FspfLsrTable_Object=MibTable
fspfLsrTable=_FspfLsrTable_Object((1,3,6,1,4,1,9,9,287,2,1))
if mibBuilder.loadTexts:fspfLsrTable.setStatus(_B)
_FspfLsrEntry_Object=MibTableRow
fspfLsrEntry=_FspfLsrEntry_Object((1,3,6,1,4,1,9,9,287,2,1,1))
fspfLsrEntry.setIndexNames((0,_G,_J),(0,_A,_e),(0,_A,_f))
if mibBuilder.loadTexts:fspfLsrEntry.setStatus(_B)
_FspfLsrDomainId_Type=DomainId
_FspfLsrDomainId_Object=MibTableColumn
fspfLsrDomainId=_FspfLsrDomainId_Object((1,3,6,1,4,1,9,9,287,2,1,1,1),_FspfLsrDomainId_Type())
fspfLsrDomainId.setMaxAccess(_g)
if mibBuilder.loadTexts:fspfLsrDomainId.setStatus(_B)
_FspfLsrType_Type=FspfLsrType
_FspfLsrType_Object=MibTableColumn
fspfLsrType=_FspfLsrType_Object((1,3,6,1,4,1,9,9,287,2,1,1,2),_FspfLsrType_Type())
fspfLsrType.setMaxAccess(_g)
if mibBuilder.loadTexts:fspfLsrType.setStatus(_B)
_FspfLsrAdvDomainId_Type=DomainId
_FspfLsrAdvDomainId_Object=MibTableColumn
fspfLsrAdvDomainId=_FspfLsrAdvDomainId_Object((1,3,6,1,4,1,9,9,287,2,1,1,3),_FspfLsrAdvDomainId_Type())
fspfLsrAdvDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsrAdvDomainId.setStatus(_B)
class _FspfLsrAge_Type(TimeIntervalSec):subtypeSpec=TimeIntervalSec.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FspfLsrAge_Type.__name__=_I
_FspfLsrAge_Object=MibTableColumn
fspfLsrAge=_FspfLsrAge_Object((1,3,6,1,4,1,9,9,287,2,1,1,4),_FspfLsrAge_Type())
fspfLsrAge.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsrAge.setStatus(_B)
if mibBuilder.loadTexts:fspfLsrAge.setUnits(_K)
class _FspfLsrIncarnationNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FspfLsrIncarnationNumber_Type.__name__=_E
_FspfLsrIncarnationNumber_Object=MibTableColumn
fspfLsrIncarnationNumber=_FspfLsrIncarnationNumber_Object((1,3,6,1,4,1,9,9,287,2,1,1,5),_FspfLsrIncarnationNumber_Type())
fspfLsrIncarnationNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsrIncarnationNumber.setStatus(_B)
class _FspfLsrCheckSum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FspfLsrCheckSum_Type.__name__=_E
_FspfLsrCheckSum_Object=MibTableColumn
fspfLsrCheckSum=_FspfLsrCheckSum_Object((1,3,6,1,4,1,9,9,287,2,1,1,6),_FspfLsrCheckSum_Type())
fspfLsrCheckSum.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsrCheckSum.setStatus(_B)
class _FspfLsrLinks_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65355))
_FspfLsrLinks_Type.__name__=_E
_FspfLsrLinks_Object=MibTableColumn
fspfLsrLinks=_FspfLsrLinks_Object((1,3,6,1,4,1,9,9,287,2,1,1,7),_FspfLsrLinks_Type())
fspfLsrLinks.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsrLinks.setStatus(_B)
_FspfLsrExternal_Type=TruthValue
_FspfLsrExternal_Object=MibTableColumn
fspfLsrExternal=_FspfLsrExternal_Object((1,3,6,1,4,1,9,9,287,2,1,1,8),_FspfLsrExternal_Type())
fspfLsrExternal.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsrExternal.setStatus(_B)
_FspfLinkTable_Object=MibTable
fspfLinkTable=_FspfLinkTable_Object((1,3,6,1,4,1,9,9,287,2,2))
if mibBuilder.loadTexts:fspfLinkTable.setStatus(_B)
_FspfLinkEntry_Object=MibTableRow
fspfLinkEntry=_FspfLinkEntry_Object((1,3,6,1,4,1,9,9,287,2,2,1))
fspfLinkEntry.setIndexNames((0,_G,_J),(0,_A,_e),(0,_A,_f),(0,_A,_AF))
if mibBuilder.loadTexts:fspfLinkEntry.setStatus(_B)
_FspfLinkIndex_Type=Unsigned32
_FspfLinkIndex_Object=MibTableColumn
fspfLinkIndex=_FspfLinkIndex_Object((1,3,6,1,4,1,9,9,287,2,2,1,1),_FspfLinkIndex_Type())
fspfLinkIndex.setMaxAccess(_g)
if mibBuilder.loadTexts:fspfLinkIndex.setStatus(_B)
_FspfLinkNbrDomainId_Type=DomainId
_FspfLinkNbrDomainId_Object=MibTableColumn
fspfLinkNbrDomainId=_FspfLinkNbrDomainId_Object((1,3,6,1,4,1,9,9,287,2,2,1,2),_FspfLinkNbrDomainId_Type())
fspfLinkNbrDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLinkNbrDomainId.setStatus(_B)
class _FspfLinkPortIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_FspfLinkPortIndex_Type.__name__=_E
_FspfLinkPortIndex_Object=MibTableColumn
fspfLinkPortIndex=_FspfLinkPortIndex_Object((1,3,6,1,4,1,9,9,287,2,2,1,3),_FspfLinkPortIndex_Type())
fspfLinkPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLinkPortIndex.setStatus(_B)
class _FspfLinkNbrPortIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_FspfLinkNbrPortIndex_Type.__name__=_E
_FspfLinkNbrPortIndex_Object=MibTableColumn
fspfLinkNbrPortIndex=_FspfLinkNbrPortIndex_Object((1,3,6,1,4,1,9,9,287,2,2,1,4),_FspfLinkNbrPortIndex_Type())
fspfLinkNbrPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLinkNbrPortIndex.setStatus(_B)
_FspfLinkType_Type=FspfLinkType
_FspfLinkType_Object=MibTableColumn
fspfLinkType=_FspfLinkType_Object((1,3,6,1,4,1,9,9,287,2,2,1,5),_FspfLinkType_Type())
fspfLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLinkType.setStatus(_B)
class _FspfLinkCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FspfLinkCost_Type.__name__=_F
_FspfLinkCost_Object=MibTableColumn
fspfLinkCost=_FspfLinkCost_Object((1,3,6,1,4,1,9,9,287,2,2,1,6),_FspfLinkCost_Type())
fspfLinkCost.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLinkCost.setStatus(_B)
class _FspfLsrNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FspfLsrNumber_Type.__name__=_E
_FspfLsrNumber_Object=MibScalar
fspfLsrNumber=_FspfLsrNumber_Object((1,3,6,1,4,1,9,9,287,2,3),_FspfLsrNumber_Type())
fspfLsrNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLsrNumber.setStatus(_B)
class _FspfLinkNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FspfLinkNumber_Type.__name__=_E
_FspfLinkNumber_Object=MibScalar
fspfLinkNumber=_FspfLinkNumber_Object((1,3,6,1,4,1,9,9,287,2,4),_FspfLinkNumber_Type())
fspfLinkNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fspfLinkNumber.setStatus(_B)
_FspfNotificationPrefix_ObjectIdentity=ObjectIdentity
fspfNotificationPrefix=_FspfNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,287,3))
_FspfNotification_ObjectIdentity=ObjectIdentity
fspfNotification=_FspfNotification_ObjectIdentity((1,3,6,1,4,1,9,9,287,3,0))
_FspfMIBConformance_ObjectIdentity=ObjectIdentity
fspfMIBConformance=_FspfMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,287,4))
_FspfMIBCompliances_ObjectIdentity=ObjectIdentity
fspfMIBCompliances=_FspfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,287,4,1))
_FspfMIBGroups_ObjectIdentity=ObjectIdentity
fspfMIBGroups=_FspfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,287,4,2))
fspfGenericGroup=ObjectGroup((1,3,6,1,4,1,9,9,287,4,2,1))
fspfGenericGroup.setObjects(*((_A,_h),(_A,_P),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:fspfGenericGroup.setStatus(_H)
fspfIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,287,4,2,3))
fspfIfGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_A6),(_A,_A7),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_A8)))
if mibBuilder.loadTexts:fspfIfGroup.setStatus(_B)
fspfDatabaseGroup=ObjectGroup((1,3,6,1,4,1,9,9,287,4,2,4))
fspfDatabaseGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:fspfDatabaseGroup.setStatus(_H)
fspfGenericGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,287,4,2,6))
fspfGenericGroupRev1.setObjects(*((_A,_h),(_A,_P),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_AY),(_A,_A5)))
if mibBuilder.loadTexts:fspfGenericGroupRev1.setStatus(_B)
fspfDatabaseGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,287,4,2,7))
fspfDatabaseGroupRev1.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:fspfDatabaseGroupRev1.setStatus(_H)
fspfDatabaseGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,287,4,2,8))
fspfDatabaseGroupRev2.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_A9),(_A,_AA),(_A,_AZ)))
if mibBuilder.loadTexts:fspfDatabaseGroupRev2.setStatus(_B)
fspfNbrStateChangeNotify=NotificationType((1,3,6,1,4,1,9,9,287,3,0,1))
fspfNbrStateChangeNotify.setObjects(*((_b,_c),(_G,_AC),(_A,_P),(_A,_A7),(_A,_A6),(_A,_A8)))
if mibBuilder.loadTexts:fspfNbrStateChangeNotify.setStatus(_B)
fspfNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,287,4,2,5))
fspfNotificationGroup.setObjects((_A,_Aa))
if mibBuilder.loadTexts:fspfNotificationGroup.setStatus(_B)
fspfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,287,4,1,1))
fspfMIBCompliance.setObjects(*((_A,_Ab),(_A,_L),(_A,_AB),(_A,_M)))
if mibBuilder.loadTexts:fspfMIBCompliance.setStatus(_H)
fspfMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,287,4,1,2))
fspfMIBCompliance1.setObjects(*((_A,_a),(_A,_L),(_A,_AB),(_A,_M)))
if mibBuilder.loadTexts:fspfMIBCompliance1.setStatus(_H)
fspfMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,287,4,1,3))
fspfMIBCompliance2.setObjects(*((_A,_a),(_A,_L),(_A,_Ac),(_A,_M)))
if mibBuilder.loadTexts:fspfMIBCompliance2.setStatus(_H)
fspfMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,287,4,1,4))
fspfMIBCompliance3.setObjects(*((_A,_a),(_A,_L),(_A,_Ad),(_A,_M)))
if mibBuilder.loadTexts:fspfMIBCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_AE:FspfRegionId,'FspfLsrType':FspfLsrType,'FspfLinkType':FspfLinkType,'FspfInterfaceState':FspfInterfaceState,'LastCreationTime':LastCreationTime,'ciscoFspfMIB':ciscoFspfMIB,'fspfConfiguration':fspfConfiguration,'fspfTable':fspfTable,'fspfEntry':fspfEntry,_h:fspfRegionId,_P:fspfDomainId,_i:fspfSpfDelay,_j:fspfSpfHoldTime,_k:fspfMinLsArrival,_l:fspfMinLsInterval,_m:fspfLsRefreshTime,_n:fspfMaxAge,_o:fspfMaxAgeCount,_p:fspfSpfComputations,_q:fspfChecksumErrors,_r:fspfLsuRxPkts,_s:fspfLsaRxPkts,_t:fspfLsuTxPkts,_u:fspfLsaTxPkts,_v:fspfHelloTxPkts,_w:fspfHelloRxPkts,_x:fspfRetransmittedLsuTxPkts,_y:fspfErrorRxPkts,_z:fspfLsrs,_A0:fspfCreateTime,_A1:fspfAdminStatus,_A2:fspfOperStatus,_A3:fspfSetToDefault,_A4:fspfRowStatus,_AY:fspfTotalCheckSum,'fspfIfTable':fspfIfTable,'fspfIfEntry':fspfIfEntry,_AG:fspfIfCost,_AH:fspfIfHelloInterval,_AI:fspfIfDeadInterval,_AJ:fspfIfRetransmitInterval,_AK:fspfIfLsuRxPkts,_AL:fspfIfLsaRxPkts,_AM:fspfIfLsuTxPkts,_AN:fspfIfLsaTxPkts,_AO:fspfIfHelloTxPkts,_AP:fspfIfHelloRxPkts,_AQ:fspfIfRetransmittedLsuTxPkts,_AR:fspfIfErrorRxPkts,_AS:fspfIfInactivityExpirations,_A6:fspfIfNbrState,_A7:fspfIfNbrDomainId,_AT:fspfIfNbrPortIndex,_AU:fspfIfAdminStatus,_AV:fspfIfCreateTime,_AW:fspfIfSetToDefault,_AX:fspfIfRowStatus,_A5:fspfNbrStateChangeNotifyEnable,_A8:fspfIfPrevNbrState,'fspfDatabase':fspfDatabase,'fspfLsrTable':fspfLsrTable,'fspfLsrEntry':fspfLsrEntry,_e:fspfLsrDomainId,_f:fspfLsrType,_Q:fspfLsrAdvDomainId,_R:fspfLsrAge,_S:fspfLsrIncarnationNumber,_T:fspfLsrCheckSum,_U:fspfLsrLinks,_AZ:fspfLsrExternal,'fspfLinkTable':fspfLinkTable,'fspfLinkEntry':fspfLinkEntry,_AF:fspfLinkIndex,_V:fspfLinkNbrDomainId,_W:fspfLinkPortIndex,_X:fspfLinkNbrPortIndex,_Y:fspfLinkType,_Z:fspfLinkCost,_A9:fspfLsrNumber,_AA:fspfLinkNumber,'fspfNotificationPrefix':fspfNotificationPrefix,'fspfNotification':fspfNotification,_Aa:fspfNbrStateChangeNotify,'fspfMIBConformance':fspfMIBConformance,'fspfMIBCompliances':fspfMIBCompliances,'fspfMIBCompliance':fspfMIBCompliance,'fspfMIBCompliance1':fspfMIBCompliance1,'fspfMIBCompliance2':fspfMIBCompliance2,'fspfMIBCompliance3':fspfMIBCompliance3,'fspfMIBGroups':fspfMIBGroups,_Ab:fspfGenericGroup,_L:fspfIfGroup,_AB:fspfDatabaseGroup,_M:fspfNotificationGroup,_a:fspfGenericGroupRev1,_Ac:fspfDatabaseGroupRev1,_Ad:fspfDatabaseGroupRev2})