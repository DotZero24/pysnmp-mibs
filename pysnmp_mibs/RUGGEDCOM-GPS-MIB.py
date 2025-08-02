_N='rcFreqAdj'
_M='rcGpsLongtitude'
_L='rcGpsLatitude'
_K='rcSatelliteInView'
_J='rcGpsAntPower'
_I='rcGpsCableCompensate'
_H='rcGpsLocInt'
_G='rcGpsStatusChange'
_F='read-write'
_E='rcGpsStatus'
_D='read-only'
_C='Integer32'
_B='RUGGEDCOM-GPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruggedcomMgmt,ruggedcomTraps=mibBuilder.importSymbols('RUGGEDCOM-MIB','ruggedcomMgmt','ruggedcomTraps')
RcTimeSyncStatus,=mibBuilder.importSymbols('RUGGEDCOM-TIMECONFIG-MIB','RcTimeSyncStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rcGps=ModuleIdentity((1,3,6,1,4,1,15004,4,9))
if mibBuilder.loadTexts:rcGps.setRevisions(('2015-10-30 17:00','2014-12-01 17:00'))
_RcGpsBase_ObjectIdentity=ObjectIdentity
rcGpsBase=_RcGpsBase_ObjectIdentity((1,3,6,1,4,1,15004,4,9,1))
_RcGpsStatus_Type=RcTimeSyncStatus
_RcGpsStatus_Object=MibScalar
rcGpsStatus=_RcGpsStatus_Object((1,3,6,1,4,1,15004,4,9,1,1),_RcGpsStatus_Type())
rcGpsStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcGpsStatus.setStatus(_A)
class _RcGpsLocInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_RcGpsLocInt_Type.__name__=_C
_RcGpsLocInt_Object=MibScalar
rcGpsLocInt=_RcGpsLocInt_Object((1,3,6,1,4,1,15004,4,9,1,2),_RcGpsLocInt_Type())
rcGpsLocInt.setMaxAccess(_F)
if mibBuilder.loadTexts:rcGpsLocInt.setStatus(_A)
class _RcGpsCableCompensate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50000))
_RcGpsCableCompensate_Type.__name__=_C
_RcGpsCableCompensate_Object=MibScalar
rcGpsCableCompensate=_RcGpsCableCompensate_Object((1,3,6,1,4,1,15004,4,9,1,3),_RcGpsCableCompensate_Type())
rcGpsCableCompensate.setMaxAccess(_F)
if mibBuilder.loadTexts:rcGpsCableCompensate.setStatus(_A)
_RcGpsAntPower_Type=TruthValue
_RcGpsAntPower_Object=MibScalar
rcGpsAntPower=_RcGpsAntPower_Object((1,3,6,1,4,1,15004,4,9,1,4),_RcGpsAntPower_Type())
rcGpsAntPower.setMaxAccess(_F)
if mibBuilder.loadTexts:rcGpsAntPower.setStatus(_A)
class _RcSatelliteInView_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_RcSatelliteInView_Type.__name__=_C
_RcSatelliteInView_Object=MibScalar
rcSatelliteInView=_RcSatelliteInView_Object((1,3,6,1,4,1,15004,4,9,1,5),_RcSatelliteInView_Type())
rcSatelliteInView.setMaxAccess(_D)
if mibBuilder.loadTexts:rcSatelliteInView.setStatus(_A)
_RcGpsLatitude_Type=DisplayString
_RcGpsLatitude_Object=MibScalar
rcGpsLatitude=_RcGpsLatitude_Object((1,3,6,1,4,1,15004,4,9,1,6),_RcGpsLatitude_Type())
rcGpsLatitude.setMaxAccess(_D)
if mibBuilder.loadTexts:rcGpsLatitude.setStatus(_A)
_RcGpsLongtitude_Type=DisplayString
_RcGpsLongtitude_Object=MibScalar
rcGpsLongtitude=_RcGpsLongtitude_Object((1,3,6,1,4,1,15004,4,9,1,7),_RcGpsLongtitude_Type())
rcGpsLongtitude.setMaxAccess(_D)
if mibBuilder.loadTexts:rcGpsLongtitude.setStatus(_A)
class _RcOFM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_RcOFM_Type.__name__=_C
_RcOFM_Object=MibScalar
rcOFM=_RcOFM_Object((1,3,6,1,4,1,15004,4,9,1,8),_RcOFM_Type())
rcOFM.setMaxAccess(_D)
if mibBuilder.loadTexts:rcOFM.setStatus(_A)
class _RcFreqAdj_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_RcFreqAdj_Type.__name__=_C
_RcFreqAdj_Object=MibScalar
rcFreqAdj=_RcFreqAdj_Object((1,3,6,1,4,1,15004,4,9,1,9),_RcFreqAdj_Type())
rcFreqAdj.setMaxAccess(_D)
if mibBuilder.loadTexts:rcFreqAdj.setStatus(_A)
_RcGpsConformance_ObjectIdentity=ObjectIdentity
rcGpsConformance=_RcGpsConformance_ObjectIdentity((1,3,6,1,4,1,15004,4,9,3))
_RcGpsGroups_ObjectIdentity=ObjectIdentity
rcGpsGroups=_RcGpsGroups_ObjectIdentity((1,3,6,1,4,1,15004,4,9,3,2))
rcGpsBaseGroup=ObjectGroup((1,3,6,1,4,1,15004,4,9,3,2,1))
rcGpsBaseGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:rcGpsBaseGroup.setStatus(_A)
rcGpsNotifyGroup=ObjectGroup((1,3,6,1,4,1,15004,4,9,3,2,2))
rcGpsNotifyGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:rcGpsNotifyGroup.setStatus(_A)
rcGpsBaseGroup01=ObjectGroup((1,3,6,1,4,1,15004,4,9,3,2,3))
rcGpsBaseGroup01.setObjects(*((_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,'rcOFM'),(_B,_N)))
if mibBuilder.loadTexts:rcGpsBaseGroup01.setStatus(_A)
rcGpsStatusChange=NotificationType((1,3,6,1,4,1,15004,5,19))
rcGpsStatusChange.setObjects((_B,_E))
if mibBuilder.loadTexts:rcGpsStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rcGps':rcGps,'rcGpsBase':rcGpsBase,_E:rcGpsStatus,_H:rcGpsLocInt,_I:rcGpsCableCompensate,_J:rcGpsAntPower,_K:rcSatelliteInView,_L:rcGpsLatitude,_M:rcGpsLongtitude,'rcOFM':rcOFM,_N:rcFreqAdj,'rcGpsConformance':rcGpsConformance,'rcGpsGroups':rcGpsGroups,'rcGpsBaseGroup':rcGpsBaseGroup,'rcGpsNotifyGroup':rcGpsNotifyGroup,'rcGpsBaseGroup01':rcGpsBaseGroup01,_G:rcGpsStatusChange})