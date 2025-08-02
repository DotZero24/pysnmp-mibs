_T='aristaIfAdditionalInformationGroup'
_S='aristaIfDot1xMbaHostDrops'
_R='aristaIfDot1xEapolHostDrops'
_Q='aristaIfDot1xEapolPortDrops'
_P='aristaIfErrDisabledReason'
_O='aristaIfInAclDrops'
_N='aristaIfOperStatusChanges'
_M='aristaIfRatesLastUpdated'
_L='aristaIfOutOctetRate'
_K='aristaIfInOctetRate'
_J='aristaIfOutPktRate'
_I='aristaIfInPktRate'
_H='aristaIfRateInterval'
_G='aristaIfCounterLastUpdated'
_F='DisplayString'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='ARISTA-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
aristaIfMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,15))
if mibBuilder.loadTexts:aristaIfMIB.setRevisions(('2021-03-10 00:00','2021-01-21 00:00','2014-10-09 00:00'))
_AristaIf_ObjectIdentity=ObjectIdentity
aristaIf=_AristaIf_ObjectIdentity((1,3,6,1,4,1,30065,3,15,1))
_AristaIfTable_Object=MibTable
aristaIfTable=_AristaIfTable_Object((1,3,6,1,4,1,30065,3,15,1,1))
if mibBuilder.loadTexts:aristaIfTable.setStatus(_A)
_AristaIfEntry_Object=MibTableRow
aristaIfEntry=_AristaIfEntry_Object((1,3,6,1,4,1,30065,3,15,1,1,1))
aristaIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:aristaIfEntry.setStatus(_A)
_AristaIfCounterLastUpdated_Type=TimeTicks
_AristaIfCounterLastUpdated_Object=MibTableColumn
aristaIfCounterLastUpdated=_AristaIfCounterLastUpdated_Object((1,3,6,1,4,1,30065,3,15,1,1,1,1),_AristaIfCounterLastUpdated_Type())
aristaIfCounterLastUpdated.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfCounterLastUpdated.setStatus(_A)
_AristaIfRateInterval_Type=TimeTicks
_AristaIfRateInterval_Object=MibTableColumn
aristaIfRateInterval=_AristaIfRateInterval_Object((1,3,6,1,4,1,30065,3,15,1,1,1,2),_AristaIfRateInterval_Type())
aristaIfRateInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfRateInterval.setStatus(_A)
_AristaIfInPktRate_Type=Gauge32
_AristaIfInPktRate_Object=MibTableColumn
aristaIfInPktRate=_AristaIfInPktRate_Object((1,3,6,1,4,1,30065,3,15,1,1,1,3),_AristaIfInPktRate_Type())
aristaIfInPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfInPktRate.setStatus(_A)
_AristaIfOutPktRate_Type=Gauge32
_AristaIfOutPktRate_Object=MibTableColumn
aristaIfOutPktRate=_AristaIfOutPktRate_Object((1,3,6,1,4,1,30065,3,15,1,1,1,4),_AristaIfOutPktRate_Type())
aristaIfOutPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfOutPktRate.setStatus(_A)
_AristaIfInOctetRate_Type=CounterBasedGauge64
_AristaIfInOctetRate_Object=MibTableColumn
aristaIfInOctetRate=_AristaIfInOctetRate_Object((1,3,6,1,4,1,30065,3,15,1,1,1,5),_AristaIfInOctetRate_Type())
aristaIfInOctetRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfInOctetRate.setStatus(_A)
_AristaIfOutOctetRate_Type=CounterBasedGauge64
_AristaIfOutOctetRate_Object=MibTableColumn
aristaIfOutOctetRate=_AristaIfOutOctetRate_Object((1,3,6,1,4,1,30065,3,15,1,1,1,6),_AristaIfOutOctetRate_Type())
aristaIfOutOctetRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfOutOctetRate.setStatus(_A)
_AristaIfRatesLastUpdated_Type=TimeTicks
_AristaIfRatesLastUpdated_Object=MibTableColumn
aristaIfRatesLastUpdated=_AristaIfRatesLastUpdated_Object((1,3,6,1,4,1,30065,3,15,1,1,1,7),_AristaIfRatesLastUpdated_Type())
aristaIfRatesLastUpdated.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfRatesLastUpdated.setStatus(_A)
_AristaIfOperStatusChanges_Type=Counter32
_AristaIfOperStatusChanges_Object=MibTableColumn
aristaIfOperStatusChanges=_AristaIfOperStatusChanges_Object((1,3,6,1,4,1,30065,3,15,1,1,1,8),_AristaIfOperStatusChanges_Type())
aristaIfOperStatusChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfOperStatusChanges.setStatus(_A)
_AristaIfInAclDrops_Type=Counter32
_AristaIfInAclDrops_Object=MibTableColumn
aristaIfInAclDrops=_AristaIfInAclDrops_Object((1,3,6,1,4,1,30065,3,15,1,1,1,9),_AristaIfInAclDrops_Type())
aristaIfInAclDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfInAclDrops.setStatus(_A)
class _AristaIfErrDisabledReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AristaIfErrDisabledReason_Type.__name__=_F
_AristaIfErrDisabledReason_Object=MibTableColumn
aristaIfErrDisabledReason=_AristaIfErrDisabledReason_Object((1,3,6,1,4,1,30065,3,15,1,1,1,10),_AristaIfErrDisabledReason_Type())
aristaIfErrDisabledReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfErrDisabledReason.setStatus(_A)
_AristaIfDot1xEapolPortDrops_Type=Counter32
_AristaIfDot1xEapolPortDrops_Object=MibTableColumn
aristaIfDot1xEapolPortDrops=_AristaIfDot1xEapolPortDrops_Object((1,3,6,1,4,1,30065,3,15,1,1,1,11),_AristaIfDot1xEapolPortDrops_Type())
aristaIfDot1xEapolPortDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfDot1xEapolPortDrops.setStatus(_A)
_AristaIfDot1xEapolHostDrops_Type=Counter32
_AristaIfDot1xEapolHostDrops_Object=MibTableColumn
aristaIfDot1xEapolHostDrops=_AristaIfDot1xEapolHostDrops_Object((1,3,6,1,4,1,30065,3,15,1,1,1,12),_AristaIfDot1xEapolHostDrops_Type())
aristaIfDot1xEapolHostDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfDot1xEapolHostDrops.setStatus(_A)
_AristaIfDot1xMbaHostDrops_Type=Counter32
_AristaIfDot1xMbaHostDrops_Object=MibTableColumn
aristaIfDot1xMbaHostDrops=_AristaIfDot1xMbaHostDrops_Object((1,3,6,1,4,1,30065,3,15,1,1,1,13),_AristaIfDot1xMbaHostDrops_Type())
aristaIfDot1xMbaHostDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIfDot1xMbaHostDrops.setStatus(_A)
_AristaIfConformance_ObjectIdentity=ObjectIdentity
aristaIfConformance=_AristaIfConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,15,2))
_AristaIfGroups_ObjectIdentity=ObjectIdentity
aristaIfGroups=_AristaIfGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,15,2,1))
_AristaIfCompliances_ObjectIdentity=ObjectIdentity
aristaIfCompliances=_AristaIfCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,15,2,2))
aristaIfAdditionalInformationGroup=ObjectGroup((1,3,6,1,4,1,30065,3,15,2,1,1))
aristaIfAdditionalInformationGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:aristaIfAdditionalInformationGroup.setStatus(_A)
aristaIfCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,15,2,2,1))
aristaIfCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:aristaIfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aristaIfMIB':aristaIfMIB,'aristaIf':aristaIf,'aristaIfTable':aristaIfTable,'aristaIfEntry':aristaIfEntry,_G:aristaIfCounterLastUpdated,_H:aristaIfRateInterval,_I:aristaIfInPktRate,_J:aristaIfOutPktRate,_K:aristaIfInOctetRate,_L:aristaIfOutOctetRate,_M:aristaIfRatesLastUpdated,_N:aristaIfOperStatusChanges,_O:aristaIfInAclDrops,_P:aristaIfErrDisabledReason,_Q:aristaIfDot1xEapolPortDrops,_R:aristaIfDot1xEapolHostDrops,_S:aristaIfDot1xMbaHostDrops,'aristaIfConformance':aristaIfConformance,'aristaIfGroups':aristaIfGroups,_T:aristaIfAdditionalInformationGroup,'aristaIfCompliances':aristaIfCompliances,'aristaIfCompliance':aristaIfCompliance})