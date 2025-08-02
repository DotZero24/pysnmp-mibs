_L='ethConfigStatus'
_K='ethTotalDayNumber'
_J='ethTotalIndex'
_I='ethIntervalNumber'
_H='ethIntervalIndex'
_G='ethCurrentIndex'
_F='ethLineIndex'
_E='read-write'
_D='SL-ETH-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slService,=mibBuilder.importSymbols('SL-NE-MIB','slService')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
slEthernet=ModuleIdentity((1,3,6,1,4,1,4515,1,1,1))
_EthConfigTable_Object=MibTable
ethConfigTable=_EthConfigTable_Object((1,3,6,1,4,1,4515,1,1,1,1))
if mibBuilder.loadTexts:ethConfigTable.setStatus(_A)
_EthConfigEntry_Object=MibTableRow
ethConfigEntry=_EthConfigEntry_Object((1,3,6,1,4,1,4515,1,1,1,1,1))
ethConfigEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:ethConfigEntry.setStatus(_A)
_EthLineIndex_Type=InterfaceIndex
_EthLineIndex_Object=MibTableColumn
ethLineIndex=_EthLineIndex_Object((1,3,6,1,4,1,4515,1,1,1,1,1,1),_EthLineIndex_Type())
ethLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethLineIndex.setStatus(_A)
class _EthTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_EthTimeElapsed_Type.__name__=_C
_EthTimeElapsed_Object=MibTableColumn
ethTimeElapsed=_EthTimeElapsed_Object((1,3,6,1,4,1,4515,1,1,1,1,1,2),_EthTimeElapsed_Type())
ethTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTimeElapsed.setStatus(_A)
class _EthValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_EthValidIntervals_Type.__name__=_C
_EthValidIntervals_Object=MibTableColumn
ethValidIntervals=_EthValidIntervals_Object((1,3,6,1,4,1,4515,1,1,1,1,1,3),_EthValidIntervals_Type())
ethValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:ethValidIntervals.setStatus(_A)
_EthResetPm_Type=Integer32
_EthResetPm_Object=MibTableColumn
ethResetPm=_EthResetPm_Object((1,3,6,1,4,1,4515,1,1,1,1,1,4),_EthResetPm_Type())
ethResetPm.setMaxAccess(_E)
if mibBuilder.loadTexts:ethResetPm.setStatus(_A)
_EthAutoNegSupported_Type=TruthValue
_EthAutoNegSupported_Object=MibTableColumn
ethAutoNegSupported=_EthAutoNegSupported_Object((1,3,6,1,4,1,4515,1,1,1,1,1,5),_EthAutoNegSupported_Type())
ethAutoNegSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:ethAutoNegSupported.setStatus(_A)
class _EthAutoNegAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_EthAutoNegAdminStatus_Type.__name__=_C
_EthAutoNegAdminStatus_Object=MibTableColumn
ethAutoNegAdminStatus=_EthAutoNegAdminStatus_Object((1,3,6,1,4,1,4515,1,1,1,1,1,6),_EthAutoNegAdminStatus_Type())
ethAutoNegAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ethAutoNegAdminStatus.setStatus(_A)
class _EthConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_EthConfigStatus_Type.__name__=_C
_EthConfigStatus_Object=MibTableColumn
ethConfigStatus=_EthConfigStatus_Object((1,3,6,1,4,1,4515,1,1,1,1,1,7),_EthConfigStatus_Type())
ethConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethConfigStatus.setStatus(_A)
class _EthTransceiverType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('base1000SX',2),('base1000LX',3)))
_EthTransceiverType_Type.__name__=_C
_EthTransceiverType_Object=MibTableColumn
ethTransceiverType=_EthTransceiverType_Object((1,3,6,1,4,1,4515,1,1,1,1,1,8),_EthTransceiverType_Type())
ethTransceiverType.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTransceiverType.setStatus(_A)
class _EthPauseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,16383))
_EthPauseTime_Type.__name__=_C
_EthPauseTime_Object=MibTableColumn
ethPauseTime=_EthPauseTime_Object((1,3,6,1,4,1,4515,1,1,1,1,1,9),_EthPauseTime_Type())
ethPauseTime.setMaxAccess(_E)
if mibBuilder.loadTexts:ethPauseTime.setStatus(_A)
_EthPauseEnable_Type=TruthValue
_EthPauseEnable_Object=MibTableColumn
ethPauseEnable=_EthPauseEnable_Object((1,3,6,1,4,1,4515,1,1,1,1,1,10),_EthPauseEnable_Type())
ethPauseEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ethPauseEnable.setStatus(_A)
_EthResetPmCounters_Type=Integer32
_EthResetPmCounters_Object=MibTableColumn
ethResetPmCounters=_EthResetPmCounters_Object((1,3,6,1,4,1,4515,1,1,1,1,1,11),_EthResetPmCounters_Type())
ethResetPmCounters.setMaxAccess(_E)
if mibBuilder.loadTexts:ethResetPmCounters.setStatus(_A)
class _EthTransceiverMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('copper',2),('fiber',3)))
_EthTransceiverMedia_Type.__name__=_C
_EthTransceiverMedia_Object=MibTableColumn
ethTransceiverMedia=_EthTransceiverMedia_Object((1,3,6,1,4,1,4515,1,1,1,1,1,12),_EthTransceiverMedia_Type())
ethTransceiverMedia.setMaxAccess(_E)
if mibBuilder.loadTexts:ethTransceiverMedia.setStatus(_A)
_EthCurrentTable_Object=MibTable
ethCurrentTable=_EthCurrentTable_Object((1,3,6,1,4,1,4515,1,1,1,2))
if mibBuilder.loadTexts:ethCurrentTable.setStatus(_A)
_EthCurrentEntry_Object=MibTableRow
ethCurrentEntry=_EthCurrentEntry_Object((1,3,6,1,4,1,4515,1,1,1,2,1))
ethCurrentEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:ethCurrentEntry.setStatus(_A)
_EthCurrentIndex_Type=InterfaceIndex
_EthCurrentIndex_Object=MibTableColumn
ethCurrentIndex=_EthCurrentIndex_Object((1,3,6,1,4,1,4515,1,1,1,2,1,1),_EthCurrentIndex_Type())
ethCurrentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentIndex.setStatus(_A)
_EthCurrentRxDropEvents_Type=Counter64
_EthCurrentRxDropEvents_Object=MibTableColumn
ethCurrentRxDropEvents=_EthCurrentRxDropEvents_Object((1,3,6,1,4,1,4515,1,1,1,2,1,2),_EthCurrentRxDropEvents_Type())
ethCurrentRxDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentRxDropEvents.setStatus(_A)
_EthCurrentOctets_Type=Counter64
_EthCurrentOctets_Object=MibTableColumn
ethCurrentOctets=_EthCurrentOctets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,3),_EthCurrentOctets_Type())
ethCurrentOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentOctets.setStatus(_A)
_EthCurrentPkts_Type=Counter64
_EthCurrentPkts_Object=MibTableColumn
ethCurrentPkts=_EthCurrentPkts_Object((1,3,6,1,4,1,4515,1,1,1,2,1,4),_EthCurrentPkts_Type())
ethCurrentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentPkts.setStatus(_A)
_EthCurrentBroadcastPkts_Type=Counter64
_EthCurrentBroadcastPkts_Object=MibTableColumn
ethCurrentBroadcastPkts=_EthCurrentBroadcastPkts_Object((1,3,6,1,4,1,4515,1,1,1,2,1,5),_EthCurrentBroadcastPkts_Type())
ethCurrentBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentBroadcastPkts.setStatus(_A)
_EthCurrentMulticastPkts_Type=Counter64
_EthCurrentMulticastPkts_Object=MibTableColumn
ethCurrentMulticastPkts=_EthCurrentMulticastPkts_Object((1,3,6,1,4,1,4515,1,1,1,2,1,6),_EthCurrentMulticastPkts_Type())
ethCurrentMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentMulticastPkts.setStatus(_A)
_EthCurrentCRCAlignErrors_Type=Counter64
_EthCurrentCRCAlignErrors_Object=MibTableColumn
ethCurrentCRCAlignErrors=_EthCurrentCRCAlignErrors_Object((1,3,6,1,4,1,4515,1,1,1,2,1,7),_EthCurrentCRCAlignErrors_Type())
ethCurrentCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentCRCAlignErrors.setStatus(_A)
_EthCurrentUndersizePkts_Type=Counter64
_EthCurrentUndersizePkts_Object=MibTableColumn
ethCurrentUndersizePkts=_EthCurrentUndersizePkts_Object((1,3,6,1,4,1,4515,1,1,1,2,1,8),_EthCurrentUndersizePkts_Type())
ethCurrentUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentUndersizePkts.setStatus(_A)
_EthCurrentOversizePkts_Type=Counter64
_EthCurrentOversizePkts_Object=MibTableColumn
ethCurrentOversizePkts=_EthCurrentOversizePkts_Object((1,3,6,1,4,1,4515,1,1,1,2,1,9),_EthCurrentOversizePkts_Type())
ethCurrentOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentOversizePkts.setStatus(_A)
_EthCurrentFragments_Type=Counter64
_EthCurrentFragments_Object=MibTableColumn
ethCurrentFragments=_EthCurrentFragments_Object((1,3,6,1,4,1,4515,1,1,1,2,1,10),_EthCurrentFragments_Type())
ethCurrentFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentFragments.setStatus(_A)
_EthCurrentJabbers_Type=Counter64
_EthCurrentJabbers_Object=MibTableColumn
ethCurrentJabbers=_EthCurrentJabbers_Object((1,3,6,1,4,1,4515,1,1,1,2,1,11),_EthCurrentJabbers_Type())
ethCurrentJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentJabbers.setStatus(_A)
_EthCurrentCollisions_Type=Counter64
_EthCurrentCollisions_Object=MibTableColumn
ethCurrentCollisions=_EthCurrentCollisions_Object((1,3,6,1,4,1,4515,1,1,1,2,1,12),_EthCurrentCollisions_Type())
ethCurrentCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentCollisions.setStatus(_A)
_EthCurrentUtilization_Type=Counter64
_EthCurrentUtilization_Object=MibTableColumn
ethCurrentUtilization=_EthCurrentUtilization_Object((1,3,6,1,4,1,4515,1,1,1,2,1,13),_EthCurrentUtilization_Type())
ethCurrentUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentUtilization.setStatus(_A)
_EthCurrentTxOctets_Type=Counter64
_EthCurrentTxOctets_Object=MibTableColumn
ethCurrentTxOctets=_EthCurrentTxOctets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,14),_EthCurrentTxOctets_Type())
ethCurrentTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxOctets.setStatus(_A)
_EthCurrentTxPkts_Type=Counter64
_EthCurrentTxPkts_Object=MibTableColumn
ethCurrentTxPkts=_EthCurrentTxPkts_Object((1,3,6,1,4,1,4515,1,1,1,2,1,15),_EthCurrentTxPkts_Type())
ethCurrentTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxPkts.setStatus(_A)
_EthCurrentRxPause_Type=Counter64
_EthCurrentRxPause_Object=MibTableColumn
ethCurrentRxPause=_EthCurrentRxPause_Object((1,3,6,1,4,1,4515,1,1,1,2,1,16),_EthCurrentRxPause_Type())
ethCurrentRxPause.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentRxPause.setStatus(_A)
_EthCurrentTxPause_Type=Counter64
_EthCurrentTxPause_Object=MibTableColumn
ethCurrentTxPause=_EthCurrentTxPause_Object((1,3,6,1,4,1,4515,1,1,1,2,1,17),_EthCurrentTxPause_Type())
ethCurrentTxPause.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxPause.setStatus(_A)
_EthCurrentTxDropEvents_Type=Counter64
_EthCurrentTxDropEvents_Object=MibTableColumn
ethCurrentTxDropEvents=_EthCurrentTxDropEvents_Object((1,3,6,1,4,1,4515,1,1,1,2,1,18),_EthCurrentTxDropEvents_Type())
ethCurrentTxDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxDropEvents.setStatus(_A)
_EthCurrentRxPkts64Octets_Type=Counter64
_EthCurrentRxPkts64Octets_Object=MibTableColumn
ethCurrentRxPkts64Octets=_EthCurrentRxPkts64Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,19),_EthCurrentRxPkts64Octets_Type())
ethCurrentRxPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentRxPkts64Octets.setStatus(_A)
_EthCurrentRxPkts65to127Octets_Type=Counter64
_EthCurrentRxPkts65to127Octets_Object=MibTableColumn
ethCurrentRxPkts65to127Octets=_EthCurrentRxPkts65to127Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,20),_EthCurrentRxPkts65to127Octets_Type())
ethCurrentRxPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentRxPkts65to127Octets.setStatus(_A)
_EthCurrentRxPkts128to255Octets_Type=Counter64
_EthCurrentRxPkts128to255Octets_Object=MibTableColumn
ethCurrentRxPkts128to255Octets=_EthCurrentRxPkts128to255Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,21),_EthCurrentRxPkts128to255Octets_Type())
ethCurrentRxPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentRxPkts128to255Octets.setStatus(_A)
_EthCurrentRxPkts256to511Octets_Type=Counter64
_EthCurrentRxPkts256to511Octets_Object=MibTableColumn
ethCurrentRxPkts256to511Octets=_EthCurrentRxPkts256to511Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,22),_EthCurrentRxPkts256to511Octets_Type())
ethCurrentRxPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentRxPkts256to511Octets.setStatus(_A)
_EthCurrentRxPkts512to1023Octets_Type=Counter64
_EthCurrentRxPkts512to1023Octets_Object=MibTableColumn
ethCurrentRxPkts512to1023Octets=_EthCurrentRxPkts512to1023Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,23),_EthCurrentRxPkts512to1023Octets_Type())
ethCurrentRxPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentRxPkts512to1023Octets.setStatus(_A)
_EthCurrentRxPkts1024to1518Octets_Type=Counter64
_EthCurrentRxPkts1024to1518Octets_Object=MibTableColumn
ethCurrentRxPkts1024to1518Octets=_EthCurrentRxPkts1024to1518Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,24),_EthCurrentRxPkts1024to1518Octets_Type())
ethCurrentRxPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentRxPkts1024to1518Octets.setStatus(_A)
_EthCurrentRxPkts1519to1522Octets_Type=Counter64
_EthCurrentRxPkts1519to1522Octets_Object=MibTableColumn
ethCurrentRxPkts1519to1522Octets=_EthCurrentRxPkts1519to1522Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,25),_EthCurrentRxPkts1519to1522Octets_Type())
ethCurrentRxPkts1519to1522Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentRxPkts1519to1522Octets.setStatus(_A)
_EthCurrentTxPkts64Octets_Type=Counter64
_EthCurrentTxPkts64Octets_Object=MibTableColumn
ethCurrentTxPkts64Octets=_EthCurrentTxPkts64Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,26),_EthCurrentTxPkts64Octets_Type())
ethCurrentTxPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxPkts64Octets.setStatus(_A)
_EthCurrentTxPkts65to127Octets_Type=Counter64
_EthCurrentTxPkts65to127Octets_Object=MibTableColumn
ethCurrentTxPkts65to127Octets=_EthCurrentTxPkts65to127Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,27),_EthCurrentTxPkts65to127Octets_Type())
ethCurrentTxPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxPkts65to127Octets.setStatus(_A)
_EthCurrentTxPkts128to255Octets_Type=Counter64
_EthCurrentTxPkts128to255Octets_Object=MibTableColumn
ethCurrentTxPkts128to255Octets=_EthCurrentTxPkts128to255Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,28),_EthCurrentTxPkts128to255Octets_Type())
ethCurrentTxPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxPkts128to255Octets.setStatus(_A)
_EthCurrentTxPkts256to511Octets_Type=Counter64
_EthCurrentTxPkts256to511Octets_Object=MibTableColumn
ethCurrentTxPkts256to511Octets=_EthCurrentTxPkts256to511Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,29),_EthCurrentTxPkts256to511Octets_Type())
ethCurrentTxPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxPkts256to511Octets.setStatus(_A)
_EthCurrentTxPkts512to1023Octets_Type=Counter64
_EthCurrentTxPkts512to1023Octets_Object=MibTableColumn
ethCurrentTxPkts512to1023Octets=_EthCurrentTxPkts512to1023Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,30),_EthCurrentTxPkts512to1023Octets_Type())
ethCurrentTxPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxPkts512to1023Octets.setStatus(_A)
_EthCurrentTxPkts1024to1518Octets_Type=Counter64
_EthCurrentTxPkts1024to1518Octets_Object=MibTableColumn
ethCurrentTxPkts1024to1518Octets=_EthCurrentTxPkts1024to1518Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,31),_EthCurrentTxPkts1024to1518Octets_Type())
ethCurrentTxPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxPkts1024to1518Octets.setStatus(_A)
_EthCurrentTxPkts1519to1522Octets_Type=Counter64
_EthCurrentTxPkts1519to1522Octets_Object=MibTableColumn
ethCurrentTxPkts1519to1522Octets=_EthCurrentTxPkts1519to1522Octets_Object((1,3,6,1,4,1,4515,1,1,1,2,1,32),_EthCurrentTxPkts1519to1522Octets_Type())
ethCurrentTxPkts1519to1522Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxPkts1519to1522Octets.setStatus(_A)
_EthCurrentRxVlanPkts_Type=Counter64
_EthCurrentRxVlanPkts_Object=MibTableColumn
ethCurrentRxVlanPkts=_EthCurrentRxVlanPkts_Object((1,3,6,1,4,1,4515,1,1,1,2,1,33),_EthCurrentRxVlanPkts_Type())
ethCurrentRxVlanPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentRxVlanPkts.setStatus(_A)
_EthCurrentTxVlanPkts_Type=Counter64
_EthCurrentTxVlanPkts_Object=MibTableColumn
ethCurrentTxVlanPkts=_EthCurrentTxVlanPkts_Object((1,3,6,1,4,1,4515,1,1,1,2,1,34),_EthCurrentTxVlanPkts_Type())
ethCurrentTxVlanPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxVlanPkts.setStatus(_A)
_EthCurrentRxJumboPkts_Type=Counter64
_EthCurrentRxJumboPkts_Object=MibTableColumn
ethCurrentRxJumboPkts=_EthCurrentRxJumboPkts_Object((1,3,6,1,4,1,4515,1,1,1,2,1,35),_EthCurrentRxJumboPkts_Type())
ethCurrentRxJumboPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentRxJumboPkts.setStatus(_A)
_EthCurrentTxJumboPkts_Type=Counter64
_EthCurrentTxJumboPkts_Object=MibTableColumn
ethCurrentTxJumboPkts=_EthCurrentTxJumboPkts_Object((1,3,6,1,4,1,4515,1,1,1,2,1,36),_EthCurrentTxJumboPkts_Type())
ethCurrentTxJumboPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethCurrentTxJumboPkts.setStatus(_A)
_EthIntervalTable_Object=MibTable
ethIntervalTable=_EthIntervalTable_Object((1,3,6,1,4,1,4515,1,1,1,3))
if mibBuilder.loadTexts:ethIntervalTable.setStatus(_A)
_EthIntervalEntry_Object=MibTableRow
ethIntervalEntry=_EthIntervalEntry_Object((1,3,6,1,4,1,4515,1,1,1,3,1))
ethIntervalEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:ethIntervalEntry.setStatus(_A)
_EthIntervalIndex_Type=InterfaceIndex
_EthIntervalIndex_Object=MibTableColumn
ethIntervalIndex=_EthIntervalIndex_Object((1,3,6,1,4,1,4515,1,1,1,3,1,1),_EthIntervalIndex_Type())
ethIntervalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalIndex.setStatus(_A)
class _EthIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_EthIntervalNumber_Type.__name__=_C
_EthIntervalNumber_Object=MibTableColumn
ethIntervalNumber=_EthIntervalNumber_Object((1,3,6,1,4,1,4515,1,1,1,3,1,2),_EthIntervalNumber_Type())
ethIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalNumber.setStatus(_A)
_EthIntervalDropEvents_Type=Counter64
_EthIntervalDropEvents_Object=MibTableColumn
ethIntervalDropEvents=_EthIntervalDropEvents_Object((1,3,6,1,4,1,4515,1,1,1,3,1,3),_EthIntervalDropEvents_Type())
ethIntervalDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalDropEvents.setStatus(_A)
_EthIntervalOctets_Type=Counter64
_EthIntervalOctets_Object=MibTableColumn
ethIntervalOctets=_EthIntervalOctets_Object((1,3,6,1,4,1,4515,1,1,1,3,1,4),_EthIntervalOctets_Type())
ethIntervalOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalOctets.setStatus(_A)
_EthIntervalPkts_Type=Counter64
_EthIntervalPkts_Object=MibTableColumn
ethIntervalPkts=_EthIntervalPkts_Object((1,3,6,1,4,1,4515,1,1,1,3,1,5),_EthIntervalPkts_Type())
ethIntervalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalPkts.setStatus(_A)
_EthIntervalBroadcastPkts_Type=Counter64
_EthIntervalBroadcastPkts_Object=MibTableColumn
ethIntervalBroadcastPkts=_EthIntervalBroadcastPkts_Object((1,3,6,1,4,1,4515,1,1,1,3,1,6),_EthIntervalBroadcastPkts_Type())
ethIntervalBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalBroadcastPkts.setStatus(_A)
_EthIntervalMulticastPkts_Type=Counter64
_EthIntervalMulticastPkts_Object=MibTableColumn
ethIntervalMulticastPkts=_EthIntervalMulticastPkts_Object((1,3,6,1,4,1,4515,1,1,1,3,1,7),_EthIntervalMulticastPkts_Type())
ethIntervalMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalMulticastPkts.setStatus(_A)
_EthIntervalCRCAlignErrors_Type=Counter64
_EthIntervalCRCAlignErrors_Object=MibTableColumn
ethIntervalCRCAlignErrors=_EthIntervalCRCAlignErrors_Object((1,3,6,1,4,1,4515,1,1,1,3,1,8),_EthIntervalCRCAlignErrors_Type())
ethIntervalCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalCRCAlignErrors.setStatus(_A)
_EthIntervalUndersizePkts_Type=Counter64
_EthIntervalUndersizePkts_Object=MibTableColumn
ethIntervalUndersizePkts=_EthIntervalUndersizePkts_Object((1,3,6,1,4,1,4515,1,1,1,3,1,9),_EthIntervalUndersizePkts_Type())
ethIntervalUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalUndersizePkts.setStatus(_A)
_EthIntervalOversizePkts_Type=Counter64
_EthIntervalOversizePkts_Object=MibTableColumn
ethIntervalOversizePkts=_EthIntervalOversizePkts_Object((1,3,6,1,4,1,4515,1,1,1,3,1,10),_EthIntervalOversizePkts_Type())
ethIntervalOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalOversizePkts.setStatus(_A)
_EthIntervalFragments_Type=Counter64
_EthIntervalFragments_Object=MibTableColumn
ethIntervalFragments=_EthIntervalFragments_Object((1,3,6,1,4,1,4515,1,1,1,3,1,11),_EthIntervalFragments_Type())
ethIntervalFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalFragments.setStatus(_A)
_EthIntervalJabbers_Type=Counter64
_EthIntervalJabbers_Object=MibTableColumn
ethIntervalJabbers=_EthIntervalJabbers_Object((1,3,6,1,4,1,4515,1,1,1,3,1,12),_EthIntervalJabbers_Type())
ethIntervalJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalJabbers.setStatus(_A)
_EthIntervalCollisions_Type=Counter64
_EthIntervalCollisions_Object=MibTableColumn
ethIntervalCollisions=_EthIntervalCollisions_Object((1,3,6,1,4,1,4515,1,1,1,3,1,13),_EthIntervalCollisions_Type())
ethIntervalCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalCollisions.setStatus(_A)
_EthIntervalUtilization_Type=Counter64
_EthIntervalUtilization_Object=MibTableColumn
ethIntervalUtilization=_EthIntervalUtilization_Object((1,3,6,1,4,1,4515,1,1,1,3,1,14),_EthIntervalUtilization_Type())
ethIntervalUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalUtilization.setStatus(_A)
_EthIntervalTxOctets_Type=Counter64
_EthIntervalTxOctets_Object=MibTableColumn
ethIntervalTxOctets=_EthIntervalTxOctets_Object((1,3,6,1,4,1,4515,1,1,1,3,1,15),_EthIntervalTxOctets_Type())
ethIntervalTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalTxOctets.setStatus(_A)
_EthIntervalTxPkts_Type=Counter64
_EthIntervalTxPkts_Object=MibTableColumn
ethIntervalTxPkts=_EthIntervalTxPkts_Object((1,3,6,1,4,1,4515,1,1,1,3,1,16),_EthIntervalTxPkts_Type())
ethIntervalTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalTxPkts.setStatus(_A)
_EthIntervalRxPause_Type=Counter64
_EthIntervalRxPause_Object=MibTableColumn
ethIntervalRxPause=_EthIntervalRxPause_Object((1,3,6,1,4,1,4515,1,1,1,3,1,17),_EthIntervalRxPause_Type())
ethIntervalRxPause.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalRxPause.setStatus(_A)
_EthIntervalTxPause_Type=Counter64
_EthIntervalTxPause_Object=MibTableColumn
ethIntervalTxPause=_EthIntervalTxPause_Object((1,3,6,1,4,1,4515,1,1,1,3,1,18),_EthIntervalTxPause_Type())
ethIntervalTxPause.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalTxPause.setStatus(_A)
_EthIntervalValidData_Type=TruthValue
_EthIntervalValidData_Object=MibTableColumn
ethIntervalValidData=_EthIntervalValidData_Object((1,3,6,1,4,1,4515,1,1,1,3,1,19),_EthIntervalValidData_Type())
ethIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalValidData.setStatus(_A)
_EthIntervalTcaFlag_Type=TruthValue
_EthIntervalTcaFlag_Object=MibTableColumn
ethIntervalTcaFlag=_EthIntervalTcaFlag_Object((1,3,6,1,4,1,4515,1,1,1,3,1,20),_EthIntervalTcaFlag_Type())
ethIntervalTcaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntervalTcaFlag.setStatus(_A)
_EthTotalTable_Object=MibTable
ethTotalTable=_EthTotalTable_Object((1,3,6,1,4,1,4515,1,1,1,4))
if mibBuilder.loadTexts:ethTotalTable.setStatus(_A)
_EthTotalEntry_Object=MibTableRow
ethTotalEntry=_EthTotalEntry_Object((1,3,6,1,4,1,4515,1,1,1,4,1))
ethTotalEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:ethTotalEntry.setStatus(_A)
_EthTotalIndex_Type=InterfaceIndex
_EthTotalIndex_Object=MibTableColumn
ethTotalIndex=_EthTotalIndex_Object((1,3,6,1,4,1,4515,1,1,1,4,1,1),_EthTotalIndex_Type())
ethTotalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalIndex.setStatus(_A)
class _EthTotalDayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,33))
_EthTotalDayNumber_Type.__name__=_C
_EthTotalDayNumber_Object=MibTableColumn
ethTotalDayNumber=_EthTotalDayNumber_Object((1,3,6,1,4,1,4515,1,1,1,4,1,2),_EthTotalDayNumber_Type())
ethTotalDayNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ethTotalDayNumber.setStatus(_A)
_EthTotalDropEvents_Type=Counter64
_EthTotalDropEvents_Object=MibTableColumn
ethTotalDropEvents=_EthTotalDropEvents_Object((1,3,6,1,4,1,4515,1,1,1,4,1,3),_EthTotalDropEvents_Type())
ethTotalDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalDropEvents.setStatus(_A)
_EthTotalOctets_Type=Counter64
_EthTotalOctets_Object=MibTableColumn
ethTotalOctets=_EthTotalOctets_Object((1,3,6,1,4,1,4515,1,1,1,4,1,4),_EthTotalOctets_Type())
ethTotalOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalOctets.setStatus(_A)
_EthTotalPkts_Type=Counter64
_EthTotalPkts_Object=MibTableColumn
ethTotalPkts=_EthTotalPkts_Object((1,3,6,1,4,1,4515,1,1,1,4,1,5),_EthTotalPkts_Type())
ethTotalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalPkts.setStatus(_A)
_EthTotalBroadcastPkts_Type=Counter64
_EthTotalBroadcastPkts_Object=MibTableColumn
ethTotalBroadcastPkts=_EthTotalBroadcastPkts_Object((1,3,6,1,4,1,4515,1,1,1,4,1,6),_EthTotalBroadcastPkts_Type())
ethTotalBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalBroadcastPkts.setStatus(_A)
_EthTotalMulticastPkts_Type=Counter64
_EthTotalMulticastPkts_Object=MibTableColumn
ethTotalMulticastPkts=_EthTotalMulticastPkts_Object((1,3,6,1,4,1,4515,1,1,1,4,1,7),_EthTotalMulticastPkts_Type())
ethTotalMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalMulticastPkts.setStatus(_A)
_EthTotalCRCAlignErrors_Type=Counter64
_EthTotalCRCAlignErrors_Object=MibTableColumn
ethTotalCRCAlignErrors=_EthTotalCRCAlignErrors_Object((1,3,6,1,4,1,4515,1,1,1,4,1,8),_EthTotalCRCAlignErrors_Type())
ethTotalCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalCRCAlignErrors.setStatus(_A)
_EthTotalUndersizePkts_Type=Counter64
_EthTotalUndersizePkts_Object=MibTableColumn
ethTotalUndersizePkts=_EthTotalUndersizePkts_Object((1,3,6,1,4,1,4515,1,1,1,4,1,9),_EthTotalUndersizePkts_Type())
ethTotalUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalUndersizePkts.setStatus(_A)
_EthTotalOversizePkts_Type=Counter64
_EthTotalOversizePkts_Object=MibTableColumn
ethTotalOversizePkts=_EthTotalOversizePkts_Object((1,3,6,1,4,1,4515,1,1,1,4,1,10),_EthTotalOversizePkts_Type())
ethTotalOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalOversizePkts.setStatus(_A)
_EthTotalFragments_Type=Counter64
_EthTotalFragments_Object=MibTableColumn
ethTotalFragments=_EthTotalFragments_Object((1,3,6,1,4,1,4515,1,1,1,4,1,11),_EthTotalFragments_Type())
ethTotalFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalFragments.setStatus(_A)
_EthTotalJabbers_Type=Counter64
_EthTotalJabbers_Object=MibTableColumn
ethTotalJabbers=_EthTotalJabbers_Object((1,3,6,1,4,1,4515,1,1,1,4,1,12),_EthTotalJabbers_Type())
ethTotalJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalJabbers.setStatus(_A)
_EthTotalCollisions_Type=Counter64
_EthTotalCollisions_Object=MibTableColumn
ethTotalCollisions=_EthTotalCollisions_Object((1,3,6,1,4,1,4515,1,1,1,4,1,13),_EthTotalCollisions_Type())
ethTotalCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalCollisions.setStatus(_A)
_EthTotalUtilization_Type=Counter64
_EthTotalUtilization_Object=MibTableColumn
ethTotalUtilization=_EthTotalUtilization_Object((1,3,6,1,4,1,4515,1,1,1,4,1,14),_EthTotalUtilization_Type())
ethTotalUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalUtilization.setStatus(_A)
_EthTotalTxOctets_Type=Counter64
_EthTotalTxOctets_Object=MibTableColumn
ethTotalTxOctets=_EthTotalTxOctets_Object((1,3,6,1,4,1,4515,1,1,1,4,1,15),_EthTotalTxOctets_Type())
ethTotalTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalTxOctets.setStatus(_A)
_EthTotalTxPkts_Type=Counter64
_EthTotalTxPkts_Object=MibTableColumn
ethTotalTxPkts=_EthTotalTxPkts_Object((1,3,6,1,4,1,4515,1,1,1,4,1,16),_EthTotalTxPkts_Type())
ethTotalTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalTxPkts.setStatus(_A)
_EthTotalRxPause_Type=Counter64
_EthTotalRxPause_Object=MibTableColumn
ethTotalRxPause=_EthTotalRxPause_Object((1,3,6,1,4,1,4515,1,1,1,4,1,17),_EthTotalRxPause_Type())
ethTotalRxPause.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalRxPause.setStatus(_A)
_EthTotalTxPause_Type=Counter64
_EthTotalTxPause_Object=MibTableColumn
ethTotalTxPause=_EthTotalTxPause_Object((1,3,6,1,4,1,4515,1,1,1,4,1,18),_EthTotalTxPause_Type())
ethTotalTxPause.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalTxPause.setStatus(_A)
_EthTotalValidData_Type=TruthValue
_EthTotalValidData_Object=MibTableColumn
ethTotalValidData=_EthTotalValidData_Object((1,3,6,1,4,1,4515,1,1,1,4,1,19),_EthTotalValidData_Type())
ethTotalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTotalValidData.setStatus(_A)
_EthTraps_ObjectIdentity=ObjectIdentity
ethTraps=_EthTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,1,1,7))
ethStatusChange=NotificationType((1,3,6,1,4,1,4515,1,1,1,7,1))
ethStatusChange.setObjects(*((_D,_F),(_D,_L)))
if mibBuilder.loadTexts:ethStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'slEthernet':slEthernet,'ethConfigTable':ethConfigTable,'ethConfigEntry':ethConfigEntry,_F:ethLineIndex,'ethTimeElapsed':ethTimeElapsed,'ethValidIntervals':ethValidIntervals,'ethResetPm':ethResetPm,'ethAutoNegSupported':ethAutoNegSupported,'ethAutoNegAdminStatus':ethAutoNegAdminStatus,_L:ethConfigStatus,'ethTransceiverType':ethTransceiverType,'ethPauseTime':ethPauseTime,'ethPauseEnable':ethPauseEnable,'ethResetPmCounters':ethResetPmCounters,'ethTransceiverMedia':ethTransceiverMedia,'ethCurrentTable':ethCurrentTable,'ethCurrentEntry':ethCurrentEntry,_G:ethCurrentIndex,'ethCurrentRxDropEvents':ethCurrentRxDropEvents,'ethCurrentOctets':ethCurrentOctets,'ethCurrentPkts':ethCurrentPkts,'ethCurrentBroadcastPkts':ethCurrentBroadcastPkts,'ethCurrentMulticastPkts':ethCurrentMulticastPkts,'ethCurrentCRCAlignErrors':ethCurrentCRCAlignErrors,'ethCurrentUndersizePkts':ethCurrentUndersizePkts,'ethCurrentOversizePkts':ethCurrentOversizePkts,'ethCurrentFragments':ethCurrentFragments,'ethCurrentJabbers':ethCurrentJabbers,'ethCurrentCollisions':ethCurrentCollisions,'ethCurrentUtilization':ethCurrentUtilization,'ethCurrentTxOctets':ethCurrentTxOctets,'ethCurrentTxPkts':ethCurrentTxPkts,'ethCurrentRxPause':ethCurrentRxPause,'ethCurrentTxPause':ethCurrentTxPause,'ethCurrentTxDropEvents':ethCurrentTxDropEvents,'ethCurrentRxPkts64Octets':ethCurrentRxPkts64Octets,'ethCurrentRxPkts65to127Octets':ethCurrentRxPkts65to127Octets,'ethCurrentRxPkts128to255Octets':ethCurrentRxPkts128to255Octets,'ethCurrentRxPkts256to511Octets':ethCurrentRxPkts256to511Octets,'ethCurrentRxPkts512to1023Octets':ethCurrentRxPkts512to1023Octets,'ethCurrentRxPkts1024to1518Octets':ethCurrentRxPkts1024to1518Octets,'ethCurrentRxPkts1519to1522Octets':ethCurrentRxPkts1519to1522Octets,'ethCurrentTxPkts64Octets':ethCurrentTxPkts64Octets,'ethCurrentTxPkts65to127Octets':ethCurrentTxPkts65to127Octets,'ethCurrentTxPkts128to255Octets':ethCurrentTxPkts128to255Octets,'ethCurrentTxPkts256to511Octets':ethCurrentTxPkts256to511Octets,'ethCurrentTxPkts512to1023Octets':ethCurrentTxPkts512to1023Octets,'ethCurrentTxPkts1024to1518Octets':ethCurrentTxPkts1024to1518Octets,'ethCurrentTxPkts1519to1522Octets':ethCurrentTxPkts1519to1522Octets,'ethCurrentRxVlanPkts':ethCurrentRxVlanPkts,'ethCurrentTxVlanPkts':ethCurrentTxVlanPkts,'ethCurrentRxJumboPkts':ethCurrentRxJumboPkts,'ethCurrentTxJumboPkts':ethCurrentTxJumboPkts,'ethIntervalTable':ethIntervalTable,'ethIntervalEntry':ethIntervalEntry,_H:ethIntervalIndex,_I:ethIntervalNumber,'ethIntervalDropEvents':ethIntervalDropEvents,'ethIntervalOctets':ethIntervalOctets,'ethIntervalPkts':ethIntervalPkts,'ethIntervalBroadcastPkts':ethIntervalBroadcastPkts,'ethIntervalMulticastPkts':ethIntervalMulticastPkts,'ethIntervalCRCAlignErrors':ethIntervalCRCAlignErrors,'ethIntervalUndersizePkts':ethIntervalUndersizePkts,'ethIntervalOversizePkts':ethIntervalOversizePkts,'ethIntervalFragments':ethIntervalFragments,'ethIntervalJabbers':ethIntervalJabbers,'ethIntervalCollisions':ethIntervalCollisions,'ethIntervalUtilization':ethIntervalUtilization,'ethIntervalTxOctets':ethIntervalTxOctets,'ethIntervalTxPkts':ethIntervalTxPkts,'ethIntervalRxPause':ethIntervalRxPause,'ethIntervalTxPause':ethIntervalTxPause,'ethIntervalValidData':ethIntervalValidData,'ethIntervalTcaFlag':ethIntervalTcaFlag,'ethTotalTable':ethTotalTable,'ethTotalEntry':ethTotalEntry,_J:ethTotalIndex,_K:ethTotalDayNumber,'ethTotalDropEvents':ethTotalDropEvents,'ethTotalOctets':ethTotalOctets,'ethTotalPkts':ethTotalPkts,'ethTotalBroadcastPkts':ethTotalBroadcastPkts,'ethTotalMulticastPkts':ethTotalMulticastPkts,'ethTotalCRCAlignErrors':ethTotalCRCAlignErrors,'ethTotalUndersizePkts':ethTotalUndersizePkts,'ethTotalOversizePkts':ethTotalOversizePkts,'ethTotalFragments':ethTotalFragments,'ethTotalJabbers':ethTotalJabbers,'ethTotalCollisions':ethTotalCollisions,'ethTotalUtilization':ethTotalUtilization,'ethTotalTxOctets':ethTotalTxOctets,'ethTotalTxPkts':ethTotalTxPkts,'ethTotalRxPause':ethTotalRxPause,'ethTotalTxPause':ethTotalTxPause,'ethTotalValidData':ethTotalValidData,'ethTraps':ethTraps,'ethStatusChange':ethStatusChange})