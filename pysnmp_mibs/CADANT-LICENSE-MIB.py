_K='cerCardDataLicenseType'
_J='cerCardDataLicenseSlot'
_I='cadChassisLicenseStatusType'
_H='cadLicenseIndex'
_G='OctetString'
_F='read-create'
_E='not-accessible'
_D='Unsigned32'
_C='CADANT-LICENSE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cadLicense,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadLicense')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
cadLicenseMib=ModuleIdentity((1,3,6,1,4,1,4998,1,1,135,1))
if mibBuilder.loadTexts:cadLicenseMib.setRevisions(('2015-06-17 00:00','2015-06-09 00:00','2014-08-20 00:00','2014-08-14 00:00','2014-07-17 00:00','2014-07-10 00:00','2014-06-25 00:00'))
class CadChassisLicenseIndexType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('reserved',1),('videoNarrowcastB',2),('videoReplicaNarrowcastB',3),('videoBroadcastB',4),('videoReplicaBroadcastB',5),('videoNarrowcastA',6),('videoReplicaNarrowcastA',7),('videoBroadcastA',8),('videoReplicaBroadcastA',9),('docsisUpstream30',10),('docsisDownstream30B',11),('docsisDownstream30A',12),('docsisDownstreamOfdm',13),('docsisUpstreamOfdma',14)))
_CadChassisLicenseTable_Object=MibTable
cadChassisLicenseTable=_CadChassisLicenseTable_Object((1,3,6,1,4,1,4998,1,1,135,1,1))
if mibBuilder.loadTexts:cadChassisLicenseTable.setStatus(_A)
_CadChassisLicenseEntry_Object=MibTableRow
cadChassisLicenseEntry=_CadChassisLicenseEntry_Object((1,3,6,1,4,1,4998,1,1,135,1,1,1))
cadChassisLicenseEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cadChassisLicenseEntry.setStatus(_A)
_CadLicenseIndex_Type=CadChassisLicenseIndexType
_CadLicenseIndex_Object=MibTableColumn
cadLicenseIndex=_CadLicenseIndex_Object((1,3,6,1,4,1,4998,1,1,135,1,1,1,1),_CadLicenseIndex_Type())
cadLicenseIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cadLicenseIndex.setStatus(_A)
class _CadLicenseKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_CadLicenseKey_Type.__name__=_G
_CadLicenseKey_Object=MibTableColumn
cadLicenseKey=_CadLicenseKey_Object((1,3,6,1,4,1,4998,1,1,135,1,1,1,2),_CadLicenseKey_Type())
cadLicenseKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cadLicenseKey.setStatus(_A)
class _CadLicenseChannelCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500000))
_CadLicenseChannelCount_Type.__name__=_D
_CadLicenseChannelCount_Object=MibTableColumn
cadLicenseChannelCount=_CadLicenseChannelCount_Object((1,3,6,1,4,1,4998,1,1,135,1,1,1,3),_CadLicenseChannelCount_Type())
cadLicenseChannelCount.setMaxAccess(_F)
if mibBuilder.loadTexts:cadLicenseChannelCount.setStatus(_A)
class _CadLicenseSpareChannelCount_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250000))
_CadLicenseSpareChannelCount_Type.__name__=_D
_CadLicenseSpareChannelCount_Object=MibTableColumn
cadLicenseSpareChannelCount=_CadLicenseSpareChannelCount_Object((1,3,6,1,4,1,4998,1,1,135,1,1,1,4),_CadLicenseSpareChannelCount_Type())
cadLicenseSpareChannelCount.setMaxAccess(_F)
if mibBuilder.loadTexts:cadLicenseSpareChannelCount.setStatus(_A)
_CadLicenseRowStatus_Type=RowStatus
_CadLicenseRowStatus_Object=MibTableColumn
cadLicenseRowStatus=_CadLicenseRowStatus_Object((1,3,6,1,4,1,4998,1,1,135,1,1,1,5),_CadLicenseRowStatus_Type())
cadLicenseRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cadLicenseRowStatus.setStatus(_A)
_CadChassisLicenseStatusTable_Object=MibTable
cadChassisLicenseStatusTable=_CadChassisLicenseStatusTable_Object((1,3,6,1,4,1,4998,1,1,135,1,2))
if mibBuilder.loadTexts:cadChassisLicenseStatusTable.setStatus(_A)
_CadChassisLicenseStatusEntry_Object=MibTableRow
cadChassisLicenseStatusEntry=_CadChassisLicenseStatusEntry_Object((1,3,6,1,4,1,4998,1,1,135,1,2,1))
cadChassisLicenseStatusEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cadChassisLicenseStatusEntry.setStatus(_A)
_CadChassisLicenseStatusType_Type=CadChassisLicenseIndexType
_CadChassisLicenseStatusType_Object=MibTableColumn
cadChassisLicenseStatusType=_CadChassisLicenseStatusType_Object((1,3,6,1,4,1,4998,1,1,135,1,2,1,1),_CadChassisLicenseStatusType_Type())
cadChassisLicenseStatusType.setMaxAccess(_E)
if mibBuilder.loadTexts:cadChassisLicenseStatusType.setStatus(_A)
_CadChassisLicensesUsed_Type=Unsigned32
_CadChassisLicensesUsed_Object=MibTableColumn
cadChassisLicensesUsed=_CadChassisLicensesUsed_Object((1,3,6,1,4,1,4998,1,1,135,1,2,1,2),_CadChassisLicensesUsed_Type())
cadChassisLicensesUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:cadChassisLicensesUsed.setStatus(_A)
_CadChassisLicensesRequested_Type=Unsigned32
_CadChassisLicensesRequested_Object=MibTableColumn
cadChassisLicensesRequested=_CadChassisLicensesRequested_Object((1,3,6,1,4,1,4998,1,1,135,1,2,1,3),_CadChassisLicensesRequested_Type())
cadChassisLicensesRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:cadChassisLicensesRequested.setStatus(_A)
_CadChassisLicensesApplied_Type=Unsigned32
_CadChassisLicensesApplied_Object=MibTableColumn
cadChassisLicensesApplied=_CadChassisLicensesApplied_Object((1,3,6,1,4,1,4998,1,1,135,1,2,1,4),_CadChassisLicensesApplied_Type())
cadChassisLicensesApplied.setMaxAccess(_B)
if mibBuilder.loadTexts:cadChassisLicensesApplied.setStatus(_A)
_CadChassisLicensesValid_Type=TruthValue
_CadChassisLicensesValid_Object=MibTableColumn
cadChassisLicensesValid=_CadChassisLicensesValid_Object((1,3,6,1,4,1,4998,1,1,135,1,2,1,5),_CadChassisLicensesValid_Type())
cadChassisLicensesValid.setMaxAccess(_B)
if mibBuilder.loadTexts:cadChassisLicensesValid.setStatus(_A)
_CerCardDataLicenseStatusTable_Object=MibTable
cerCardDataLicenseStatusTable=_CerCardDataLicenseStatusTable_Object((1,3,6,1,4,1,4998,1,1,135,1,3))
if mibBuilder.loadTexts:cerCardDataLicenseStatusTable.setStatus(_A)
_CerCardDataLicenseStatusEntry_Object=MibTableRow
cerCardDataLicenseStatusEntry=_CerCardDataLicenseStatusEntry_Object((1,3,6,1,4,1,4998,1,1,135,1,3,1))
cerCardDataLicenseStatusEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:cerCardDataLicenseStatusEntry.setStatus(_A)
class _CerCardDataLicenseSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6),ValueRangeConstraint(9,14))
_CerCardDataLicenseSlot_Type.__name__=_D
_CerCardDataLicenseSlot_Object=MibTableColumn
cerCardDataLicenseSlot=_CerCardDataLicenseSlot_Object((1,3,6,1,4,1,4998,1,1,135,1,3,1,1),_CerCardDataLicenseSlot_Type())
cerCardDataLicenseSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:cerCardDataLicenseSlot.setStatus(_A)
_CerCardDataLicenseType_Type=CadChassisLicenseIndexType
_CerCardDataLicenseType_Object=MibTableColumn
cerCardDataLicenseType=_CerCardDataLicenseType_Object((1,3,6,1,4,1,4998,1,1,135,1,3,1,2),_CerCardDataLicenseType_Type())
cerCardDataLicenseType.setMaxAccess(_E)
if mibBuilder.loadTexts:cerCardDataLicenseType.setStatus(_A)
_CerCardDataLicensesUsed_Type=Unsigned32
_CerCardDataLicensesUsed_Object=MibTableColumn
cerCardDataLicensesUsed=_CerCardDataLicensesUsed_Object((1,3,6,1,4,1,4998,1,1,135,1,3,1,3),_CerCardDataLicensesUsed_Type())
cerCardDataLicensesUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:cerCardDataLicensesUsed.setStatus(_A)
_CerCardDataLicensesRequested_Type=Unsigned32
_CerCardDataLicensesRequested_Object=MibTableColumn
cerCardDataLicensesRequested=_CerCardDataLicensesRequested_Object((1,3,6,1,4,1,4998,1,1,135,1,3,1,4),_CerCardDataLicensesRequested_Type())
cerCardDataLicensesRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:cerCardDataLicensesRequested.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'CadChassisLicenseIndexType':CadChassisLicenseIndexType,'cadLicenseMib':cadLicenseMib,'cadChassisLicenseTable':cadChassisLicenseTable,'cadChassisLicenseEntry':cadChassisLicenseEntry,_H:cadLicenseIndex,'cadLicenseKey':cadLicenseKey,'cadLicenseChannelCount':cadLicenseChannelCount,'cadLicenseSpareChannelCount':cadLicenseSpareChannelCount,'cadLicenseRowStatus':cadLicenseRowStatus,'cadChassisLicenseStatusTable':cadChassisLicenseStatusTable,'cadChassisLicenseStatusEntry':cadChassisLicenseStatusEntry,_I:cadChassisLicenseStatusType,'cadChassisLicensesUsed':cadChassisLicensesUsed,'cadChassisLicensesRequested':cadChassisLicensesRequested,'cadChassisLicensesApplied':cadChassisLicensesApplied,'cadChassisLicensesValid':cadChassisLicensesValid,'cerCardDataLicenseStatusTable':cerCardDataLicenseStatusTable,'cerCardDataLicenseStatusEntry':cerCardDataLicenseStatusEntry,_J:cerCardDataLicenseSlot,_K:cerCardDataLicenseType,'cerCardDataLicensesUsed':cerCardDataLicensesUsed,'cerCardDataLicensesRequested':cerCardDataLicensesRequested})