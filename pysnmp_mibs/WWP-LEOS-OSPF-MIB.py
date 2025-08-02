_L='wwpLeosOspfAddressLessIf'
_K='wwpLeosOspfIfIpAddress'
_J='wwpLeosOspfAreaId'
_I='milliseconds'
_H='Unsigned32'
_G='Integer32'
_F='not-accessible'
_E='WWP-LEOS-OSPF-MIB'
_D='read-write'
_C='TruthValue'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AreaID,=mibBuilder.importSymbols('OSPF-MIB','AreaID')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_C)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosOspfMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,31))
if mibBuilder.loadTexts:wwpLeosOspfMIB.setRevisions(('2001-04-03 17:00',))
class OspfOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('operStatusUp',1),('operStatusDown',2),('operStatusGoingUp',3),('operStatusGoingDown',4),('operStatusActFailed',5)))
_WwpLeosOspfMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosOspfMIBObjects=_WwpLeosOspfMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,31,1))
_WwpLeosOspfGeneralGroup_ObjectIdentity=ObjectIdentity
wwpLeosOspfGeneralGroup=_WwpLeosOspfGeneralGroup_ObjectIdentity((1,3,6,1,4,1,6141,2,60,31,1,1))
class _WwpLeosOspfRFC1583Comp_Type(TruthValue):defaultValue=2
_WwpLeosOspfRFC1583Comp_Type.__name__=_C
_WwpLeosOspfRFC1583Comp_Object=MibScalar
wwpLeosOspfRFC1583Comp=_WwpLeosOspfRFC1583Comp_Object((1,3,6,1,4,1,6141,2,60,31,1,1,1),_WwpLeosOspfRFC1583Comp_Type())
wwpLeosOspfRFC1583Comp.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOspfRFC1583Comp.setStatus(_A)
_WwpLeosOspfOperStatus_Type=OspfOperStatus
_WwpLeosOspfOperStatus_Object=MibScalar
wwpLeosOspfOperStatus=_WwpLeosOspfOperStatus_Object((1,3,6,1,4,1,6141,2,60,31,1,1,2),_WwpLeosOspfOperStatus_Type())
wwpLeosOspfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfOperStatus.setStatus(_A)
class _WwpLeosOspfOpaqueLsaSupport_Type(TruthValue):defaultValue=1
_WwpLeosOspfOpaqueLsaSupport_Type.__name__=_C
_WwpLeosOspfOpaqueLsaSupport_Object=MibScalar
wwpLeosOspfOpaqueLsaSupport=_WwpLeosOspfOpaqueLsaSupport_Object((1,3,6,1,4,1,6141,2,60,31,1,1,3),_WwpLeosOspfOpaqueLsaSupport_Type())
wwpLeosOspfOpaqueLsaSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOspfOpaqueLsaSupport.setStatus(_A)
class _WwpLeosOspfTrafficEngSupport_Type(TruthValue):defaultValue=1
_WwpLeosOspfTrafficEngSupport_Type.__name__=_C
_WwpLeosOspfTrafficEngSupport_Object=MibScalar
wwpLeosOspfTrafficEngSupport=_WwpLeosOspfTrafficEngSupport_Object((1,3,6,1,4,1,6141,2,60,31,1,1,4),_WwpLeosOspfTrafficEngSupport_Type())
wwpLeosOspfTrafficEngSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfTrafficEngSupport.setStatus(_A)
_WwpLeosOspfExtOpLsaCount_Type=Gauge32
_WwpLeosOspfExtOpLsaCount_Object=MibScalar
wwpLeosOspfExtOpLsaCount=_WwpLeosOspfExtOpLsaCount_Object((1,3,6,1,4,1,6141,2,60,31,1,1,5),_WwpLeosOspfExtOpLsaCount_Type())
wwpLeosOspfExtOpLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfExtOpLsaCount.setStatus(_A)
_WwpLeosOspfExtOpLsaCksumSum_Type=Integer32
_WwpLeosOspfExtOpLsaCksumSum_Object=MibScalar
wwpLeosOspfExtOpLsaCksumSum=_WwpLeosOspfExtOpLsaCksumSum_Object((1,3,6,1,4,1,6141,2,60,31,1,1,6),_WwpLeosOspfExtOpLsaCksumSum_Type())
wwpLeosOspfExtOpLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfExtOpLsaCksumSum.setStatus(_A)
_WwpLeosOspfNumUpdPending_Type=Unsigned32
_WwpLeosOspfNumUpdPending_Object=MibScalar
wwpLeosOspfNumUpdPending=_WwpLeosOspfNumUpdPending_Object((1,3,6,1,4,1,6141,2,60,31,1,1,7),_WwpLeosOspfNumUpdPending_Type())
wwpLeosOspfNumUpdPending.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfNumUpdPending.setStatus(_A)
_WwpLeosOspfNumUpdMerged_Type=Unsigned32
_WwpLeosOspfNumUpdMerged_Object=MibScalar
wwpLeosOspfNumUpdMerged=_WwpLeosOspfNumUpdMerged_Object((1,3,6,1,4,1,6141,2,60,31,1,1,8),_WwpLeosOspfNumUpdMerged_Type())
wwpLeosOspfNumUpdMerged.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfNumUpdMerged.setStatus(_A)
_WwpLeosOspfNumCksumsPending_Type=Unsigned32
_WwpLeosOspfNumCksumsPending_Object=MibScalar
wwpLeosOspfNumCksumsPending=_WwpLeosOspfNumCksumsPending_Object((1,3,6,1,4,1,6141,2,60,31,1,1,9),_WwpLeosOspfNumCksumsPending_Type())
wwpLeosOspfNumCksumsPending.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfNumCksumsPending.setStatus(_A)
class _WwpLeosOspfCalcMaxDelay_Type(Unsigned32):defaultValue=5000
_WwpLeosOspfCalcMaxDelay_Type.__name__=_H
_WwpLeosOspfCalcMaxDelay_Object=MibScalar
wwpLeosOspfCalcMaxDelay=_WwpLeosOspfCalcMaxDelay_Object((1,3,6,1,4,1,6141,2,60,31,1,1,10),_WwpLeosOspfCalcMaxDelay_Type())
wwpLeosOspfCalcMaxDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOspfCalcMaxDelay.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOspfCalcMaxDelay.setUnits(_I)
_WwpLeosOspf_ObjectIdentity=ObjectIdentity
wwpLeosOspf=_WwpLeosOspf_ObjectIdentity((1,3,6,1,4,1,6141,2,60,31,1,2))
_WwpLeosOspfAreaTable_Object=MibTable
wwpLeosOspfAreaTable=_WwpLeosOspfAreaTable_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1))
if mibBuilder.loadTexts:wwpLeosOspfAreaTable.setStatus(_A)
_WwpLeosOspfAreaEntry_Object=MibTableRow
wwpLeosOspfAreaEntry=_WwpLeosOspfAreaEntry_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1))
wwpLeosOspfAreaEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:wwpLeosOspfAreaEntry.setStatus(_A)
_WwpLeosOspfAreaId_Type=AreaID
_WwpLeosOspfAreaId_Object=MibTableColumn
wwpLeosOspfAreaId=_WwpLeosOspfAreaId_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,1),_WwpLeosOspfAreaId_Type())
wwpLeosOspfAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosOspfAreaId.setStatus(_A)
class _WwpLeosOspfAreaTransitCapability_Type(TruthValue):defaultValue=2
_WwpLeosOspfAreaTransitCapability_Type.__name__=_C
_WwpLeosOspfAreaTransitCapability_Object=MibTableColumn
wwpLeosOspfAreaTransitCapability=_WwpLeosOspfAreaTransitCapability_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,2),_WwpLeosOspfAreaTransitCapability_Type())
wwpLeosOspfAreaTransitCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaTransitCapability.setStatus(_A)
_WwpLeosOspfAreaRtrLsaCount_Type=Gauge32
_WwpLeosOspfAreaRtrLsaCount_Object=MibTableColumn
wwpLeosOspfAreaRtrLsaCount=_WwpLeosOspfAreaRtrLsaCount_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,3),_WwpLeosOspfAreaRtrLsaCount_Type())
wwpLeosOspfAreaRtrLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaRtrLsaCount.setStatus(_A)
_WwpLeosOspfAreaRtrLsaCksumSum_Type=Integer32
_WwpLeosOspfAreaRtrLsaCksumSum_Object=MibTableColumn
wwpLeosOspfAreaRtrLsaCksumSum=_WwpLeosOspfAreaRtrLsaCksumSum_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,4),_WwpLeosOspfAreaRtrLsaCksumSum_Type())
wwpLeosOspfAreaRtrLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaRtrLsaCksumSum.setStatus(_A)
_WwpLeosOspfAreaNetLsaCount_Type=Gauge32
_WwpLeosOspfAreaNetLsaCount_Object=MibTableColumn
wwpLeosOspfAreaNetLsaCount=_WwpLeosOspfAreaNetLsaCount_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,5),_WwpLeosOspfAreaNetLsaCount_Type())
wwpLeosOspfAreaNetLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaNetLsaCount.setStatus(_A)
_WwpLeosOspfAreaNetLsaCksumSum_Type=Integer32
_WwpLeosOspfAreaNetLsaCksumSum_Object=MibTableColumn
wwpLeosOspfAreaNetLsaCksumSum=_WwpLeosOspfAreaNetLsaCksumSum_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,6),_WwpLeosOspfAreaNetLsaCksumSum_Type())
wwpLeosOspfAreaNetLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaNetLsaCksumSum.setStatus(_A)
_WwpLeosOspfAreaSummLsaCount_Type=Gauge32
_WwpLeosOspfAreaSummLsaCount_Object=MibTableColumn
wwpLeosOspfAreaSummLsaCount=_WwpLeosOspfAreaSummLsaCount_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,7),_WwpLeosOspfAreaSummLsaCount_Type())
wwpLeosOspfAreaSummLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaSummLsaCount.setStatus(_A)
_WwpLeosOspfAreaSummLsaCksumSum_Type=Integer32
_WwpLeosOspfAreaSummLsaCksumSum_Object=MibTableColumn
wwpLeosOspfAreaSummLsaCksumSum=_WwpLeosOspfAreaSummLsaCksumSum_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,8),_WwpLeosOspfAreaSummLsaCksumSum_Type())
wwpLeosOspfAreaSummLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaSummLsaCksumSum.setStatus(_A)
_WwpLeosOspfAreaSummAsLsaCount_Type=Gauge32
_WwpLeosOspfAreaSummAsLsaCount_Object=MibTableColumn
wwpLeosOspfAreaSummAsLsaCount=_WwpLeosOspfAreaSummAsLsaCount_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,9),_WwpLeosOspfAreaSummAsLsaCount_Type())
wwpLeosOspfAreaSummAsLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaSummAsLsaCount.setStatus(_A)
_WwpLeosOspfAreaSummAsLsaCksumSum_Type=Integer32
_WwpLeosOspfAreaSummAsLsaCksumSum_Object=MibTableColumn
wwpLeosOspfAreaSummAsLsaCksumSum=_WwpLeosOspfAreaSummAsLsaCksumSum_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,10),_WwpLeosOspfAreaSummAsLsaCksumSum_Type())
wwpLeosOspfAreaSummAsLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaSummAsLsaCksumSum.setStatus(_A)
_WwpLeosOspfAreaNssaLsaCount_Type=Gauge32
_WwpLeosOspfAreaNssaLsaCount_Object=MibTableColumn
wwpLeosOspfAreaNssaLsaCount=_WwpLeosOspfAreaNssaLsaCount_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,11),_WwpLeosOspfAreaNssaLsaCount_Type())
wwpLeosOspfAreaNssaLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaNssaLsaCount.setStatus(_A)
_WwpLeosOspfAreaNssaLsaCksumSum_Type=Integer32
_WwpLeosOspfAreaNssaLsaCksumSum_Object=MibTableColumn
wwpLeosOspfAreaNssaLsaCksumSum=_WwpLeosOspfAreaNssaLsaCksumSum_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,12),_WwpLeosOspfAreaNssaLsaCksumSum_Type())
wwpLeosOspfAreaNssaLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaNssaLsaCksumSum.setStatus(_A)
_WwpLeosOspfAreaOpLsaCount_Type=Gauge32
_WwpLeosOspfAreaOpLsaCount_Object=MibTableColumn
wwpLeosOspfAreaOpLsaCount=_WwpLeosOspfAreaOpLsaCount_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,13),_WwpLeosOspfAreaOpLsaCount_Type())
wwpLeosOspfAreaOpLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaOpLsaCount.setStatus(_A)
_WwpLeosOspfAreaOpLsaCksumSum_Type=Integer32
_WwpLeosOspfAreaOpLsaCksumSum_Object=MibTableColumn
wwpLeosOspfAreaOpLsaCksumSum=_WwpLeosOspfAreaOpLsaCksumSum_Object((1,3,6,1,4,1,6141,2,60,31,1,2,1,1,14),_WwpLeosOspfAreaOpLsaCksumSum_Type())
wwpLeosOspfAreaOpLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfAreaOpLsaCksumSum.setStatus(_A)
_WwpLeosOspfIfTable_Object=MibTable
wwpLeosOspfIfTable=_WwpLeosOspfIfTable_Object((1,3,6,1,4,1,6141,2,60,31,1,2,2))
if mibBuilder.loadTexts:wwpLeosOspfIfTable.setStatus(_A)
_WwpLeosOspfIfEntry_Object=MibTableRow
wwpLeosOspfIfEntry=_WwpLeosOspfIfEntry_Object((1,3,6,1,4,1,6141,2,60,31,1,2,2,1))
wwpLeosOspfIfEntry.setIndexNames((0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:wwpLeosOspfIfEntry.setStatus(_A)
_WwpLeosOspfIfIpAddress_Type=IpAddress
_WwpLeosOspfIfIpAddress_Object=MibTableColumn
wwpLeosOspfIfIpAddress=_WwpLeosOspfIfIpAddress_Object((1,3,6,1,4,1,6141,2,60,31,1,2,2,1,1),_WwpLeosOspfIfIpAddress_Type())
wwpLeosOspfIfIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosOspfIfIpAddress.setStatus(_A)
_WwpLeosOspfAddressLessIf_Type=Integer32
_WwpLeosOspfAddressLessIf_Object=MibTableColumn
wwpLeosOspfAddressLessIf=_WwpLeosOspfAddressLessIf_Object((1,3,6,1,4,1,6141,2,60,31,1,2,2,1,2),_WwpLeosOspfAddressLessIf_Type())
wwpLeosOspfAddressLessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosOspfAddressLessIf.setStatus(_A)
_WwpLeosOspfIfLsaCount_Type=Gauge32
_WwpLeosOspfIfLsaCount_Object=MibTableColumn
wwpLeosOspfIfLsaCount=_WwpLeosOspfIfLsaCount_Object((1,3,6,1,4,1,6141,2,60,31,1,2,2,1,3),_WwpLeosOspfIfLsaCount_Type())
wwpLeosOspfIfLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfIfLsaCount.setStatus(_A)
_WwpLeosOspfIfLsaCksumSum_Type=Integer32
_WwpLeosOspfIfLsaCksumSum_Object=MibTableColumn
wwpLeosOspfIfLsaCksumSum=_WwpLeosOspfIfLsaCksumSum_Object((1,3,6,1,4,1,6141,2,60,31,1,2,2,1,4),_WwpLeosOspfIfLsaCksumSum_Type())
wwpLeosOspfIfLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfIfLsaCksumSum.setStatus(_A)
_WwpLeosOspfIfOperStatus_Type=OspfOperStatus
_WwpLeosOspfIfOperStatus_Object=MibTableColumn
wwpLeosOspfIfOperStatus=_WwpLeosOspfIfOperStatus_Object((1,3,6,1,4,1,6141,2,60,31,1,2,2,1,5),_WwpLeosOspfIfOperStatus_Type())
wwpLeosOspfIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfIfOperStatus.setStatus(_A)
_WwpLeosOspfIfNetMask_Type=IpAddress
_WwpLeosOspfIfNetMask_Object=MibTableColumn
wwpLeosOspfIfNetMask=_WwpLeosOspfIfNetMask_Object((1,3,6,1,4,1,6141,2,60,31,1,2,2,1,6),_WwpLeosOspfIfNetMask_Type())
wwpLeosOspfIfNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOspfIfNetMask.setStatus(_A)
class _WwpLeosOspfIfTransmitTimerDelay_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,429496999))
_WwpLeosOspfIfTransmitTimerDelay_Type.__name__=_G
_WwpLeosOspfIfTransmitTimerDelay_Object=MibTableColumn
wwpLeosOspfIfTransmitTimerDelay=_WwpLeosOspfIfTransmitTimerDelay_Object((1,3,6,1,4,1,6141,2,60,31,1,2,2,1,7),_WwpLeosOspfIfTransmitTimerDelay_Type())
wwpLeosOspfIfTransmitTimerDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOspfIfTransmitTimerDelay.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOspfIfTransmitTimerDelay.setUnits(_I)
mibBuilder.exportSymbols(_E,**{'OspfOperStatus':OspfOperStatus,'wwpLeosOspfMIB':wwpLeosOspfMIB,'wwpLeosOspfMIBObjects':wwpLeosOspfMIBObjects,'wwpLeosOspfGeneralGroup':wwpLeosOspfGeneralGroup,'wwpLeosOspfRFC1583Comp':wwpLeosOspfRFC1583Comp,'wwpLeosOspfOperStatus':wwpLeosOspfOperStatus,'wwpLeosOspfOpaqueLsaSupport':wwpLeosOspfOpaqueLsaSupport,'wwpLeosOspfTrafficEngSupport':wwpLeosOspfTrafficEngSupport,'wwpLeosOspfExtOpLsaCount':wwpLeosOspfExtOpLsaCount,'wwpLeosOspfExtOpLsaCksumSum':wwpLeosOspfExtOpLsaCksumSum,'wwpLeosOspfNumUpdPending':wwpLeosOspfNumUpdPending,'wwpLeosOspfNumUpdMerged':wwpLeosOspfNumUpdMerged,'wwpLeosOspfNumCksumsPending':wwpLeosOspfNumCksumsPending,'wwpLeosOspfCalcMaxDelay':wwpLeosOspfCalcMaxDelay,'wwpLeosOspf':wwpLeosOspf,'wwpLeosOspfAreaTable':wwpLeosOspfAreaTable,'wwpLeosOspfAreaEntry':wwpLeosOspfAreaEntry,_J:wwpLeosOspfAreaId,'wwpLeosOspfAreaTransitCapability':wwpLeosOspfAreaTransitCapability,'wwpLeosOspfAreaRtrLsaCount':wwpLeosOspfAreaRtrLsaCount,'wwpLeosOspfAreaRtrLsaCksumSum':wwpLeosOspfAreaRtrLsaCksumSum,'wwpLeosOspfAreaNetLsaCount':wwpLeosOspfAreaNetLsaCount,'wwpLeosOspfAreaNetLsaCksumSum':wwpLeosOspfAreaNetLsaCksumSum,'wwpLeosOspfAreaSummLsaCount':wwpLeosOspfAreaSummLsaCount,'wwpLeosOspfAreaSummLsaCksumSum':wwpLeosOspfAreaSummLsaCksumSum,'wwpLeosOspfAreaSummAsLsaCount':wwpLeosOspfAreaSummAsLsaCount,'wwpLeosOspfAreaSummAsLsaCksumSum':wwpLeosOspfAreaSummAsLsaCksumSum,'wwpLeosOspfAreaNssaLsaCount':wwpLeosOspfAreaNssaLsaCount,'wwpLeosOspfAreaNssaLsaCksumSum':wwpLeosOspfAreaNssaLsaCksumSum,'wwpLeosOspfAreaOpLsaCount':wwpLeosOspfAreaOpLsaCount,'wwpLeosOspfAreaOpLsaCksumSum':wwpLeosOspfAreaOpLsaCksumSum,'wwpLeosOspfIfTable':wwpLeosOspfIfTable,'wwpLeosOspfIfEntry':wwpLeosOspfIfEntry,_K:wwpLeosOspfIfIpAddress,_L:wwpLeosOspfAddressLessIf,'wwpLeosOspfIfLsaCount':wwpLeosOspfIfLsaCount,'wwpLeosOspfIfLsaCksumSum':wwpLeosOspfIfLsaCksumSum,'wwpLeosOspfIfOperStatus':wwpLeosOspfIfOperStatus,'wwpLeosOspfIfNetMask':wwpLeosOspfIfNetMask,'wwpLeosOspfIfTransmitTimerDelay':wwpLeosOspfIfTransmitTimerDelay})