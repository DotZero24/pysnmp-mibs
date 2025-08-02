_G='aniBsuStatsBWServiceClass'
_F='BSUSTATS-MIB'
_E='Integer32'
_D='aniBsuWirelessPort'
_C='BSUWIRELESSIF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bsu,=mibBuilder.importSymbols('ANIROOT-MIB','bsu')
aniBsuWirelessPort,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
aniBsuStatistics=ModuleIdentity((1,3,6,1,4,1,4325,3,3))
_AniBsuStatsGrp_ObjectIdentity=ObjectIdentity
aniBsuStatsGrp=_AniBsuStatsGrp_ObjectIdentity((1,3,6,1,4,1,4325,3,3,1))
_AniBsuRfStatsTable_Object=MibTable
aniBsuRfStatsTable=_AniBsuRfStatsTable_Object((1,3,6,1,4,1,4325,3,3,2))
if mibBuilder.loadTexts:aniBsuRfStatsTable.setStatus(_A)
_AniBsuRfStatsEntry_Object=MibTableRow
aniBsuRfStatsEntry=_AniBsuRfStatsEntry_Object((1,3,6,1,4,1,4325,3,3,2,1))
aniBsuRfStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:aniBsuRfStatsEntry.setStatus(_A)
_AniBsuRfStatsInPackets_Type=Counter32
_AniBsuRfStatsInPackets_Object=MibTableColumn
aniBsuRfStatsInPackets=_AniBsuRfStatsInPackets_Object((1,3,6,1,4,1,4325,3,3,2,1,1),_AniBsuRfStatsInPackets_Type())
aniBsuRfStatsInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfStatsInPackets.setStatus(_A)
_AniBsuRfStatsOutPackets_Type=Counter32
_AniBsuRfStatsOutPackets_Object=MibTableColumn
aniBsuRfStatsOutPackets=_AniBsuRfStatsOutPackets_Object((1,3,6,1,4,1,4325,3,3,2,1,2),_AniBsuRfStatsOutPackets_Type())
aniBsuRfStatsOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfStatsOutPackets.setStatus(_A)
_AniBsuRfStatsInOctets_Type=Counter32
_AniBsuRfStatsInOctets_Object=MibTableColumn
aniBsuRfStatsInOctets=_AniBsuRfStatsInOctets_Object((1,3,6,1,4,1,4325,3,3,2,1,3),_AniBsuRfStatsInOctets_Type())
aniBsuRfStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfStatsInOctets.setStatus(_A)
_AniBsuRfStatsOutOctets_Type=Counter32
_AniBsuRfStatsOutOctets_Object=MibTableColumn
aniBsuRfStatsOutOctets=_AniBsuRfStatsOutOctets_Object((1,3,6,1,4,1,4325,3,3,2,1,4),_AniBsuRfStatsOutOctets_Type())
aniBsuRfStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfStatsOutOctets.setStatus(_A)
class _AniBsuRfStatsNumSusLinked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_AniBsuRfStatsNumSusLinked_Type.__name__=_E
_AniBsuRfStatsNumSusLinked_Object=MibTableColumn
aniBsuRfStatsNumSusLinked=_AniBsuRfStatsNumSusLinked_Object((1,3,6,1,4,1,4325,3,3,2,1,5),_AniBsuRfStatsNumSusLinked_Type())
aniBsuRfStatsNumSusLinked.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfStatsNumSusLinked.setStatus(_A)
_AniBsuStatsBWGroup_ObjectIdentity=ObjectIdentity
aniBsuStatsBWGroup=_AniBsuStatsBWGroup_ObjectIdentity((1,3,6,1,4,1,4325,3,3,3))
_AniBsuStatsBWTable_Object=MibTable
aniBsuStatsBWTable=_AniBsuStatsBWTable_Object((1,3,6,1,4,1,4325,3,3,3,1))
if mibBuilder.loadTexts:aniBsuStatsBWTable.setStatus(_A)
_AniBsuStatsBWEntry_Object=MibTableRow
aniBsuStatsBWEntry=_AniBsuStatsBWEntry_Object((1,3,6,1,4,1,4325,3,3,3,1,1))
aniBsuStatsBWEntry.setIndexNames((0,_C,_D),(0,_F,_G))
if mibBuilder.loadTexts:aniBsuStatsBWEntry.setStatus(_A)
class _AniBsuStatsBWServiceClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('besteffort',1),('cir',2),('cbr',3)))
_AniBsuStatsBWServiceClass_Type.__name__=_E
_AniBsuStatsBWServiceClass_Object=MibTableColumn
aniBsuStatsBWServiceClass=_AniBsuStatsBWServiceClass_Object((1,3,6,1,4,1,4325,3,3,3,1,1,1),_AniBsuStatsBWServiceClass_Type())
aniBsuStatsBWServiceClass.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatsBWServiceClass.setStatus(_A)
_AniBsuStatsBWUSMaxAllocation_Type=Counter32
_AniBsuStatsBWUSMaxAllocation_Object=MibTableColumn
aniBsuStatsBWUSMaxAllocation=_AniBsuStatsBWUSMaxAllocation_Object((1,3,6,1,4,1,4325,3,3,3,1,1,2),_AniBsuStatsBWUSMaxAllocation_Type())
aniBsuStatsBWUSMaxAllocation.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatsBWUSMaxAllocation.setStatus(_A)
_AniBsuStatsBWUSMaxAllocPercent_Type=Integer32
_AniBsuStatsBWUSMaxAllocPercent_Object=MibTableColumn
aniBsuStatsBWUSMaxAllocPercent=_AniBsuStatsBWUSMaxAllocPercent_Object((1,3,6,1,4,1,4325,3,3,3,1,1,3),_AniBsuStatsBWUSMaxAllocPercent_Type())
aniBsuStatsBWUSMaxAllocPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatsBWUSMaxAllocPercent.setStatus(_A)
_AniBsuStatsBWUSCurrAllocation_Type=Counter32
_AniBsuStatsBWUSCurrAllocation_Object=MibTableColumn
aniBsuStatsBWUSCurrAllocation=_AniBsuStatsBWUSCurrAllocation_Object((1,3,6,1,4,1,4325,3,3,3,1,1,4),_AniBsuStatsBWUSCurrAllocation_Type())
aniBsuStatsBWUSCurrAllocation.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatsBWUSCurrAllocation.setStatus(_A)
_AniBsuStatsBWUSSubscrPercent_Type=DisplayString
_AniBsuStatsBWUSSubscrPercent_Object=MibTableColumn
aniBsuStatsBWUSSubscrPercent=_AniBsuStatsBWUSSubscrPercent_Object((1,3,6,1,4,1,4325,3,3,3,1,1,5),_AniBsuStatsBWUSSubscrPercent_Type())
aniBsuStatsBWUSSubscrPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatsBWUSSubscrPercent.setStatus(_A)
_AniBsuStatsBWDSMaxAllocation_Type=Counter32
_AniBsuStatsBWDSMaxAllocation_Object=MibTableColumn
aniBsuStatsBWDSMaxAllocation=_AniBsuStatsBWDSMaxAllocation_Object((1,3,6,1,4,1,4325,3,3,3,1,1,6),_AniBsuStatsBWDSMaxAllocation_Type())
aniBsuStatsBWDSMaxAllocation.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatsBWDSMaxAllocation.setStatus(_A)
_AniBsuStatsBWDSMaxAllocPercent_Type=Integer32
_AniBsuStatsBWDSMaxAllocPercent_Object=MibTableColumn
aniBsuStatsBWDSMaxAllocPercent=_AniBsuStatsBWDSMaxAllocPercent_Object((1,3,6,1,4,1,4325,3,3,3,1,1,7),_AniBsuStatsBWDSMaxAllocPercent_Type())
aniBsuStatsBWDSMaxAllocPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatsBWDSMaxAllocPercent.setStatus(_A)
_AniBsuStatsBWDSCurrAllocation_Type=Counter32
_AniBsuStatsBWDSCurrAllocation_Object=MibTableColumn
aniBsuStatsBWDSCurrAllocation=_AniBsuStatsBWDSCurrAllocation_Object((1,3,6,1,4,1,4325,3,3,3,1,1,8),_AniBsuStatsBWDSCurrAllocation_Type())
aniBsuStatsBWDSCurrAllocation.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatsBWDSCurrAllocation.setStatus(_A)
_AniBsuStatsBWDSSubscrPercent_Type=DisplayString
_AniBsuStatsBWDSSubscrPercent_Object=MibTableColumn
aniBsuStatsBWDSSubscrPercent=_AniBsuStatsBWDSSubscrPercent_Object((1,3,6,1,4,1,4325,3,3,3,1,1,9),_AniBsuStatsBWDSSubscrPercent_Type())
aniBsuStatsBWDSSubscrPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatsBWDSSubscrPercent.setStatus(_A)
_AniBsuStatsBWTotalTable_Object=MibTable
aniBsuStatsBWTotalTable=_AniBsuStatsBWTotalTable_Object((1,3,6,1,4,1,4325,3,3,3,2))
if mibBuilder.loadTexts:aniBsuStatsBWTotalTable.setStatus(_A)
_AniBsuStatsBWTotalEntry_Object=MibTableRow
aniBsuStatsBWTotalEntry=_AniBsuStatsBWTotalEntry_Object((1,3,6,1,4,1,4325,3,3,3,2,1))
aniBsuStatsBWTotalEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:aniBsuStatsBWTotalEntry.setStatus(_A)
_AniBsuStatsBWTotalUSMaxAllocation_Type=Counter32
_AniBsuStatsBWTotalUSMaxAllocation_Object=MibTableColumn
aniBsuStatsBWTotalUSMaxAllocation=_AniBsuStatsBWTotalUSMaxAllocation_Object((1,3,6,1,4,1,4325,3,3,3,2,1,1),_AniBsuStatsBWTotalUSMaxAllocation_Type())
aniBsuStatsBWTotalUSMaxAllocation.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatsBWTotalUSMaxAllocation.setStatus(_A)
_AniBsuStatsBWTotalDSMaxAllocation_Type=Counter32
_AniBsuStatsBWTotalDSMaxAllocation_Object=MibTableColumn
aniBsuStatsBWTotalDSMaxAllocation=_AniBsuStatsBWTotalDSMaxAllocation_Object((1,3,6,1,4,1,4325,3,3,3,2,1,2),_AniBsuStatsBWTotalDSMaxAllocation_Type())
aniBsuStatsBWTotalDSMaxAllocation.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatsBWTotalDSMaxAllocation.setStatus(_A)
_AniBsuRfSigQStatsTable_Object=MibTable
aniBsuRfSigQStatsTable=_AniBsuRfSigQStatsTable_Object((1,3,6,1,4,1,4325,3,3,4))
if mibBuilder.loadTexts:aniBsuRfSigQStatsTable.setStatus(_A)
_AniBsuRfSigQStatsEntry_Object=MibTableRow
aniBsuRfSigQStatsEntry=_AniBsuRfSigQStatsEntry_Object((1,3,6,1,4,1,4325,3,3,4,1))
aniBsuRfSigQStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:aniBsuRfSigQStatsEntry.setStatus(_A)
_AniBsuRfSigQStatsNoFecErrorCount_Type=Counter32
_AniBsuRfSigQStatsNoFecErrorCount_Object=MibTableColumn
aniBsuRfSigQStatsNoFecErrorCount=_AniBsuRfSigQStatsNoFecErrorCount_Object((1,3,6,1,4,1,4325,3,3,4,1,1),_AniBsuRfSigQStatsNoFecErrorCount_Type())
aniBsuRfSigQStatsNoFecErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfSigQStatsNoFecErrorCount.setStatus(_A)
_AniBsuRfSigQStatsCorrFecErrorCount_Type=Counter32
_AniBsuRfSigQStatsCorrFecErrorCount_Object=MibTableColumn
aniBsuRfSigQStatsCorrFecErrorCount=_AniBsuRfSigQStatsCorrFecErrorCount_Object((1,3,6,1,4,1,4325,3,3,4,1,2),_AniBsuRfSigQStatsCorrFecErrorCount_Type())
aniBsuRfSigQStatsCorrFecErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfSigQStatsCorrFecErrorCount.setStatus(_A)
_AniBsuRfSigQStatsUncorrFecErrorCount_Type=Counter32
_AniBsuRfSigQStatsUncorrFecErrorCount_Object=MibTableColumn
aniBsuRfSigQStatsUncorrFecErrorCount=_AniBsuRfSigQStatsUncorrFecErrorCount_Object((1,3,6,1,4,1,4325,3,3,4,1,3),_AniBsuRfSigQStatsUncorrFecErrorCount_Type())
aniBsuRfSigQStatsUncorrFecErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfSigQStatsUncorrFecErrorCount.setStatus(_A)
_AniBsuRfSigQStatsNoUniqueWordCount_Type=Counter32
_AniBsuRfSigQStatsNoUniqueWordCount_Object=MibTableColumn
aniBsuRfSigQStatsNoUniqueWordCount=_AniBsuRfSigQStatsNoUniqueWordCount_Object((1,3,6,1,4,1,4325,3,3,4,1,4),_AniBsuRfSigQStatsNoUniqueWordCount_Type())
aniBsuRfSigQStatsNoUniqueWordCount.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfSigQStatsNoUniqueWordCount.setStatus(_A)
_AniBsuRfSigQStatsCollidedBurstCount_Type=Counter32
_AniBsuRfSigQStatsCollidedBurstCount_Object=MibTableColumn
aniBsuRfSigQStatsCollidedBurstCount=_AniBsuRfSigQStatsCollidedBurstCount_Object((1,3,6,1,4,1,4325,3,3,4,1,5),_AniBsuRfSigQStatsCollidedBurstCount_Type())
aniBsuRfSigQStatsCollidedBurstCount.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfSigQStatsCollidedBurstCount.setStatus(_A)
_AniBsuRfSigQStatsNoEnergyCount_Type=Counter32
_AniBsuRfSigQStatsNoEnergyCount_Object=MibTableColumn
aniBsuRfSigQStatsNoEnergyCount=_AniBsuRfSigQStatsNoEnergyCount_Object((1,3,6,1,4,1,4325,3,3,4,1,6),_AniBsuRfSigQStatsNoEnergyCount_Type())
aniBsuRfSigQStatsNoEnergyCount.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfSigQStatsNoEnergyCount.setStatus(_A)
_AniBsuRfSigQStatsPayloadLenErrorCount_Type=Counter32
_AniBsuRfSigQStatsPayloadLenErrorCount_Object=MibTableColumn
aniBsuRfSigQStatsPayloadLenErrorCount=_AniBsuRfSigQStatsPayloadLenErrorCount_Object((1,3,6,1,4,1,4325,3,3,4,1,7),_AniBsuRfSigQStatsPayloadLenErrorCount_Type())
aniBsuRfSigQStatsPayloadLenErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfSigQStatsPayloadLenErrorCount.setStatus(_A)
_AniBsuRfSigQStatsBurstErrorRate_Type=DisplayString
_AniBsuRfSigQStatsBurstErrorRate_Object=MibTableColumn
aniBsuRfSigQStatsBurstErrorRate=_AniBsuRfSigQStatsBurstErrorRate_Object((1,3,6,1,4,1,4325,3,3,4,1,8),_AniBsuRfSigQStatsBurstErrorRate_Type())
aniBsuRfSigQStatsBurstErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuRfSigQStatsBurstErrorRate.setStatus(_A)
_AniBsuRfSigQStatsResetCounter_Type=TruthValue
_AniBsuRfSigQStatsResetCounter_Object=MibTableColumn
aniBsuRfSigQStatsResetCounter=_AniBsuRfSigQStatsResetCounter_Object((1,3,6,1,4,1,4325,3,3,4,1,9),_AniBsuRfSigQStatsResetCounter_Type())
aniBsuRfSigQStatsResetCounter.setMaxAccess('read-write')
if mibBuilder.loadTexts:aniBsuRfSigQStatsResetCounter.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'aniBsuStatistics':aniBsuStatistics,'aniBsuStatsGrp':aniBsuStatsGrp,'aniBsuRfStatsTable':aniBsuRfStatsTable,'aniBsuRfStatsEntry':aniBsuRfStatsEntry,'aniBsuRfStatsInPackets':aniBsuRfStatsInPackets,'aniBsuRfStatsOutPackets':aniBsuRfStatsOutPackets,'aniBsuRfStatsInOctets':aniBsuRfStatsInOctets,'aniBsuRfStatsOutOctets':aniBsuRfStatsOutOctets,'aniBsuRfStatsNumSusLinked':aniBsuRfStatsNumSusLinked,'aniBsuStatsBWGroup':aniBsuStatsBWGroup,'aniBsuStatsBWTable':aniBsuStatsBWTable,'aniBsuStatsBWEntry':aniBsuStatsBWEntry,_G:aniBsuStatsBWServiceClass,'aniBsuStatsBWUSMaxAllocation':aniBsuStatsBWUSMaxAllocation,'aniBsuStatsBWUSMaxAllocPercent':aniBsuStatsBWUSMaxAllocPercent,'aniBsuStatsBWUSCurrAllocation':aniBsuStatsBWUSCurrAllocation,'aniBsuStatsBWUSSubscrPercent':aniBsuStatsBWUSSubscrPercent,'aniBsuStatsBWDSMaxAllocation':aniBsuStatsBWDSMaxAllocation,'aniBsuStatsBWDSMaxAllocPercent':aniBsuStatsBWDSMaxAllocPercent,'aniBsuStatsBWDSCurrAllocation':aniBsuStatsBWDSCurrAllocation,'aniBsuStatsBWDSSubscrPercent':aniBsuStatsBWDSSubscrPercent,'aniBsuStatsBWTotalTable':aniBsuStatsBWTotalTable,'aniBsuStatsBWTotalEntry':aniBsuStatsBWTotalEntry,'aniBsuStatsBWTotalUSMaxAllocation':aniBsuStatsBWTotalUSMaxAllocation,'aniBsuStatsBWTotalDSMaxAllocation':aniBsuStatsBWTotalDSMaxAllocation,'aniBsuRfSigQStatsTable':aniBsuRfSigQStatsTable,'aniBsuRfSigQStatsEntry':aniBsuRfSigQStatsEntry,'aniBsuRfSigQStatsNoFecErrorCount':aniBsuRfSigQStatsNoFecErrorCount,'aniBsuRfSigQStatsCorrFecErrorCount':aniBsuRfSigQStatsCorrFecErrorCount,'aniBsuRfSigQStatsUncorrFecErrorCount':aniBsuRfSigQStatsUncorrFecErrorCount,'aniBsuRfSigQStatsNoUniqueWordCount':aniBsuRfSigQStatsNoUniqueWordCount,'aniBsuRfSigQStatsCollidedBurstCount':aniBsuRfSigQStatsCollidedBurstCount,'aniBsuRfSigQStatsNoEnergyCount':aniBsuRfSigQStatsNoEnergyCount,'aniBsuRfSigQStatsPayloadLenErrorCount':aniBsuRfSigQStatsPayloadLenErrorCount,'aniBsuRfSigQStatsBurstErrorRate':aniBsuRfSigQStatsBurstErrorRate,'aniBsuRfSigQStatsResetCounter':aniBsuRfSigQStatsResetCounter})