_M='AdvertisedLabel'
_L='wwpLeosRsvpteIfIndex'
_K='WWP-LEOS-RSVPTE-MIB'
_J='seconds'
_I='disable'
_H='enable'
_G='DisplayString'
_F='TruthValue'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention',_F)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosRsvpteMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,30))
if mibBuilder.loadTexts:wwpLeosRsvpteMIB.setRevisions(('2011-07-06 00:00','2005-08-08 17:00'))
class AdvertisedLabel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,99)));namedValues=NamedValues(*(('implicitnull',1),('nonreserved',99)))
_WwpLeosRsvpteMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosRsvpteMIBObjects=_WwpLeosRsvpteMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,30,1))
_WwpLeosRsvpteObjects_ObjectIdentity=ObjectIdentity
wwpLeosRsvpteObjects=_WwpLeosRsvpteObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,30,1,1))
class _WwpLeosRsvpteAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosRsvpteAdminStatus_Type.__name__=_B
_WwpLeosRsvpteAdminStatus_Object=MibScalar
wwpLeosRsvpteAdminStatus=_WwpLeosRsvpteAdminStatus_Object((1,3,6,1,4,1,6141,2,60,30,1,1,1),_WwpLeosRsvpteAdminStatus_Type())
wwpLeosRsvpteAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRsvpteAdminStatus.setStatus(_A)
class _WwpLeosRsvpteOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),('down',2),('goingUp',3),('goingDown',4),('actFailed',5)))
_WwpLeosRsvpteOperStatus_Type.__name__=_B
_WwpLeosRsvpteOperStatus_Object=MibScalar
wwpLeosRsvpteOperStatus=_WwpLeosRsvpteOperStatus_Object((1,3,6,1,4,1,6141,2,60,30,1,1,2),_WwpLeosRsvpteOperStatus_Type())
wwpLeosRsvpteOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteOperStatus.setStatus(_A)
class _WwpLeosRsvpteRetryInterval_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,65))
_WwpLeosRsvpteRetryInterval_Type.__name__=_E
_WwpLeosRsvpteRetryInterval_Object=MibScalar
wwpLeosRsvpteRetryInterval=_WwpLeosRsvpteRetryInterval_Object((1,3,6,1,4,1,6141,2,60,30,1,1,3),_WwpLeosRsvpteRetryInterval_Type())
wwpLeosRsvpteRetryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRsvpteRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosRsvpteRetryInterval.setUnits(_J)
class _WwpLeosRsvpteRetryInfiniteState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosRsvpteRetryInfiniteState_Type.__name__=_B
_WwpLeosRsvpteRetryInfiniteState_Object=MibScalar
wwpLeosRsvpteRetryInfiniteState=_WwpLeosRsvpteRetryInfiniteState_Object((1,3,6,1,4,1,6141,2,60,30,1,1,4),_WwpLeosRsvpteRetryInfiniteState_Type())
wwpLeosRsvpteRetryInfiniteState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRsvpteRetryInfiniteState.setStatus(_A)
class _WwpLeosRsvpteRetryMax_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WwpLeosRsvpteRetryMax_Type.__name__=_B
_WwpLeosRsvpteRetryMax_Object=MibScalar
wwpLeosRsvpteRetryMax=_WwpLeosRsvpteRetryMax_Object((1,3,6,1,4,1,6141,2,60,30,1,1,5),_WwpLeosRsvpteRetryMax_Type())
wwpLeosRsvpteRetryMax.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteRetryMax.setStatus(_A)
class _WwpLeosRsvpteRefreshInterval_Type(Integer32):defaultValue=30000
_WwpLeosRsvpteRefreshInterval_Type.__name__=_B
_WwpLeosRsvpteRefreshInterval_Object=MibScalar
wwpLeosRsvpteRefreshInterval=_WwpLeosRsvpteRefreshInterval_Object((1,3,6,1,4,1,6141,2,60,30,1,1,6),_WwpLeosRsvpteRefreshInterval_Type())
wwpLeosRsvpteRefreshInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteRefreshInterval.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosRsvpteRefreshInterval.setUnits('milliseconds')
class _WwpLeosRsvpteRefreshMultiple_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214783647))
_WwpLeosRsvpteRefreshMultiple_Type.__name__=_B
_WwpLeosRsvpteRefreshMultiple_Object=MibScalar
wwpLeosRsvpteRefreshMultiple=_WwpLeosRsvpteRefreshMultiple_Object((1,3,6,1,4,1,6141,2,60,30,1,1,7),_WwpLeosRsvpteRefreshMultiple_Type())
wwpLeosRsvpteRefreshMultiple.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteRefreshMultiple.setStatus(_A)
class _WwpLeosRsvpteRfrshSlewDenom_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214783647))
_WwpLeosRsvpteRfrshSlewDenom_Type.__name__=_B
_WwpLeosRsvpteRfrshSlewDenom_Object=MibScalar
wwpLeosRsvpteRfrshSlewDenom=_WwpLeosRsvpteRfrshSlewDenom_Object((1,3,6,1,4,1,6141,2,60,30,1,1,8),_WwpLeosRsvpteRfrshSlewDenom_Type())
wwpLeosRsvpteRfrshSlewDenom.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteRfrshSlewDenom.setStatus(_A)
class _WwpLeosRsvpteRfrshSlewNumerator_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214783647))
_WwpLeosRsvpteRfrshSlewNumerator_Type.__name__=_B
_WwpLeosRsvpteRfrshSlewNumerator_Object=MibScalar
wwpLeosRsvpteRfrshSlewNumerator=_WwpLeosRsvpteRfrshSlewNumerator_Object((1,3,6,1,4,1,6141,2,60,30,1,1,9),_WwpLeosRsvpteRfrshSlewNumerator_Type())
wwpLeosRsvpteRfrshSlewNumerator.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteRfrshSlewNumerator.setStatus(_A)
class _WwpLeosRsvpteBlockadeMultiple_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214783647))
_WwpLeosRsvpteBlockadeMultiple_Type.__name__=_B
_WwpLeosRsvpteBlockadeMultiple_Object=MibScalar
wwpLeosRsvpteBlockadeMultiple=_WwpLeosRsvpteBlockadeMultiple_Object((1,3,6,1,4,1,6141,2,60,30,1,1,10),_WwpLeosRsvpteBlockadeMultiple_Type())
wwpLeosRsvpteBlockadeMultiple.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteBlockadeMultiple.setStatus(_A)
class _WwpLeosRsvpteLSPSetupPriority_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosRsvpteLSPSetupPriority_Type.__name__=_B
_WwpLeosRsvpteLSPSetupPriority_Object=MibScalar
wwpLeosRsvpteLSPSetupPriority=_WwpLeosRsvpteLSPSetupPriority_Object((1,3,6,1,4,1,6141,2,60,30,1,1,11),_WwpLeosRsvpteLSPSetupPriority_Type())
wwpLeosRsvpteLSPSetupPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteLSPSetupPriority.setStatus(_A)
class _WwpLeosRsvpteLSPHoldingPriority_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosRsvpteLSPHoldingPriority_Type.__name__=_B
_WwpLeosRsvpteLSPHoldingPriority_Object=MibScalar
wwpLeosRsvpteLSPHoldingPriority=_WwpLeosRsvpteLSPHoldingPriority_Object((1,3,6,1,4,1,6141,2,60,30,1,1,12),_WwpLeosRsvpteLSPHoldingPriority_Type())
wwpLeosRsvpteLSPHoldingPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteLSPHoldingPriority.setStatus(_A)
class _WwpLeosRsvpteUseHopByHop_Type(TruthValue):defaultValue=2
_WwpLeosRsvpteUseHopByHop_Type.__name__=_F
_WwpLeosRsvpteUseHopByHop_Object=MibScalar
wwpLeosRsvpteUseHopByHop=_WwpLeosRsvpteUseHopByHop_Object((1,3,6,1,4,1,6141,2,60,30,1,1,13),_WwpLeosRsvpteUseHopByHop_Type())
wwpLeosRsvpteUseHopByHop.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteUseHopByHop.setStatus(_A)
class _WwpLeosRsvpteRestartCapable_Type(TruthValue):defaultValue=2
_WwpLeosRsvpteRestartCapable_Type.__name__=_F
_WwpLeosRsvpteRestartCapable_Object=MibScalar
wwpLeosRsvpteRestartCapable=_WwpLeosRsvpteRestartCapable_Object((1,3,6,1,4,1,6141,2,60,30,1,1,14),_WwpLeosRsvpteRestartCapable_Type())
wwpLeosRsvpteRestartCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteRestartCapable.setStatus(_A)
class _WwpLeosRsvpteRestartTime_Type(Unsigned32):defaultValue=10000
_WwpLeosRsvpteRestartTime_Type.__name__=_E
_WwpLeosRsvpteRestartTime_Object=MibScalar
wwpLeosRsvpteRestartTime=_WwpLeosRsvpteRestartTime_Object((1,3,6,1,4,1,6141,2,60,30,1,1,15),_WwpLeosRsvpteRestartTime_Type())
wwpLeosRsvpteRestartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteRestartTime.setStatus(_A)
class _WwpLeosRsvpteRecoveryTime_Type(Unsigned32):defaultValue=10000
_WwpLeosRsvpteRecoveryTime_Type.__name__=_E
_WwpLeosRsvpteRecoveryTime_Object=MibScalar
wwpLeosRsvpteRecoveryTime=_WwpLeosRsvpteRecoveryTime_Object((1,3,6,1,4,1,6141,2,60,30,1,1,16),_WwpLeosRsvpteRecoveryTime_Type())
wwpLeosRsvpteRecoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteRecoveryTime.setStatus(_A)
class _WwpLeosRsvpteMinPeerRestart_Type(Integer32):defaultValue=0
_WwpLeosRsvpteMinPeerRestart_Type.__name__=_B
_WwpLeosRsvpteMinPeerRestart_Object=MibScalar
wwpLeosRsvpteMinPeerRestart=_WwpLeosRsvpteMinPeerRestart_Object((1,3,6,1,4,1,6141,2,60,30,1,1,17),_WwpLeosRsvpteMinPeerRestart_Type())
wwpLeosRsvpteMinPeerRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteMinPeerRestart.setStatus(_A)
_WwpLeosRsvpte_ObjectIdentity=ObjectIdentity
wwpLeosRsvpte=_WwpLeosRsvpte_ObjectIdentity((1,3,6,1,4,1,6141,2,60,30,1,2))
_WwpLeosRsvpteIfTable_Object=MibTable
wwpLeosRsvpteIfTable=_WwpLeosRsvpteIfTable_Object((1,3,6,1,4,1,6141,2,60,30,1,2,1))
if mibBuilder.loadTexts:wwpLeosRsvpteIfTable.setStatus(_A)
_WwpLeosRsvpteIfEntry_Object=MibTableRow
wwpLeosRsvpteIfEntry=_WwpLeosRsvpteIfEntry_Object((1,3,6,1,4,1,6141,2,60,30,1,2,1,1))
wwpLeosRsvpteIfEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:wwpLeosRsvpteIfEntry.setStatus(_A)
class _WwpLeosRsvpteIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpLeosRsvpteIfName_Type.__name__=_G
_WwpLeosRsvpteIfName_Object=MibTableColumn
wwpLeosRsvpteIfName=_WwpLeosRsvpteIfName_Object((1,3,6,1,4,1,6141,2,60,30,1,2,1,1,1),_WwpLeosRsvpteIfName_Type())
wwpLeosRsvpteIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteIfName.setStatus(_A)
class _WwpLeosRsvpteIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WwpLeosRsvpteIfIndex_Type.__name__=_B
_WwpLeosRsvpteIfIndex_Object=MibTableColumn
wwpLeosRsvpteIfIndex=_WwpLeosRsvpteIfIndex_Object((1,3,6,1,4,1,6141,2,60,30,1,2,1,1,2),_WwpLeosRsvpteIfIndex_Type())
wwpLeosRsvpteIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:wwpLeosRsvpteIfIndex.setStatus(_A)
_WwpLeosRsvpteIfIpAddr_Type=IpAddress
_WwpLeosRsvpteIfIpAddr_Object=MibTableColumn
wwpLeosRsvpteIfIpAddr=_WwpLeosRsvpteIfIpAddr_Object((1,3,6,1,4,1,6141,2,60,30,1,2,1,1,3),_WwpLeosRsvpteIfIpAddr_Type())
wwpLeosRsvpteIfIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteIfIpAddr.setStatus(_A)
class _WwpLeosRsvpteIfMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,9216))
_WwpLeosRsvpteIfMtu_Type.__name__=_B
_WwpLeosRsvpteIfMtu_Object=MibTableColumn
wwpLeosRsvpteIfMtu=_WwpLeosRsvpteIfMtu_Object((1,3,6,1,4,1,6141,2,60,30,1,2,1,1,4),_WwpLeosRsvpteIfMtu_Type())
wwpLeosRsvpteIfMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRsvpteIfMtu.setStatus(_A)
class _WwpLeosRsvpteIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosRsvpteIfAdminStatus_Type.__name__=_B
_WwpLeosRsvpteIfAdminStatus_Object=MibTableColumn
wwpLeosRsvpteIfAdminStatus=_WwpLeosRsvpteIfAdminStatus_Object((1,3,6,1,4,1,6141,2,60,30,1,2,1,1,5),_WwpLeosRsvpteIfAdminStatus_Type())
wwpLeosRsvpteIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRsvpteIfAdminStatus.setStatus(_A)
class _WwpLeosRsvpteIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_WwpLeosRsvpteIfOperStatus_Type.__name__=_B
_WwpLeosRsvpteIfOperStatus_Object=MibTableColumn
wwpLeosRsvpteIfOperStatus=_WwpLeosRsvpteIfOperStatus_Object((1,3,6,1,4,1,6141,2,60,30,1,2,1,1,6),_WwpLeosRsvpteIfOperStatus_Type())
wwpLeosRsvpteIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosRsvpteIfOperStatus.setStatus(_A)
class _WwpLeosRsvpteIfHelloInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_WwpLeosRsvpteIfHelloInterval_Type.__name__=_E
_WwpLeosRsvpteIfHelloInterval_Object=MibTableColumn
wwpLeosRsvpteIfHelloInterval=_WwpLeosRsvpteIfHelloInterval_Object((1,3,6,1,4,1,6141,2,60,30,1,2,1,1,7),_WwpLeosRsvpteIfHelloInterval_Type())
wwpLeosRsvpteIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRsvpteIfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosRsvpteIfHelloInterval.setUnits(_J)
class _WwpLeosRsvpteIfHelloTolerance_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_WwpLeosRsvpteIfHelloTolerance_Type.__name__=_E
_WwpLeosRsvpteIfHelloTolerance_Object=MibTableColumn
wwpLeosRsvpteIfHelloTolerance=_WwpLeosRsvpteIfHelloTolerance_Object((1,3,6,1,4,1,6141,2,60,30,1,2,1,1,8),_WwpLeosRsvpteIfHelloTolerance_Type())
wwpLeosRsvpteIfHelloTolerance.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRsvpteIfHelloTolerance.setStatus(_A)
class _WwpLeosRsvpteIfAdvertisedLabel_Type(AdvertisedLabel):defaultValue=99
_WwpLeosRsvpteIfAdvertisedLabel_Type.__name__=_M
_WwpLeosRsvpteIfAdvertisedLabel_Object=MibTableColumn
wwpLeosRsvpteIfAdvertisedLabel=_WwpLeosRsvpteIfAdvertisedLabel_Object((1,3,6,1,4,1,6141,2,60,30,1,2,1,1,9),_WwpLeosRsvpteIfAdvertisedLabel_Type())
wwpLeosRsvpteIfAdvertisedLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRsvpteIfAdvertisedLabel.setStatus(_A)
mibBuilder.exportSymbols(_K,**{_M:AdvertisedLabel,'wwpLeosRsvpteMIB':wwpLeosRsvpteMIB,'wwpLeosRsvpteMIBObjects':wwpLeosRsvpteMIBObjects,'wwpLeosRsvpteObjects':wwpLeosRsvpteObjects,'wwpLeosRsvpteAdminStatus':wwpLeosRsvpteAdminStatus,'wwpLeosRsvpteOperStatus':wwpLeosRsvpteOperStatus,'wwpLeosRsvpteRetryInterval':wwpLeosRsvpteRetryInterval,'wwpLeosRsvpteRetryInfiniteState':wwpLeosRsvpteRetryInfiniteState,'wwpLeosRsvpteRetryMax':wwpLeosRsvpteRetryMax,'wwpLeosRsvpteRefreshInterval':wwpLeosRsvpteRefreshInterval,'wwpLeosRsvpteRefreshMultiple':wwpLeosRsvpteRefreshMultiple,'wwpLeosRsvpteRfrshSlewDenom':wwpLeosRsvpteRfrshSlewDenom,'wwpLeosRsvpteRfrshSlewNumerator':wwpLeosRsvpteRfrshSlewNumerator,'wwpLeosRsvpteBlockadeMultiple':wwpLeosRsvpteBlockadeMultiple,'wwpLeosRsvpteLSPSetupPriority':wwpLeosRsvpteLSPSetupPriority,'wwpLeosRsvpteLSPHoldingPriority':wwpLeosRsvpteLSPHoldingPriority,'wwpLeosRsvpteUseHopByHop':wwpLeosRsvpteUseHopByHop,'wwpLeosRsvpteRestartCapable':wwpLeosRsvpteRestartCapable,'wwpLeosRsvpteRestartTime':wwpLeosRsvpteRestartTime,'wwpLeosRsvpteRecoveryTime':wwpLeosRsvpteRecoveryTime,'wwpLeosRsvpteMinPeerRestart':wwpLeosRsvpteMinPeerRestart,'wwpLeosRsvpte':wwpLeosRsvpte,'wwpLeosRsvpteIfTable':wwpLeosRsvpteIfTable,'wwpLeosRsvpteIfEntry':wwpLeosRsvpteIfEntry,'wwpLeosRsvpteIfName':wwpLeosRsvpteIfName,_L:wwpLeosRsvpteIfIndex,'wwpLeosRsvpteIfIpAddr':wwpLeosRsvpteIfIpAddr,'wwpLeosRsvpteIfMtu':wwpLeosRsvpteIfMtu,'wwpLeosRsvpteIfAdminStatus':wwpLeosRsvpteIfAdminStatus,'wwpLeosRsvpteIfOperStatus':wwpLeosRsvpteIfOperStatus,'wwpLeosRsvpteIfHelloInterval':wwpLeosRsvpteIfHelloInterval,'wwpLeosRsvpteIfHelloTolerance':wwpLeosRsvpteIfHelloTolerance,'wwpLeosRsvpteIfAdvertisedLabel':wwpLeosRsvpteIfAdvertisedLabel})