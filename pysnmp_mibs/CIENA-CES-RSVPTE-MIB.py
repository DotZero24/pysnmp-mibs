_K='AdvertisedLabel'
_J='cienaCesRsvpteIfIndex'
_I='CIENA-CES-RSVPTE-MIB'
_H='seconds'
_G='OctetString'
_F='deprecated'
_E='TruthValue'
_D='Unsigned32'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaCesConfig,cienaCesNotifications=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications')
CienaGlobalState,=mibBuilder.importSymbols('CIENA-TC','CienaGlobalState')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_E)
cienaCesRsvpteMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,16))
if mibBuilder.loadTexts:cienaCesRsvpteMIB.setRevisions(('2017-06-07 00:00','2016-07-15 00:00','2016-07-14 00:00','2016-07-04 00:00','2013-05-08 00:00','2011-02-02 00:00'))
class AdvertisedLabel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,99)));namedValues=NamedValues(*(('implicitnull',1),('nonreserved',99)))
class RsvpOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('operStatusUp',1),('operStatusDown',2),('operStatusGoingUp',3),('operStatusGoingDown',4),('operStatusActFailed',5)))
class RsvpGRMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('helpNeighbor',1),('restartCapable',2),('notApplicable',3)))
_CienaCesRsvpteMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesRsvpteMIBObjects=_CienaCesRsvpteMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,16,1))
_CienaCesRsvpteObjects_ObjectIdentity=ObjectIdentity
cienaCesRsvpteObjects=_CienaCesRsvpteObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,16,1,1))
_CienaCesRsvpteAdminStatus_Type=CienaGlobalState
_CienaCesRsvpteAdminStatus_Object=MibScalar
cienaCesRsvpteAdminStatus=_CienaCesRsvpteAdminStatus_Object((1,3,6,1,4,1,1271,2,1,16,1,1,1),_CienaCesRsvpteAdminStatus_Type())
cienaCesRsvpteAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteAdminStatus.setStatus(_A)
_CienaCesRsvpteOperStatus_Type=RsvpOperStatus
_CienaCesRsvpteOperStatus_Object=MibScalar
cienaCesRsvpteOperStatus=_CienaCesRsvpteOperStatus_Object((1,3,6,1,4,1,1271,2,1,16,1,1,2),_CienaCesRsvpteOperStatus_Type())
cienaCesRsvpteOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteOperStatus.setStatus(_A)
class _CienaCesRsvpteRetryInterval_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,65))
_CienaCesRsvpteRetryInterval_Type.__name__=_D
_CienaCesRsvpteRetryInterval_Object=MibScalar
cienaCesRsvpteRetryInterval=_CienaCesRsvpteRetryInterval_Object((1,3,6,1,4,1,1271,2,1,16,1,1,3),_CienaCesRsvpteRetryInterval_Type())
cienaCesRsvpteRetryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:cienaCesRsvpteRetryInterval.setUnits(_H)
class _CienaCesRsvpteRetryInfiniteState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CienaCesRsvpteRetryInfiniteState_Type.__name__=_C
_CienaCesRsvpteRetryInfiniteState_Object=MibScalar
cienaCesRsvpteRetryInfiniteState=_CienaCesRsvpteRetryInfiniteState_Object((1,3,6,1,4,1,1271,2,1,16,1,1,4),_CienaCesRsvpteRetryInfiniteState_Type())
cienaCesRsvpteRetryInfiniteState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRetryInfiniteState.setStatus(_A)
class _CienaCesRsvpteRetryMax_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CienaCesRsvpteRetryMax_Type.__name__=_C
_CienaCesRsvpteRetryMax_Object=MibScalar
cienaCesRsvpteRetryMax=_CienaCesRsvpteRetryMax_Object((1,3,6,1,4,1,1271,2,1,16,1,1,5),_CienaCesRsvpteRetryMax_Type())
cienaCesRsvpteRetryMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRetryMax.setStatus(_A)
class _CienaCesRsvpteRefreshInterval_Type(Integer32):defaultValue=30000
_CienaCesRsvpteRefreshInterval_Type.__name__=_C
_CienaCesRsvpteRefreshInterval_Object=MibScalar
cienaCesRsvpteRefreshInterval=_CienaCesRsvpteRefreshInterval_Object((1,3,6,1,4,1,1271,2,1,16,1,1,6),_CienaCesRsvpteRefreshInterval_Type())
cienaCesRsvpteRefreshInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRefreshInterval.setStatus(_A)
if mibBuilder.loadTexts:cienaCesRsvpteRefreshInterval.setUnits('milliseconds')
class _CienaCesRsvpteRefreshMultiple_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214783647))
_CienaCesRsvpteRefreshMultiple_Type.__name__=_C
_CienaCesRsvpteRefreshMultiple_Object=MibScalar
cienaCesRsvpteRefreshMultiple=_CienaCesRsvpteRefreshMultiple_Object((1,3,6,1,4,1,1271,2,1,16,1,1,7),_CienaCesRsvpteRefreshMultiple_Type())
cienaCesRsvpteRefreshMultiple.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRefreshMultiple.setStatus(_A)
class _CienaCesRsvpteRfrshSlewDenom_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214783647))
_CienaCesRsvpteRfrshSlewDenom_Type.__name__=_C
_CienaCesRsvpteRfrshSlewDenom_Object=MibScalar
cienaCesRsvpteRfrshSlewDenom=_CienaCesRsvpteRfrshSlewDenom_Object((1,3,6,1,4,1,1271,2,1,16,1,1,8),_CienaCesRsvpteRfrshSlewDenom_Type())
cienaCesRsvpteRfrshSlewDenom.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRfrshSlewDenom.setStatus(_F)
class _CienaCesRsvpteRfrshSlewNumerator_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214783647))
_CienaCesRsvpteRfrshSlewNumerator_Type.__name__=_C
_CienaCesRsvpteRfrshSlewNumerator_Object=MibScalar
cienaCesRsvpteRfrshSlewNumerator=_CienaCesRsvpteRfrshSlewNumerator_Object((1,3,6,1,4,1,1271,2,1,16,1,1,9),_CienaCesRsvpteRfrshSlewNumerator_Type())
cienaCesRsvpteRfrshSlewNumerator.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRfrshSlewNumerator.setStatus(_F)
class _CienaCesRsvpteBlockadeMultiple_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214783647))
_CienaCesRsvpteBlockadeMultiple_Type.__name__=_C
_CienaCesRsvpteBlockadeMultiple_Object=MibScalar
cienaCesRsvpteBlockadeMultiple=_CienaCesRsvpteBlockadeMultiple_Object((1,3,6,1,4,1,1271,2,1,16,1,1,10),_CienaCesRsvpteBlockadeMultiple_Type())
cienaCesRsvpteBlockadeMultiple.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteBlockadeMultiple.setStatus(_A)
class _CienaCesRsvpteLSPSetupPriority_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CienaCesRsvpteLSPSetupPriority_Type.__name__=_C
_CienaCesRsvpteLSPSetupPriority_Object=MibScalar
cienaCesRsvpteLSPSetupPriority=_CienaCesRsvpteLSPSetupPriority_Object((1,3,6,1,4,1,1271,2,1,16,1,1,11),_CienaCesRsvpteLSPSetupPriority_Type())
cienaCesRsvpteLSPSetupPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteLSPSetupPriority.setStatus(_A)
class _CienaCesRsvpteLSPHoldingPriority_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CienaCesRsvpteLSPHoldingPriority_Type.__name__=_C
_CienaCesRsvpteLSPHoldingPriority_Object=MibScalar
cienaCesRsvpteLSPHoldingPriority=_CienaCesRsvpteLSPHoldingPriority_Object((1,3,6,1,4,1,1271,2,1,16,1,1,12),_CienaCesRsvpteLSPHoldingPriority_Type())
cienaCesRsvpteLSPHoldingPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteLSPHoldingPriority.setStatus(_A)
class _CienaCesRsvpteUseHopByHop_Type(TruthValue):defaultValue=2
_CienaCesRsvpteUseHopByHop_Type.__name__=_E
_CienaCesRsvpteUseHopByHop_Object=MibScalar
cienaCesRsvpteUseHopByHop=_CienaCesRsvpteUseHopByHop_Object((1,3,6,1,4,1,1271,2,1,16,1,1,13),_CienaCesRsvpteUseHopByHop_Type())
cienaCesRsvpteUseHopByHop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteUseHopByHop.setStatus(_A)
class _CienaCesRsvpteRestartCapable_Type(TruthValue):defaultValue=1
_CienaCesRsvpteRestartCapable_Type.__name__=_E
_CienaCesRsvpteRestartCapable_Object=MibScalar
cienaCesRsvpteRestartCapable=_CienaCesRsvpteRestartCapable_Object((1,3,6,1,4,1,1271,2,1,16,1,1,14),_CienaCesRsvpteRestartCapable_Type())
cienaCesRsvpteRestartCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRestartCapable.setStatus(_A)
class _CienaCesRsvpteRestartTime_Type(Unsigned32):defaultValue=60000
_CienaCesRsvpteRestartTime_Type.__name__=_D
_CienaCesRsvpteRestartTime_Object=MibScalar
cienaCesRsvpteRestartTime=_CienaCesRsvpteRestartTime_Object((1,3,6,1,4,1,1271,2,1,16,1,1,15),_CienaCesRsvpteRestartTime_Type())
cienaCesRsvpteRestartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRestartTime.setStatus(_A)
class _CienaCesRsvpteRecoveryTime_Type(Unsigned32):defaultValue=120000
_CienaCesRsvpteRecoveryTime_Type.__name__=_D
_CienaCesRsvpteRecoveryTime_Object=MibScalar
cienaCesRsvpteRecoveryTime=_CienaCesRsvpteRecoveryTime_Object((1,3,6,1,4,1,1271,2,1,16,1,1,16),_CienaCesRsvpteRecoveryTime_Type())
cienaCesRsvpteRecoveryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRecoveryTime.setStatus(_A)
class _CienaCesRsvpteMinPeerRestart_Type(Integer32):defaultValue=0
_CienaCesRsvpteMinPeerRestart_Type.__name__=_C
_CienaCesRsvpteMinPeerRestart_Object=MibScalar
cienaCesRsvpteMinPeerRestart=_CienaCesRsvpteMinPeerRestart_Object((1,3,6,1,4,1,1271,2,1,16,1,1,17),_CienaCesRsvpteMinPeerRestart_Type())
cienaCesRsvpteMinPeerRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteMinPeerRestart.setStatus(_A)
class _CienaCesRsvpteRefreshSlewDenominator_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214783647))
_CienaCesRsvpteRefreshSlewDenominator_Type.__name__=_C
_CienaCesRsvpteRefreshSlewDenominator_Object=MibScalar
cienaCesRsvpteRefreshSlewDenominator=_CienaCesRsvpteRefreshSlewDenominator_Object((1,3,6,1,4,1,1271,2,1,16,1,1,18),_CienaCesRsvpteRefreshSlewDenominator_Type())
cienaCesRsvpteRefreshSlewDenominator.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRefreshSlewDenominator.setStatus(_A)
class _CienaCesRsvpteRefreshSlewNumerator_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214783647))
_CienaCesRsvpteRefreshSlewNumerator_Type.__name__=_C
_CienaCesRsvpteRefreshSlewNumerator_Object=MibScalar
cienaCesRsvpteRefreshSlewNumerator=_CienaCesRsvpteRefreshSlewNumerator_Object((1,3,6,1,4,1,1271,2,1,16,1,1,19),_CienaCesRsvpteRefreshSlewNumerator_Type())
cienaCesRsvpteRefreshSlewNumerator.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteRefreshSlewNumerator.setStatus(_A)
_CienaCesRsvpteGRAdminStatus_Type=CienaGlobalState
_CienaCesRsvpteGRAdminStatus_Object=MibScalar
cienaCesRsvpteGRAdminStatus=_CienaCesRsvpteGRAdminStatus_Object((1,3,6,1,4,1,1271,2,1,16,1,1,20),_CienaCesRsvpteGRAdminStatus_Type())
cienaCesRsvpteGRAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteGRAdminStatus.setStatus(_A)
_CienaCesRsvpteGRMode_Type=RsvpGRMode
_CienaCesRsvpteGRMode_Object=MibScalar
cienaCesRsvpteGRMode=_CienaCesRsvpteGRMode_Object((1,3,6,1,4,1,1271,2,1,16,1,1,21),_CienaCesRsvpteGRMode_Type())
cienaCesRsvpteGRMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteGRMode.setStatus(_A)
_CienaCesRsvpte_ObjectIdentity=ObjectIdentity
cienaCesRsvpte=_CienaCesRsvpte_ObjectIdentity((1,3,6,1,4,1,1271,2,1,16,1,2))
_CienaCesRsvpteIfTable_Object=MibTable
cienaCesRsvpteIfTable=_CienaCesRsvpteIfTable_Object((1,3,6,1,4,1,1271,2,1,16,1,2,1))
if mibBuilder.loadTexts:cienaCesRsvpteIfTable.setStatus(_A)
_CienaCesRsvpteIfEntry_Object=MibTableRow
cienaCesRsvpteIfEntry=_CienaCesRsvpteIfEntry_Object((1,3,6,1,4,1,1271,2,1,16,1,2,1,1))
cienaCesRsvpteIfEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:cienaCesRsvpteIfEntry.setStatus(_A)
class _CienaCesRsvpteIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_CienaCesRsvpteIfIndex_Type.__name__=_C
_CienaCesRsvpteIfIndex_Object=MibTableColumn
cienaCesRsvpteIfIndex=_CienaCesRsvpteIfIndex_Object((1,3,6,1,4,1,1271,2,1,16,1,2,1,1,1),_CienaCesRsvpteIfIndex_Type())
cienaCesRsvpteIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cienaCesRsvpteIfIndex.setStatus(_A)
class _CienaCesRsvpteIfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CienaCesRsvpteIfName_Type.__name__=_G
_CienaCesRsvpteIfName_Object=MibTableColumn
cienaCesRsvpteIfName=_CienaCesRsvpteIfName_Object((1,3,6,1,4,1,1271,2,1,16,1,2,1,1,2),_CienaCesRsvpteIfName_Type())
cienaCesRsvpteIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteIfName.setStatus(_A)
_CienaCesRsvpteIfIpAddr_Type=IpAddress
_CienaCesRsvpteIfIpAddr_Object=MibTableColumn
cienaCesRsvpteIfIpAddr=_CienaCesRsvpteIfIpAddr_Object((1,3,6,1,4,1,1271,2,1,16,1,2,1,1,3),_CienaCesRsvpteIfIpAddr_Type())
cienaCesRsvpteIfIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteIfIpAddr.setStatus(_A)
class _CienaCesRsvpteIfMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,9216))
_CienaCesRsvpteIfMtu_Type.__name__=_C
_CienaCesRsvpteIfMtu_Object=MibTableColumn
cienaCesRsvpteIfMtu=_CienaCesRsvpteIfMtu_Object((1,3,6,1,4,1,1271,2,1,16,1,2,1,1,4),_CienaCesRsvpteIfMtu_Type())
cienaCesRsvpteIfMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteIfMtu.setStatus(_F)
_CienaCesRsvpteIfAdminStatus_Type=CienaGlobalState
_CienaCesRsvpteIfAdminStatus_Object=MibTableColumn
cienaCesRsvpteIfAdminStatus=_CienaCesRsvpteIfAdminStatus_Object((1,3,6,1,4,1,1271,2,1,16,1,2,1,1,5),_CienaCesRsvpteIfAdminStatus_Type())
cienaCesRsvpteIfAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteIfAdminStatus.setStatus(_A)
class _CienaCesRsvpteIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CienaCesRsvpteIfOperStatus_Type.__name__=_C
_CienaCesRsvpteIfOperStatus_Object=MibTableColumn
cienaCesRsvpteIfOperStatus=_CienaCesRsvpteIfOperStatus_Object((1,3,6,1,4,1,1271,2,1,16,1,2,1,1,6),_CienaCesRsvpteIfOperStatus_Type())
cienaCesRsvpteIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteIfOperStatus.setStatus(_A)
class _CienaCesRsvpteIfHelloInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CienaCesRsvpteIfHelloInterval_Type.__name__=_D
_CienaCesRsvpteIfHelloInterval_Object=MibTableColumn
cienaCesRsvpteIfHelloInterval=_CienaCesRsvpteIfHelloInterval_Object((1,3,6,1,4,1,1271,2,1,16,1,2,1,1,7),_CienaCesRsvpteIfHelloInterval_Type())
cienaCesRsvpteIfHelloInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteIfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:cienaCesRsvpteIfHelloInterval.setUnits(_H)
class _CienaCesRsvpteIfHelloTolerance_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CienaCesRsvpteIfHelloTolerance_Type.__name__=_D
_CienaCesRsvpteIfHelloTolerance_Object=MibTableColumn
cienaCesRsvpteIfHelloTolerance=_CienaCesRsvpteIfHelloTolerance_Object((1,3,6,1,4,1,1271,2,1,16,1,2,1,1,8),_CienaCesRsvpteIfHelloTolerance_Type())
cienaCesRsvpteIfHelloTolerance.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteIfHelloTolerance.setStatus(_A)
class _CienaCesRsvpteIfAdvertisedLabel_Type(AdvertisedLabel):defaultValue=99
_CienaCesRsvpteIfAdvertisedLabel_Type.__name__=_K
_CienaCesRsvpteIfAdvertisedLabel_Object=MibTableColumn
cienaCesRsvpteIfAdvertisedLabel=_CienaCesRsvpteIfAdvertisedLabel_Object((1,3,6,1,4,1,1271,2,1,16,1,2,1,1,9),_CienaCesRsvpteIfAdvertisedLabel_Type())
cienaCesRsvpteIfAdvertisedLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRsvpteIfAdvertisedLabel.setStatus(_A)
mibBuilder.exportSymbols(_I,**{_K:AdvertisedLabel,'RsvpOperStatus':RsvpOperStatus,'RsvpGRMode':RsvpGRMode,'cienaCesRsvpteMIB':cienaCesRsvpteMIB,'cienaCesRsvpteMIBObjects':cienaCesRsvpteMIBObjects,'cienaCesRsvpteObjects':cienaCesRsvpteObjects,'cienaCesRsvpteAdminStatus':cienaCesRsvpteAdminStatus,'cienaCesRsvpteOperStatus':cienaCesRsvpteOperStatus,'cienaCesRsvpteRetryInterval':cienaCesRsvpteRetryInterval,'cienaCesRsvpteRetryInfiniteState':cienaCesRsvpteRetryInfiniteState,'cienaCesRsvpteRetryMax':cienaCesRsvpteRetryMax,'cienaCesRsvpteRefreshInterval':cienaCesRsvpteRefreshInterval,'cienaCesRsvpteRefreshMultiple':cienaCesRsvpteRefreshMultiple,'cienaCesRsvpteRfrshSlewDenom':cienaCesRsvpteRfrshSlewDenom,'cienaCesRsvpteRfrshSlewNumerator':cienaCesRsvpteRfrshSlewNumerator,'cienaCesRsvpteBlockadeMultiple':cienaCesRsvpteBlockadeMultiple,'cienaCesRsvpteLSPSetupPriority':cienaCesRsvpteLSPSetupPriority,'cienaCesRsvpteLSPHoldingPriority':cienaCesRsvpteLSPHoldingPriority,'cienaCesRsvpteUseHopByHop':cienaCesRsvpteUseHopByHop,'cienaCesRsvpteRestartCapable':cienaCesRsvpteRestartCapable,'cienaCesRsvpteRestartTime':cienaCesRsvpteRestartTime,'cienaCesRsvpteRecoveryTime':cienaCesRsvpteRecoveryTime,'cienaCesRsvpteMinPeerRestart':cienaCesRsvpteMinPeerRestart,'cienaCesRsvpteRefreshSlewDenominator':cienaCesRsvpteRefreshSlewDenominator,'cienaCesRsvpteRefreshSlewNumerator':cienaCesRsvpteRefreshSlewNumerator,'cienaCesRsvpteGRAdminStatus':cienaCesRsvpteGRAdminStatus,'cienaCesRsvpteGRMode':cienaCesRsvpteGRMode,'cienaCesRsvpte':cienaCesRsvpte,'cienaCesRsvpteIfTable':cienaCesRsvpteIfTable,'cienaCesRsvpteIfEntry':cienaCesRsvpteIfEntry,_J:cienaCesRsvpteIfIndex,'cienaCesRsvpteIfName':cienaCesRsvpteIfName,'cienaCesRsvpteIfIpAddr':cienaCesRsvpteIfIpAddr,'cienaCesRsvpteIfMtu':cienaCesRsvpteIfMtu,'cienaCesRsvpteIfAdminStatus':cienaCesRsvpteIfAdminStatus,'cienaCesRsvpteIfOperStatus':cienaCesRsvpteIfOperStatus,'cienaCesRsvpteIfHelloInterval':cienaCesRsvpteIfHelloInterval,'cienaCesRsvpteIfHelloTolerance':cienaCesRsvpteIfHelloTolerance,'cienaCesRsvpteIfAdvertisedLabel':cienaCesRsvpteIfAdvertisedLabel})