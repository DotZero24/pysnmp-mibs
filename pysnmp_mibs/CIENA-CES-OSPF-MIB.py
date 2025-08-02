_K='cienaCesOspfAddressLessIf'
_J='cienaCesOspfIfIpAddress'
_I='cienaCesOspfAreaId'
_H='milliseconds'
_G='Unsigned32'
_F='not-accessible'
_E='Integer32'
_D='CIENA-CES-OSPF-MIB'
_C='TruthValue'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaCesConfig,=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig')
AreaID,=mibBuilder.importSymbols('OSPF-MIB','AreaID')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_C)
cienaCesOspfMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,19))
if mibBuilder.loadTexts:cienaCesOspfMIB.setRevisions(('2017-06-07 00:00','2013-04-18 00:00','2011-02-02 00:00'))
class OspfOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('operStatusUp',1),('operStatusDown',2),('operStatusGoingUp',3),('operStatusGoingDown',4),('operStatusActFailed',5)))
_CienaCesOspfMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesOspfMIBObjects=_CienaCesOspfMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,19,1))
_CienaCesOspfGeneralGroup_ObjectIdentity=ObjectIdentity
cienaCesOspfGeneralGroup=_CienaCesOspfGeneralGroup_ObjectIdentity((1,3,6,1,4,1,1271,2,1,19,1,1))
class _CienaCesOspfRFC1583Comp_Type(TruthValue):defaultValue=2
_CienaCesOspfRFC1583Comp_Type.__name__=_C
_CienaCesOspfRFC1583Comp_Object=MibScalar
cienaCesOspfRFC1583Comp=_CienaCesOspfRFC1583Comp_Object((1,3,6,1,4,1,1271,2,1,19,1,1,1),_CienaCesOspfRFC1583Comp_Type())
cienaCesOspfRFC1583Comp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfRFC1583Comp.setStatus(_A)
_CienaCesOspfOperStatus_Type=OspfOperStatus
_CienaCesOspfOperStatus_Object=MibScalar
cienaCesOspfOperStatus=_CienaCesOspfOperStatus_Object((1,3,6,1,4,1,1271,2,1,19,1,1,2),_CienaCesOspfOperStatus_Type())
cienaCesOspfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfOperStatus.setStatus(_A)
class _CienaCesOspfOpaqueLsaSupport_Type(TruthValue):defaultValue=1
_CienaCesOspfOpaqueLsaSupport_Type.__name__=_C
_CienaCesOspfOpaqueLsaSupport_Object=MibScalar
cienaCesOspfOpaqueLsaSupport=_CienaCesOspfOpaqueLsaSupport_Object((1,3,6,1,4,1,1271,2,1,19,1,1,3),_CienaCesOspfOpaqueLsaSupport_Type())
cienaCesOspfOpaqueLsaSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfOpaqueLsaSupport.setStatus(_A)
class _CienaCesOspfTrafficEngSupport_Type(TruthValue):defaultValue=1
_CienaCesOspfTrafficEngSupport_Type.__name__=_C
_CienaCesOspfTrafficEngSupport_Object=MibScalar
cienaCesOspfTrafficEngSupport=_CienaCesOspfTrafficEngSupport_Object((1,3,6,1,4,1,1271,2,1,19,1,1,4),_CienaCesOspfTrafficEngSupport_Type())
cienaCesOspfTrafficEngSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfTrafficEngSupport.setStatus(_A)
_CienaCesOspfExtOpLsaCount_Type=Gauge32
_CienaCesOspfExtOpLsaCount_Object=MibScalar
cienaCesOspfExtOpLsaCount=_CienaCesOspfExtOpLsaCount_Object((1,3,6,1,4,1,1271,2,1,19,1,1,5),_CienaCesOspfExtOpLsaCount_Type())
cienaCesOspfExtOpLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfExtOpLsaCount.setStatus(_A)
_CienaCesOspfExtOpLsaCksumSum_Type=Integer32
_CienaCesOspfExtOpLsaCksumSum_Object=MibScalar
cienaCesOspfExtOpLsaCksumSum=_CienaCesOspfExtOpLsaCksumSum_Object((1,3,6,1,4,1,1271,2,1,19,1,1,6),_CienaCesOspfExtOpLsaCksumSum_Type())
cienaCesOspfExtOpLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfExtOpLsaCksumSum.setStatus(_A)
_CienaCesOspfNumUpdPending_Type=Unsigned32
_CienaCesOspfNumUpdPending_Object=MibScalar
cienaCesOspfNumUpdPending=_CienaCesOspfNumUpdPending_Object((1,3,6,1,4,1,1271,2,1,19,1,1,7),_CienaCesOspfNumUpdPending_Type())
cienaCesOspfNumUpdPending.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfNumUpdPending.setStatus(_A)
_CienaCesOspfNumUpdMerged_Type=Unsigned32
_CienaCesOspfNumUpdMerged_Object=MibScalar
cienaCesOspfNumUpdMerged=_CienaCesOspfNumUpdMerged_Object((1,3,6,1,4,1,1271,2,1,19,1,1,8),_CienaCesOspfNumUpdMerged_Type())
cienaCesOspfNumUpdMerged.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfNumUpdMerged.setStatus(_A)
_CienaCesOspfNumCksumsPending_Type=Unsigned32
_CienaCesOspfNumCksumsPending_Object=MibScalar
cienaCesOspfNumCksumsPending=_CienaCesOspfNumCksumsPending_Object((1,3,6,1,4,1,1271,2,1,19,1,1,9),_CienaCesOspfNumCksumsPending_Type())
cienaCesOspfNumCksumsPending.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfNumCksumsPending.setStatus(_A)
class _CienaCesOspfCalcMaxDelay_Type(Unsigned32):defaultValue=5000
_CienaCesOspfCalcMaxDelay_Type.__name__=_G
_CienaCesOspfCalcMaxDelay_Object=MibScalar
cienaCesOspfCalcMaxDelay=_CienaCesOspfCalcMaxDelay_Object((1,3,6,1,4,1,1271,2,1,19,1,1,10),_CienaCesOspfCalcMaxDelay_Type())
cienaCesOspfCalcMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfCalcMaxDelay.setStatus(_A)
if mibBuilder.loadTexts:cienaCesOspfCalcMaxDelay.setUnits(_H)
_CienaCesOspfRouterId_Type=IpAddress
_CienaCesOspfRouterId_Object=MibScalar
cienaCesOspfRouterId=_CienaCesOspfRouterId_Object((1,3,6,1,4,1,1271,2,1,19,1,1,11),_CienaCesOspfRouterId_Type())
cienaCesOspfRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfRouterId.setStatus(_A)
_CienaCesOspf_ObjectIdentity=ObjectIdentity
cienaCesOspf=_CienaCesOspf_ObjectIdentity((1,3,6,1,4,1,1271,2,1,19,1,2))
_CienaCesOspfAreaTable_Object=MibTable
cienaCesOspfAreaTable=_CienaCesOspfAreaTable_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1))
if mibBuilder.loadTexts:cienaCesOspfAreaTable.setStatus(_A)
_CienaCesOspfAreaEntry_Object=MibTableRow
cienaCesOspfAreaEntry=_CienaCesOspfAreaEntry_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1))
cienaCesOspfAreaEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:cienaCesOspfAreaEntry.setStatus(_A)
_CienaCesOspfAreaId_Type=AreaID
_CienaCesOspfAreaId_Object=MibTableColumn
cienaCesOspfAreaId=_CienaCesOspfAreaId_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,1),_CienaCesOspfAreaId_Type())
cienaCesOspfAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesOspfAreaId.setStatus(_A)
class _CienaCesOspfAreaTransitCapability_Type(TruthValue):defaultValue=2
_CienaCesOspfAreaTransitCapability_Type.__name__=_C
_CienaCesOspfAreaTransitCapability_Object=MibTableColumn
cienaCesOspfAreaTransitCapability=_CienaCesOspfAreaTransitCapability_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,2),_CienaCesOspfAreaTransitCapability_Type())
cienaCesOspfAreaTransitCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaTransitCapability.setStatus(_A)
_CienaCesOspfAreaRtrLsaCount_Type=Gauge32
_CienaCesOspfAreaRtrLsaCount_Object=MibTableColumn
cienaCesOspfAreaRtrLsaCount=_CienaCesOspfAreaRtrLsaCount_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,3),_CienaCesOspfAreaRtrLsaCount_Type())
cienaCesOspfAreaRtrLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaRtrLsaCount.setStatus(_A)
_CienaCesOspfAreaRtrLsaCksumSum_Type=Integer32
_CienaCesOspfAreaRtrLsaCksumSum_Object=MibTableColumn
cienaCesOspfAreaRtrLsaCksumSum=_CienaCesOspfAreaRtrLsaCksumSum_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,4),_CienaCesOspfAreaRtrLsaCksumSum_Type())
cienaCesOspfAreaRtrLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaRtrLsaCksumSum.setStatus(_A)
_CienaCesOspfAreaNetLsaCount_Type=Gauge32
_CienaCesOspfAreaNetLsaCount_Object=MibTableColumn
cienaCesOspfAreaNetLsaCount=_CienaCesOspfAreaNetLsaCount_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,5),_CienaCesOspfAreaNetLsaCount_Type())
cienaCesOspfAreaNetLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaNetLsaCount.setStatus(_A)
_CienaCesOspfAreaNetLsaCksumSum_Type=Integer32
_CienaCesOspfAreaNetLsaCksumSum_Object=MibTableColumn
cienaCesOspfAreaNetLsaCksumSum=_CienaCesOspfAreaNetLsaCksumSum_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,6),_CienaCesOspfAreaNetLsaCksumSum_Type())
cienaCesOspfAreaNetLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaNetLsaCksumSum.setStatus(_A)
_CienaCesOspfAreaSummLsaCount_Type=Gauge32
_CienaCesOspfAreaSummLsaCount_Object=MibTableColumn
cienaCesOspfAreaSummLsaCount=_CienaCesOspfAreaSummLsaCount_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,7),_CienaCesOspfAreaSummLsaCount_Type())
cienaCesOspfAreaSummLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaSummLsaCount.setStatus(_A)
_CienaCesOspfAreaSummLsaCksumSum_Type=Integer32
_CienaCesOspfAreaSummLsaCksumSum_Object=MibTableColumn
cienaCesOspfAreaSummLsaCksumSum=_CienaCesOspfAreaSummLsaCksumSum_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,8),_CienaCesOspfAreaSummLsaCksumSum_Type())
cienaCesOspfAreaSummLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaSummLsaCksumSum.setStatus(_A)
_CienaCesOspfAreaSummAsLsaCount_Type=Gauge32
_CienaCesOspfAreaSummAsLsaCount_Object=MibTableColumn
cienaCesOspfAreaSummAsLsaCount=_CienaCesOspfAreaSummAsLsaCount_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,9),_CienaCesOspfAreaSummAsLsaCount_Type())
cienaCesOspfAreaSummAsLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaSummAsLsaCount.setStatus(_A)
_CienaCesOspfAreaSummAsLsaCksumSum_Type=Integer32
_CienaCesOspfAreaSummAsLsaCksumSum_Object=MibTableColumn
cienaCesOspfAreaSummAsLsaCksumSum=_CienaCesOspfAreaSummAsLsaCksumSum_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,10),_CienaCesOspfAreaSummAsLsaCksumSum_Type())
cienaCesOspfAreaSummAsLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaSummAsLsaCksumSum.setStatus(_A)
_CienaCesOspfAreaNssaLsaCount_Type=Gauge32
_CienaCesOspfAreaNssaLsaCount_Object=MibTableColumn
cienaCesOspfAreaNssaLsaCount=_CienaCesOspfAreaNssaLsaCount_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,11),_CienaCesOspfAreaNssaLsaCount_Type())
cienaCesOspfAreaNssaLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaNssaLsaCount.setStatus(_A)
_CienaCesOspfAreaNssaLsaCksumSum_Type=Integer32
_CienaCesOspfAreaNssaLsaCksumSum_Object=MibTableColumn
cienaCesOspfAreaNssaLsaCksumSum=_CienaCesOspfAreaNssaLsaCksumSum_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,12),_CienaCesOspfAreaNssaLsaCksumSum_Type())
cienaCesOspfAreaNssaLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaNssaLsaCksumSum.setStatus(_A)
_CienaCesOspfAreaOpLsaCount_Type=Gauge32
_CienaCesOspfAreaOpLsaCount_Object=MibTableColumn
cienaCesOspfAreaOpLsaCount=_CienaCesOspfAreaOpLsaCount_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,13),_CienaCesOspfAreaOpLsaCount_Type())
cienaCesOspfAreaOpLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaOpLsaCount.setStatus(_A)
_CienaCesOspfAreaOpLsaCksumSum_Type=Integer32
_CienaCesOspfAreaOpLsaCksumSum_Object=MibTableColumn
cienaCesOspfAreaOpLsaCksumSum=_CienaCesOspfAreaOpLsaCksumSum_Object((1,3,6,1,4,1,1271,2,1,19,1,2,1,1,14),_CienaCesOspfAreaOpLsaCksumSum_Type())
cienaCesOspfAreaOpLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfAreaOpLsaCksumSum.setStatus(_A)
_CienaCesOspfIfTable_Object=MibTable
cienaCesOspfIfTable=_CienaCesOspfIfTable_Object((1,3,6,1,4,1,1271,2,1,19,1,2,2))
if mibBuilder.loadTexts:cienaCesOspfIfTable.setStatus(_A)
_CienaCesOspfIfEntry_Object=MibTableRow
cienaCesOspfIfEntry=_CienaCesOspfIfEntry_Object((1,3,6,1,4,1,1271,2,1,19,1,2,2,1))
cienaCesOspfIfEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:cienaCesOspfIfEntry.setStatus(_A)
_CienaCesOspfIfIpAddress_Type=IpAddress
_CienaCesOspfIfIpAddress_Object=MibTableColumn
cienaCesOspfIfIpAddress=_CienaCesOspfIfIpAddress_Object((1,3,6,1,4,1,1271,2,1,19,1,2,2,1,1),_CienaCesOspfIfIpAddress_Type())
cienaCesOspfIfIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesOspfIfIpAddress.setStatus(_A)
class _CienaCesOspfAddressLessIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CienaCesOspfAddressLessIf_Type.__name__=_E
_CienaCesOspfAddressLessIf_Object=MibTableColumn
cienaCesOspfAddressLessIf=_CienaCesOspfAddressLessIf_Object((1,3,6,1,4,1,1271,2,1,19,1,2,2,1,2),_CienaCesOspfAddressLessIf_Type())
cienaCesOspfAddressLessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesOspfAddressLessIf.setStatus(_A)
_CienaCesOspfIfLsaCount_Type=Gauge32
_CienaCesOspfIfLsaCount_Object=MibTableColumn
cienaCesOspfIfLsaCount=_CienaCesOspfIfLsaCount_Object((1,3,6,1,4,1,1271,2,1,19,1,2,2,1,3),_CienaCesOspfIfLsaCount_Type())
cienaCesOspfIfLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfIfLsaCount.setStatus(_A)
_CienaCesOspfIfLsaCksumSum_Type=Integer32
_CienaCesOspfIfLsaCksumSum_Object=MibTableColumn
cienaCesOspfIfLsaCksumSum=_CienaCesOspfIfLsaCksumSum_Object((1,3,6,1,4,1,1271,2,1,19,1,2,2,1,4),_CienaCesOspfIfLsaCksumSum_Type())
cienaCesOspfIfLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfIfLsaCksumSum.setStatus(_A)
_CienaCesOspfIfOperStatus_Type=OspfOperStatus
_CienaCesOspfIfOperStatus_Object=MibTableColumn
cienaCesOspfIfOperStatus=_CienaCesOspfIfOperStatus_Object((1,3,6,1,4,1,1271,2,1,19,1,2,2,1,5),_CienaCesOspfIfOperStatus_Type())
cienaCesOspfIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfIfOperStatus.setStatus(_A)
_CienaCesOspfIfNetMask_Type=IpAddress
_CienaCesOspfIfNetMask_Object=MibTableColumn
cienaCesOspfIfNetMask=_CienaCesOspfIfNetMask_Object((1,3,6,1,4,1,1271,2,1,19,1,2,2,1,6),_CienaCesOspfIfNetMask_Type())
cienaCesOspfIfNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfIfNetMask.setStatus(_A)
class _CienaCesOspfIfTransmitTimerDelay_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,429496799))
_CienaCesOspfIfTransmitTimerDelay_Type.__name__=_E
_CienaCesOspfIfTransmitTimerDelay_Object=MibTableColumn
cienaCesOspfIfTransmitTimerDelay=_CienaCesOspfIfTransmitTimerDelay_Object((1,3,6,1,4,1,1271,2,1,19,1,2,2,1,7),_CienaCesOspfIfTransmitTimerDelay_Type())
cienaCesOspfIfTransmitTimerDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesOspfIfTransmitTimerDelay.setStatus(_A)
if mibBuilder.loadTexts:cienaCesOspfIfTransmitTimerDelay.setUnits(_H)
mibBuilder.exportSymbols(_D,**{'OspfOperStatus':OspfOperStatus,'cienaCesOspfMIB':cienaCesOspfMIB,'cienaCesOspfMIBObjects':cienaCesOspfMIBObjects,'cienaCesOspfGeneralGroup':cienaCesOspfGeneralGroup,'cienaCesOspfRFC1583Comp':cienaCesOspfRFC1583Comp,'cienaCesOspfOperStatus':cienaCesOspfOperStatus,'cienaCesOspfOpaqueLsaSupport':cienaCesOspfOpaqueLsaSupport,'cienaCesOspfTrafficEngSupport':cienaCesOspfTrafficEngSupport,'cienaCesOspfExtOpLsaCount':cienaCesOspfExtOpLsaCount,'cienaCesOspfExtOpLsaCksumSum':cienaCesOspfExtOpLsaCksumSum,'cienaCesOspfNumUpdPending':cienaCesOspfNumUpdPending,'cienaCesOspfNumUpdMerged':cienaCesOspfNumUpdMerged,'cienaCesOspfNumCksumsPending':cienaCesOspfNumCksumsPending,'cienaCesOspfCalcMaxDelay':cienaCesOspfCalcMaxDelay,'cienaCesOspfRouterId':cienaCesOspfRouterId,'cienaCesOspf':cienaCesOspf,'cienaCesOspfAreaTable':cienaCesOspfAreaTable,'cienaCesOspfAreaEntry':cienaCesOspfAreaEntry,_I:cienaCesOspfAreaId,'cienaCesOspfAreaTransitCapability':cienaCesOspfAreaTransitCapability,'cienaCesOspfAreaRtrLsaCount':cienaCesOspfAreaRtrLsaCount,'cienaCesOspfAreaRtrLsaCksumSum':cienaCesOspfAreaRtrLsaCksumSum,'cienaCesOspfAreaNetLsaCount':cienaCesOspfAreaNetLsaCount,'cienaCesOspfAreaNetLsaCksumSum':cienaCesOspfAreaNetLsaCksumSum,'cienaCesOspfAreaSummLsaCount':cienaCesOspfAreaSummLsaCount,'cienaCesOspfAreaSummLsaCksumSum':cienaCesOspfAreaSummLsaCksumSum,'cienaCesOspfAreaSummAsLsaCount':cienaCesOspfAreaSummAsLsaCount,'cienaCesOspfAreaSummAsLsaCksumSum':cienaCesOspfAreaSummAsLsaCksumSum,'cienaCesOspfAreaNssaLsaCount':cienaCesOspfAreaNssaLsaCount,'cienaCesOspfAreaNssaLsaCksumSum':cienaCesOspfAreaNssaLsaCksumSum,'cienaCesOspfAreaOpLsaCount':cienaCesOspfAreaOpLsaCount,'cienaCesOspfAreaOpLsaCksumSum':cienaCesOspfAreaOpLsaCksumSum,'cienaCesOspfIfTable':cienaCesOspfIfTable,'cienaCesOspfIfEntry':cienaCesOspfIfEntry,_J:cienaCesOspfIfIpAddress,_K:cienaCesOspfAddressLessIf,'cienaCesOspfIfLsaCount':cienaCesOspfIfLsaCount,'cienaCesOspfIfLsaCksumSum':cienaCesOspfIfLsaCksumSum,'cienaCesOspfIfOperStatus':cienaCesOspfIfOperStatus,'cienaCesOspfIfNetMask':cienaCesOspfIfNetMask,'cienaCesOspfIfTransmitTimerDelay':cienaCesOspfIfTransmitTimerDelay})