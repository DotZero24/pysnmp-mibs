_P='esconPortConfigStatus'
_O='esconCounterValue'
_N='esconCounterId'
_M='esconPortDayThresholdIndex'
_L='esconPortIntervalThresholdIndex'
_K='esconPortTotalDayNumber'
_J='esconPortTotalIndex'
_I='esconPortIntervalNumber'
_H='esconPortIntervalIndex'
_G='esconPortCurrentIndex'
_F='esconPortConfigIndex'
_E='Integer32'
_D='SL-ESCON-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
slService,=mibBuilder.importSymbols('SL-NE-MIB','slService')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
esconMIB=ModuleIdentity((1,3,6,1,4,1,4515,1,1,5))
class EsconAddressId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class EsconNodeDescription(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_EsconMIBObjects_ObjectIdentity=ObjectIdentity
esconMIBObjects=_EsconMIBObjects_ObjectIdentity((1,3,6,1,4,1,4515,1,1,5,1))
_EsconConfig_ObjectIdentity=ObjectIdentity
esconConfig=_EsconConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,1,5,1,1))
_EsconPortConfigTable_Object=MibTable
esconPortConfigTable=_EsconPortConfigTable_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1))
if mibBuilder.loadTexts:esconPortConfigTable.setStatus(_A)
_EsconPortConfigEntry_Object=MibTableRow
esconPortConfigEntry=_EsconPortConfigEntry_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1,1))
esconPortConfigEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:esconPortConfigEntry.setStatus(_A)
_EsconPortConfigIndex_Type=InterfaceIndex
_EsconPortConfigIndex_Object=MibTableColumn
esconPortConfigIndex=_EsconPortConfigIndex_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1,1,1),_EsconPortConfigIndex_Type())
esconPortConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortConfigIndex.setStatus(_A)
_EsconPortConfigSrcAddress_Type=EsconAddressId
_EsconPortConfigSrcAddress_Object=MibTableColumn
esconPortConfigSrcAddress=_EsconPortConfigSrcAddress_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1,1,2),_EsconPortConfigSrcAddress_Type())
esconPortConfigSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortConfigSrcAddress.setStatus(_A)
_EsconPortConfigSrcDescription_Type=EsconNodeDescription
_EsconPortConfigSrcDescription_Object=MibTableColumn
esconPortConfigSrcDescription=_EsconPortConfigSrcDescription_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1,1,3),_EsconPortConfigSrcDescription_Type())
esconPortConfigSrcDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortConfigSrcDescription.setStatus(_A)
class _EsconPortConfigTranceiverMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('sm',2),('mm',3)))
_EsconPortConfigTranceiverMedia_Type.__name__=_E
_EsconPortConfigTranceiverMedia_Object=MibTableColumn
esconPortConfigTranceiverMedia=_EsconPortConfigTranceiverMedia_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1,1,4),_EsconPortConfigTranceiverMedia_Type())
esconPortConfigTranceiverMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortConfigTranceiverMedia.setStatus(_A)
_EsconPortConfigResetPmCounters_Type=Integer32
_EsconPortConfigResetPmCounters_Object=MibTableColumn
esconPortConfigResetPmCounters=_EsconPortConfigResetPmCounters_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1,1,5),_EsconPortConfigResetPmCounters_Type())
esconPortConfigResetPmCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortConfigResetPmCounters.setStatus(_A)
class _EsconPortConfigTranceiverType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('shortWave',2),('longWave',3)))
_EsconPortConfigTranceiverType_Type.__name__=_E
_EsconPortConfigTranceiverType_Object=MibTableColumn
esconPortConfigTranceiverType=_EsconPortConfigTranceiverType_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1,1,6),_EsconPortConfigTranceiverType_Type())
esconPortConfigTranceiverType.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortConfigTranceiverType.setStatus(_A)
class _EsconPortConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_EsconPortConfigStatus_Type.__name__=_E
_EsconPortConfigStatus_Object=MibTableColumn
esconPortConfigStatus=_EsconPortConfigStatus_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1,1,7),_EsconPortConfigStatus_Type())
esconPortConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortConfigStatus.setStatus(_A)
class _EsconPortConfigValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_EsconPortConfigValidIntervals_Type.__name__=_E
_EsconPortConfigValidIntervals_Object=MibTableColumn
esconPortConfigValidIntervals=_EsconPortConfigValidIntervals_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1,1,8),_EsconPortConfigValidIntervals_Type())
esconPortConfigValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortConfigValidIntervals.setStatus(_A)
class _EsconPortConfigLoginState_Type(Bits):namedValues=NamedValues(*(('signalSense',0),('syncPort',1),('validLogin',2)))
_EsconPortConfigLoginState_Type.__name__='Bits'
_EsconPortConfigLoginState_Object=MibTableColumn
esconPortConfigLoginState=_EsconPortConfigLoginState_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1,1,9),_EsconPortConfigLoginState_Type())
esconPortConfigLoginState.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortConfigLoginState.setStatus(_A)
_EsconPortResetPmCounters_Type=Integer32
_EsconPortResetPmCounters_Object=MibTableColumn
esconPortResetPmCounters=_EsconPortResetPmCounters_Object((1,3,6,1,4,1,4515,1,1,5,1,1,1,1,10),_EsconPortResetPmCounters_Type())
esconPortResetPmCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortResetPmCounters.setStatus(_A)
_EsconPm_ObjectIdentity=ObjectIdentity
esconPm=_EsconPm_ObjectIdentity((1,3,6,1,4,1,4515,1,1,5,1,2))
_EsconPortCurrentTable_Object=MibTable
esconPortCurrentTable=_EsconPortCurrentTable_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1))
if mibBuilder.loadTexts:esconPortCurrentTable.setStatus(_A)
_EsconPortCurrentEntry_Object=MibTableRow
esconPortCurrentEntry=_EsconPortCurrentEntry_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1))
esconPortCurrentEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:esconPortCurrentEntry.setStatus(_A)
_EsconPortCurrentIndex_Type=InterfaceIndex
_EsconPortCurrentIndex_Object=MibTableColumn
esconPortCurrentIndex=_EsconPortCurrentIndex_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,1),_EsconPortCurrentIndex_Type())
esconPortCurrentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentIndex.setStatus(_A)
_EsconPortCurrentRxOctets_Type=Counter64
_EsconPortCurrentRxOctets_Object=MibTableColumn
esconPortCurrentRxOctets=_EsconPortCurrentRxOctets_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,2),_EsconPortCurrentRxOctets_Type())
esconPortCurrentRxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentRxOctets.setStatus(_A)
_EsconPortCurrentRxPkts_Type=Counter64
_EsconPortCurrentRxPkts_Object=MibTableColumn
esconPortCurrentRxPkts=_EsconPortCurrentRxPkts_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,3),_EsconPortCurrentRxPkts_Type())
esconPortCurrentRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentRxPkts.setStatus(_A)
_EsconPortCurrentRxSigLosses_Type=Counter64
_EsconPortCurrentRxSigLosses_Object=MibTableColumn
esconPortCurrentRxSigLosses=_EsconPortCurrentRxSigLosses_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,4),_EsconPortCurrentRxSigLosses_Type())
esconPortCurrentRxSigLosses.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentRxSigLosses.setStatus(_A)
_EsconPortCurrentRxSyncLosses_Type=Counter64
_EsconPortCurrentRxSyncLosses_Object=MibTableColumn
esconPortCurrentRxSyncLosses=_EsconPortCurrentRxSyncLosses_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,5),_EsconPortCurrentRxSyncLosses_Type())
esconPortCurrentRxSyncLosses.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentRxSyncLosses.setStatus(_A)
_EsconPortCurrentRxLinkFailures_Type=Counter64
_EsconPortCurrentRxLinkFailures_Object=MibTableColumn
esconPortCurrentRxLinkFailures=_EsconPortCurrentRxLinkFailures_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,6),_EsconPortCurrentRxLinkFailures_Type())
esconPortCurrentRxLinkFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentRxLinkFailures.setStatus(_A)
_EsconPortCurrentRxInvalidCrcs_Type=Counter64
_EsconPortCurrentRxInvalidCrcs_Object=MibTableColumn
esconPortCurrentRxInvalidCrcs=_EsconPortCurrentRxInvalidCrcs_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,7),_EsconPortCurrentRxInvalidCrcs_Type())
esconPortCurrentRxInvalidCrcs.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentRxInvalidCrcs.setStatus(_A)
_EsconPortCurrentRxDelimiterErrors_Type=Counter64
_EsconPortCurrentRxDelimiterErrors_Object=MibTableColumn
esconPortCurrentRxDelimiterErrors=_EsconPortCurrentRxDelimiterErrors_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,8),_EsconPortCurrentRxDelimiterErrors_Type())
esconPortCurrentRxDelimiterErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentRxDelimiterErrors.setStatus(_A)
_EsconPortCurrentRxDisparityErrors_Type=Counter64
_EsconPortCurrentRxDisparityErrors_Object=MibTableColumn
esconPortCurrentRxDisparityErrors=_EsconPortCurrentRxDisparityErrors_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,9),_EsconPortCurrentRxDisparityErrors_Type())
esconPortCurrentRxDisparityErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentRxDisparityErrors.setStatus(_A)
_EsconPortCurrentRxSizeFrames_Type=Counter64
_EsconPortCurrentRxSizeFrames_Object=MibTableColumn
esconPortCurrentRxSizeFrames=_EsconPortCurrentRxSizeFrames_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,10),_EsconPortCurrentRxSizeFrames_Type())
esconPortCurrentRxSizeFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentRxSizeFrames.setStatus(_A)
_EsconPortCurrentRxInvalidTxWords_Type=Counter64
_EsconPortCurrentRxInvalidTxWords_Object=MibTableColumn
esconPortCurrentRxInvalidTxWords=_EsconPortCurrentRxInvalidTxWords_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,11),_EsconPortCurrentRxInvalidTxWords_Type())
esconPortCurrentRxInvalidTxWords.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentRxInvalidTxWords.setStatus(_A)
_EsconPortCurrentTxOctets_Type=Counter64
_EsconPortCurrentTxOctets_Object=MibTableColumn
esconPortCurrentTxOctets=_EsconPortCurrentTxOctets_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,12),_EsconPortCurrentTxOctets_Type())
esconPortCurrentTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentTxOctets.setStatus(_A)
_EsconPortCurrentTxPkts_Type=Counter64
_EsconPortCurrentTxPkts_Object=MibTableColumn
esconPortCurrentTxPkts=_EsconPortCurrentTxPkts_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,13),_EsconPortCurrentTxPkts_Type())
esconPortCurrentTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentTxPkts.setStatus(_A)
_EsconPortCurrentTxHeaderError_Type=Counter64
_EsconPortCurrentTxHeaderError_Object=MibTableColumn
esconPortCurrentTxHeaderError=_EsconPortCurrentTxHeaderError_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,14),_EsconPortCurrentTxHeaderError_Type())
esconPortCurrentTxHeaderError.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentTxHeaderError.setStatus(_A)
_EsconPortCurrentTxJitterUnderflow_Type=Counter64
_EsconPortCurrentTxJitterUnderflow_Object=MibTableColumn
esconPortCurrentTxJitterUnderflow=_EsconPortCurrentTxJitterUnderflow_Object((1,3,6,1,4,1,4515,1,1,5,1,2,1,1,15),_EsconPortCurrentTxJitterUnderflow_Type())
esconPortCurrentTxJitterUnderflow.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortCurrentTxJitterUnderflow.setStatus(_A)
_EsconPortIntervalTable_Object=MibTable
esconPortIntervalTable=_EsconPortIntervalTable_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2))
if mibBuilder.loadTexts:esconPortIntervalTable.setStatus(_A)
_EsconPortIntervalEntry_Object=MibTableRow
esconPortIntervalEntry=_EsconPortIntervalEntry_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1))
esconPortIntervalEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:esconPortIntervalEntry.setStatus(_A)
_EsconPortIntervalIndex_Type=InterfaceIndex
_EsconPortIntervalIndex_Object=MibTableColumn
esconPortIntervalIndex=_EsconPortIntervalIndex_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,1),_EsconPortIntervalIndex_Type())
esconPortIntervalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalIndex.setStatus(_A)
class _EsconPortIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_EsconPortIntervalNumber_Type.__name__=_E
_EsconPortIntervalNumber_Object=MibTableColumn
esconPortIntervalNumber=_EsconPortIntervalNumber_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,2),_EsconPortIntervalNumber_Type())
esconPortIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalNumber.setStatus(_A)
_EsconPortIntervalRxOctets_Type=Counter64
_EsconPortIntervalRxOctets_Object=MibTableColumn
esconPortIntervalRxOctets=_EsconPortIntervalRxOctets_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,3),_EsconPortIntervalRxOctets_Type())
esconPortIntervalRxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalRxOctets.setStatus(_A)
_EsconPortIntervalRxPkts_Type=Counter64
_EsconPortIntervalRxPkts_Object=MibTableColumn
esconPortIntervalRxPkts=_EsconPortIntervalRxPkts_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,4),_EsconPortIntervalRxPkts_Type())
esconPortIntervalRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalRxPkts.setStatus(_A)
_EsconPortIntervalRxSigLosses_Type=Counter64
_EsconPortIntervalRxSigLosses_Object=MibTableColumn
esconPortIntervalRxSigLosses=_EsconPortIntervalRxSigLosses_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,5),_EsconPortIntervalRxSigLosses_Type())
esconPortIntervalRxSigLosses.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalRxSigLosses.setStatus(_A)
_EsconPortIntervalRxSyncLosses_Type=Counter64
_EsconPortIntervalRxSyncLosses_Object=MibTableColumn
esconPortIntervalRxSyncLosses=_EsconPortIntervalRxSyncLosses_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,6),_EsconPortIntervalRxSyncLosses_Type())
esconPortIntervalRxSyncLosses.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalRxSyncLosses.setStatus(_A)
_EsconPortIntervalRxLinkFailures_Type=Counter64
_EsconPortIntervalRxLinkFailures_Object=MibTableColumn
esconPortIntervalRxLinkFailures=_EsconPortIntervalRxLinkFailures_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,7),_EsconPortIntervalRxLinkFailures_Type())
esconPortIntervalRxLinkFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalRxLinkFailures.setStatus(_A)
_EsconPortIntervalRxInvalidCrcs_Type=Counter64
_EsconPortIntervalRxInvalidCrcs_Object=MibTableColumn
esconPortIntervalRxInvalidCrcs=_EsconPortIntervalRxInvalidCrcs_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,8),_EsconPortIntervalRxInvalidCrcs_Type())
esconPortIntervalRxInvalidCrcs.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalRxInvalidCrcs.setStatus(_A)
_EsconPortIntervalRxDelimiterErrors_Type=Counter64
_EsconPortIntervalRxDelimiterErrors_Object=MibTableColumn
esconPortIntervalRxDelimiterErrors=_EsconPortIntervalRxDelimiterErrors_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,9),_EsconPortIntervalRxDelimiterErrors_Type())
esconPortIntervalRxDelimiterErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalRxDelimiterErrors.setStatus(_A)
_EsconPortIntervalRxDisparityErrors_Type=Counter64
_EsconPortIntervalRxDisparityErrors_Object=MibTableColumn
esconPortIntervalRxDisparityErrors=_EsconPortIntervalRxDisparityErrors_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,10),_EsconPortIntervalRxDisparityErrors_Type())
esconPortIntervalRxDisparityErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalRxDisparityErrors.setStatus(_A)
_EsconPortIntervalRxSizeFrames_Type=Counter64
_EsconPortIntervalRxSizeFrames_Object=MibTableColumn
esconPortIntervalRxSizeFrames=_EsconPortIntervalRxSizeFrames_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,11),_EsconPortIntervalRxSizeFrames_Type())
esconPortIntervalRxSizeFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalRxSizeFrames.setStatus(_A)
_EsconPortIntervalRxInvalidTxWords_Type=Counter64
_EsconPortIntervalRxInvalidTxWords_Object=MibTableColumn
esconPortIntervalRxInvalidTxWords=_EsconPortIntervalRxInvalidTxWords_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,12),_EsconPortIntervalRxInvalidTxWords_Type())
esconPortIntervalRxInvalidTxWords.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalRxInvalidTxWords.setStatus(_A)
_EsconPortIntervalTxOctets_Type=Counter64
_EsconPortIntervalTxOctets_Object=MibTableColumn
esconPortIntervalTxOctets=_EsconPortIntervalTxOctets_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,13),_EsconPortIntervalTxOctets_Type())
esconPortIntervalTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalTxOctets.setStatus(_A)
_EsconPortIntervalTxPkts_Type=Counter64
_EsconPortIntervalTxPkts_Object=MibTableColumn
esconPortIntervalTxPkts=_EsconPortIntervalTxPkts_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,14),_EsconPortIntervalTxPkts_Type())
esconPortIntervalTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalTxPkts.setStatus(_A)
_EsconPortIntervalTxHeaderError_Type=Counter64
_EsconPortIntervalTxHeaderError_Object=MibTableColumn
esconPortIntervalTxHeaderError=_EsconPortIntervalTxHeaderError_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,15),_EsconPortIntervalTxHeaderError_Type())
esconPortIntervalTxHeaderError.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalTxHeaderError.setStatus(_A)
_EsconPortIntervalTxJitterUnderflow_Type=Counter64
_EsconPortIntervalTxJitterUnderflow_Object=MibTableColumn
esconPortIntervalTxJitterUnderflow=_EsconPortIntervalTxJitterUnderflow_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,16),_EsconPortIntervalTxJitterUnderflow_Type())
esconPortIntervalTxJitterUnderflow.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalTxJitterUnderflow.setStatus(_A)
_EsconPortIntervalValidData_Type=TruthValue
_EsconPortIntervalValidData_Object=MibTableColumn
esconPortIntervalValidData=_EsconPortIntervalValidData_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,17),_EsconPortIntervalValidData_Type())
esconPortIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalValidData.setStatus(_A)
_EsconPortIntervalTcaFlag_Type=TruthValue
_EsconPortIntervalTcaFlag_Object=MibTableColumn
esconPortIntervalTcaFlag=_EsconPortIntervalTcaFlag_Object((1,3,6,1,4,1,4515,1,1,5,1,2,2,1,18),_EsconPortIntervalTcaFlag_Type())
esconPortIntervalTcaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalTcaFlag.setStatus(_A)
_EsconPortTotalTable_Object=MibTable
esconPortTotalTable=_EsconPortTotalTable_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3))
if mibBuilder.loadTexts:esconPortTotalTable.setStatus(_A)
_EsconPortTotalEntry_Object=MibTableRow
esconPortTotalEntry=_EsconPortTotalEntry_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1))
esconPortTotalEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:esconPortTotalEntry.setStatus(_A)
_EsconPortTotalIndex_Type=InterfaceIndex
_EsconPortTotalIndex_Object=MibTableColumn
esconPortTotalIndex=_EsconPortTotalIndex_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,1),_EsconPortTotalIndex_Type())
esconPortTotalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalIndex.setStatus(_A)
class _EsconPortTotalDayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,33))
_EsconPortTotalDayNumber_Type.__name__=_E
_EsconPortTotalDayNumber_Object=MibTableColumn
esconPortTotalDayNumber=_EsconPortTotalDayNumber_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,2),_EsconPortTotalDayNumber_Type())
esconPortTotalDayNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:esconPortTotalDayNumber.setStatus(_A)
_EsconPortTotalRxOctets_Type=Counter64
_EsconPortTotalRxOctets_Object=MibTableColumn
esconPortTotalRxOctets=_EsconPortTotalRxOctets_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,3),_EsconPortTotalRxOctets_Type())
esconPortTotalRxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalRxOctets.setStatus(_A)
_EsconPortTotalRxPkts_Type=Counter64
_EsconPortTotalRxPkts_Object=MibTableColumn
esconPortTotalRxPkts=_EsconPortTotalRxPkts_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,4),_EsconPortTotalRxPkts_Type())
esconPortTotalRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalRxPkts.setStatus(_A)
_EsconPortTotalRxSigLosses_Type=Counter64
_EsconPortTotalRxSigLosses_Object=MibTableColumn
esconPortTotalRxSigLosses=_EsconPortTotalRxSigLosses_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,5),_EsconPortTotalRxSigLosses_Type())
esconPortTotalRxSigLosses.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalRxSigLosses.setStatus(_A)
_EsconPortTotalRxSyncLosses_Type=Counter64
_EsconPortTotalRxSyncLosses_Object=MibTableColumn
esconPortTotalRxSyncLosses=_EsconPortTotalRxSyncLosses_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,6),_EsconPortTotalRxSyncLosses_Type())
esconPortTotalRxSyncLosses.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalRxSyncLosses.setStatus(_A)
_EsconPortTotalRxLinkFailures_Type=Counter64
_EsconPortTotalRxLinkFailures_Object=MibTableColumn
esconPortTotalRxLinkFailures=_EsconPortTotalRxLinkFailures_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,7),_EsconPortTotalRxLinkFailures_Type())
esconPortTotalRxLinkFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalRxLinkFailures.setStatus(_A)
_EsconPortTotalRxInvalidCrcs_Type=Counter64
_EsconPortTotalRxInvalidCrcs_Object=MibTableColumn
esconPortTotalRxInvalidCrcs=_EsconPortTotalRxInvalidCrcs_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,8),_EsconPortTotalRxInvalidCrcs_Type())
esconPortTotalRxInvalidCrcs.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalRxInvalidCrcs.setStatus(_A)
_EsconPortTotalRxDelimiterErrors_Type=Counter64
_EsconPortTotalRxDelimiterErrors_Object=MibTableColumn
esconPortTotalRxDelimiterErrors=_EsconPortTotalRxDelimiterErrors_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,9),_EsconPortTotalRxDelimiterErrors_Type())
esconPortTotalRxDelimiterErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalRxDelimiterErrors.setStatus(_A)
_EsconPortTotalRxDisparityErrors_Type=Counter64
_EsconPortTotalRxDisparityErrors_Object=MibTableColumn
esconPortTotalRxDisparityErrors=_EsconPortTotalRxDisparityErrors_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,10),_EsconPortTotalRxDisparityErrors_Type())
esconPortTotalRxDisparityErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalRxDisparityErrors.setStatus(_A)
_EsconPortTotalRxSizeFrames_Type=Counter64
_EsconPortTotalRxSizeFrames_Object=MibTableColumn
esconPortTotalRxSizeFrames=_EsconPortTotalRxSizeFrames_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,11),_EsconPortTotalRxSizeFrames_Type())
esconPortTotalRxSizeFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalRxSizeFrames.setStatus(_A)
_EsconPortTotalRxInvalidTxWords_Type=Counter64
_EsconPortTotalRxInvalidTxWords_Object=MibTableColumn
esconPortTotalRxInvalidTxWords=_EsconPortTotalRxInvalidTxWords_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,12),_EsconPortTotalRxInvalidTxWords_Type())
esconPortTotalRxInvalidTxWords.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalRxInvalidTxWords.setStatus(_A)
_EsconPortTotalTxOctets_Type=Counter64
_EsconPortTotalTxOctets_Object=MibTableColumn
esconPortTotalTxOctets=_EsconPortTotalTxOctets_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,13),_EsconPortTotalTxOctets_Type())
esconPortTotalTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalTxOctets.setStatus(_A)
_EsconPortTotalTxPkts_Type=Counter64
_EsconPortTotalTxPkts_Object=MibTableColumn
esconPortTotalTxPkts=_EsconPortTotalTxPkts_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,14),_EsconPortTotalTxPkts_Type())
esconPortTotalTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalTxPkts.setStatus(_A)
_EsconPortTotalTxHeaderError_Type=Counter64
_EsconPortTotalTxHeaderError_Object=MibTableColumn
esconPortTotalTxHeaderError=_EsconPortTotalTxHeaderError_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,15),_EsconPortTotalTxHeaderError_Type())
esconPortTotalTxHeaderError.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalTxHeaderError.setStatus(_A)
_EsconPortTotalTxJitterUnderflow_Type=Counter64
_EsconPortTotalTxJitterUnderflow_Object=MibTableColumn
esconPortTotalTxJitterUnderflow=_EsconPortTotalTxJitterUnderflow_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,16),_EsconPortTotalTxJitterUnderflow_Type())
esconPortTotalTxJitterUnderflow.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalTxJitterUnderflow.setStatus(_A)
_EsconPortTotalValidData_Type=TruthValue
_EsconPortTotalValidData_Object=MibTableColumn
esconPortTotalValidData=_EsconPortTotalValidData_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,17),_EsconPortTotalValidData_Type())
esconPortTotalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalValidData.setStatus(_A)
_EsconPortTotalTcaFlag_Type=TruthValue
_EsconPortTotalTcaFlag_Object=MibTableColumn
esconPortTotalTcaFlag=_EsconPortTotalTcaFlag_Object((1,3,6,1,4,1,4515,1,1,5,1,2,3,1,18),_EsconPortTotalTcaFlag_Type())
esconPortTotalTcaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortTotalTcaFlag.setStatus(_A)
_EsconPortIntervalThresholdTable_Object=MibTable
esconPortIntervalThresholdTable=_EsconPortIntervalThresholdTable_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4))
if mibBuilder.loadTexts:esconPortIntervalThresholdTable.setStatus(_A)
_EsconPortIntervalThresholdEntry_Object=MibTableRow
esconPortIntervalThresholdEntry=_EsconPortIntervalThresholdEntry_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1))
esconPortIntervalThresholdEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:esconPortIntervalThresholdEntry.setStatus(_A)
_EsconPortIntervalThresholdIndex_Type=InterfaceIndex
_EsconPortIntervalThresholdIndex_Object=MibTableColumn
esconPortIntervalThresholdIndex=_EsconPortIntervalThresholdIndex_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1,1),_EsconPortIntervalThresholdIndex_Type())
esconPortIntervalThresholdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortIntervalThresholdIndex.setStatus(_A)
_EsconPortIntervalThresholdRxSigLosses_Type=Counter64
_EsconPortIntervalThresholdRxSigLosses_Object=MibTableColumn
esconPortIntervalThresholdRxSigLosses=_EsconPortIntervalThresholdRxSigLosses_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1,2),_EsconPortIntervalThresholdRxSigLosses_Type())
esconPortIntervalThresholdRxSigLosses.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortIntervalThresholdRxSigLosses.setStatus(_A)
_EsconPortIntervalThresholdRxSyncLosses_Type=Counter64
_EsconPortIntervalThresholdRxSyncLosses_Object=MibTableColumn
esconPortIntervalThresholdRxSyncLosses=_EsconPortIntervalThresholdRxSyncLosses_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1,3),_EsconPortIntervalThresholdRxSyncLosses_Type())
esconPortIntervalThresholdRxSyncLosses.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortIntervalThresholdRxSyncLosses.setStatus(_A)
_EsconPortIntervalThresholdRxLinkFailures_Type=Counter64
_EsconPortIntervalThresholdRxLinkFailures_Object=MibTableColumn
esconPortIntervalThresholdRxLinkFailures=_EsconPortIntervalThresholdRxLinkFailures_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1,4),_EsconPortIntervalThresholdRxLinkFailures_Type())
esconPortIntervalThresholdRxLinkFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortIntervalThresholdRxLinkFailures.setStatus(_A)
_EsconPortIntervalThresholdRxInvalidCrcs_Type=Counter64
_EsconPortIntervalThresholdRxInvalidCrcs_Object=MibTableColumn
esconPortIntervalThresholdRxInvalidCrcs=_EsconPortIntervalThresholdRxInvalidCrcs_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1,5),_EsconPortIntervalThresholdRxInvalidCrcs_Type())
esconPortIntervalThresholdRxInvalidCrcs.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortIntervalThresholdRxInvalidCrcs.setStatus(_A)
_EsconPortIntervalThresholdRxDelimiterErrors_Type=Counter64
_EsconPortIntervalThresholdRxDelimiterErrors_Object=MibTableColumn
esconPortIntervalThresholdRxDelimiterErrors=_EsconPortIntervalThresholdRxDelimiterErrors_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1,6),_EsconPortIntervalThresholdRxDelimiterErrors_Type())
esconPortIntervalThresholdRxDelimiterErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortIntervalThresholdRxDelimiterErrors.setStatus(_A)
_EsconPortIntervalThresholdRxDisparityErrors_Type=Counter64
_EsconPortIntervalThresholdRxDisparityErrors_Object=MibTableColumn
esconPortIntervalThresholdRxDisparityErrors=_EsconPortIntervalThresholdRxDisparityErrors_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1,7),_EsconPortIntervalThresholdRxDisparityErrors_Type())
esconPortIntervalThresholdRxDisparityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortIntervalThresholdRxDisparityErrors.setStatus(_A)
_EsconPortIntervalThresholdRxSizeFrames_Type=Counter64
_EsconPortIntervalThresholdRxSizeFrames_Object=MibTableColumn
esconPortIntervalThresholdRxSizeFrames=_EsconPortIntervalThresholdRxSizeFrames_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1,8),_EsconPortIntervalThresholdRxSizeFrames_Type())
esconPortIntervalThresholdRxSizeFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortIntervalThresholdRxSizeFrames.setStatus(_A)
_EsconPortIntervalThresholdRxInvalidTxWords_Type=Counter64
_EsconPortIntervalThresholdRxInvalidTxWords_Object=MibTableColumn
esconPortIntervalThresholdRxInvalidTxWords=_EsconPortIntervalThresholdRxInvalidTxWords_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1,9),_EsconPortIntervalThresholdRxInvalidTxWords_Type())
esconPortIntervalThresholdRxInvalidTxWords.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortIntervalThresholdRxInvalidTxWords.setStatus(_A)
_EsconPortIntervalThresholdTxHeaderError_Type=Counter64
_EsconPortIntervalThresholdTxHeaderError_Object=MibTableColumn
esconPortIntervalThresholdTxHeaderError=_EsconPortIntervalThresholdTxHeaderError_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1,10),_EsconPortIntervalThresholdTxHeaderError_Type())
esconPortIntervalThresholdTxHeaderError.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortIntervalThresholdTxHeaderError.setStatus(_A)
_EsconPortIntervalThresholdTxJitterUnderflow_Type=Counter64
_EsconPortIntervalThresholdTxJitterUnderflow_Object=MibTableColumn
esconPortIntervalThresholdTxJitterUnderflow=_EsconPortIntervalThresholdTxJitterUnderflow_Object((1,3,6,1,4,1,4515,1,1,5,1,2,4,1,11),_EsconPortIntervalThresholdTxJitterUnderflow_Type())
esconPortIntervalThresholdTxJitterUnderflow.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortIntervalThresholdTxJitterUnderflow.setStatus(_A)
_EsconPortDayThresholdTable_Object=MibTable
esconPortDayThresholdTable=_EsconPortDayThresholdTable_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5))
if mibBuilder.loadTexts:esconPortDayThresholdTable.setStatus(_A)
_EsconPortDayThresholdEntry_Object=MibTableRow
esconPortDayThresholdEntry=_EsconPortDayThresholdEntry_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1))
esconPortDayThresholdEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:esconPortDayThresholdEntry.setStatus(_A)
_EsconPortDayThresholdIndex_Type=InterfaceIndex
_EsconPortDayThresholdIndex_Object=MibTableColumn
esconPortDayThresholdIndex=_EsconPortDayThresholdIndex_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1,1),_EsconPortDayThresholdIndex_Type())
esconPortDayThresholdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortDayThresholdIndex.setStatus(_A)
_EsconPortDayThresholdRxSigLosses_Type=Counter64
_EsconPortDayThresholdRxSigLosses_Object=MibTableColumn
esconPortDayThresholdRxSigLosses=_EsconPortDayThresholdRxSigLosses_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1,2),_EsconPortDayThresholdRxSigLosses_Type())
esconPortDayThresholdRxSigLosses.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortDayThresholdRxSigLosses.setStatus(_A)
_EsconPortDayThresholdRxSyncLosses_Type=Counter64
_EsconPortDayThresholdRxSyncLosses_Object=MibTableColumn
esconPortDayThresholdRxSyncLosses=_EsconPortDayThresholdRxSyncLosses_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1,3),_EsconPortDayThresholdRxSyncLosses_Type())
esconPortDayThresholdRxSyncLosses.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortDayThresholdRxSyncLosses.setStatus(_A)
_EsconPortDayThresholdRxLinkFailures_Type=Counter64
_EsconPortDayThresholdRxLinkFailures_Object=MibTableColumn
esconPortDayThresholdRxLinkFailures=_EsconPortDayThresholdRxLinkFailures_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1,4),_EsconPortDayThresholdRxLinkFailures_Type())
esconPortDayThresholdRxLinkFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortDayThresholdRxLinkFailures.setStatus(_A)
_EsconPortDayThresholdRxInvalidCrcs_Type=Counter64
_EsconPortDayThresholdRxInvalidCrcs_Object=MibTableColumn
esconPortDayThresholdRxInvalidCrcs=_EsconPortDayThresholdRxInvalidCrcs_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1,5),_EsconPortDayThresholdRxInvalidCrcs_Type())
esconPortDayThresholdRxInvalidCrcs.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortDayThresholdRxInvalidCrcs.setStatus(_A)
_EsconPortDayThresholdRxDelimiterErrors_Type=Counter64
_EsconPortDayThresholdRxDelimiterErrors_Object=MibTableColumn
esconPortDayThresholdRxDelimiterErrors=_EsconPortDayThresholdRxDelimiterErrors_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1,6),_EsconPortDayThresholdRxDelimiterErrors_Type())
esconPortDayThresholdRxDelimiterErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortDayThresholdRxDelimiterErrors.setStatus(_A)
_EsconPortDayThresholdRxDisparityErrors_Type=Counter64
_EsconPortDayThresholdRxDisparityErrors_Object=MibTableColumn
esconPortDayThresholdRxDisparityErrors=_EsconPortDayThresholdRxDisparityErrors_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1,7),_EsconPortDayThresholdRxDisparityErrors_Type())
esconPortDayThresholdRxDisparityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortDayThresholdRxDisparityErrors.setStatus(_A)
_EsconPortDayThresholdRxSizeFrames_Type=Counter64
_EsconPortDayThresholdRxSizeFrames_Object=MibTableColumn
esconPortDayThresholdRxSizeFrames=_EsconPortDayThresholdRxSizeFrames_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1,8),_EsconPortDayThresholdRxSizeFrames_Type())
esconPortDayThresholdRxSizeFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortDayThresholdRxSizeFrames.setStatus(_A)
_EsconPortDayThresholdRxInvalidTxWords_Type=Counter64
_EsconPortDayThresholdRxInvalidTxWords_Object=MibTableColumn
esconPortDayThresholdRxInvalidTxWords=_EsconPortDayThresholdRxInvalidTxWords_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1,9),_EsconPortDayThresholdRxInvalidTxWords_Type())
esconPortDayThresholdRxInvalidTxWords.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortDayThresholdRxInvalidTxWords.setStatus(_A)
_EsconPortDayThresholdTxHeaderError_Type=Counter64
_EsconPortDayThresholdTxHeaderError_Object=MibTableColumn
esconPortDayThresholdTxHeaderError=_EsconPortDayThresholdTxHeaderError_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1,10),_EsconPortDayThresholdTxHeaderError_Type())
esconPortDayThresholdTxHeaderError.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortDayThresholdTxHeaderError.setStatus(_A)
_EsconPortDayThresholdTxJitterUnderflow_Type=Counter64
_EsconPortDayThresholdTxJitterUnderflow_Object=MibTableColumn
esconPortDayThresholdTxJitterUnderflow=_EsconPortDayThresholdTxJitterUnderflow_Object((1,3,6,1,4,1,4515,1,1,5,1,2,5,1,11),_EsconPortDayThresholdTxJitterUnderflow_Type())
esconPortDayThresholdTxJitterUnderflow.setMaxAccess(_C)
if mibBuilder.loadTexts:esconPortDayThresholdTxJitterUnderflow.setStatus(_A)
_EsconTraps_ObjectIdentity=ObjectIdentity
esconTraps=_EsconTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,1,5,1,3))
_EsconCounterId_Type=ObjectIdentifier
_EsconCounterId_Object=MibScalar
esconCounterId=_EsconCounterId_Object((1,3,6,1,4,1,4515,1,1,5,1,3,1),_EsconCounterId_Type())
esconCounterId.setMaxAccess(_B)
if mibBuilder.loadTexts:esconCounterId.setStatus(_A)
_EsconCounterValue_Type=Counter64
_EsconCounterValue_Object=MibScalar
esconCounterValue=_EsconCounterValue_Object((1,3,6,1,4,1,4515,1,1,5,1,3,2),_EsconCounterValue_Type())
esconCounterValue.setMaxAccess(_B)
if mibBuilder.loadTexts:esconCounterValue.setStatus(_A)
esconPortThresholdCrossing=NotificationType((1,3,6,1,4,1,4515,1,1,5,1,3,3))
esconPortThresholdCrossing.setObjects(*((_D,_N),(_D,_O)))
if mibBuilder.loadTexts:esconPortThresholdCrossing.setStatus(_A)
esconPortStatusChange=NotificationType((1,3,6,1,4,1,4515,1,1,5,1,3,4))
esconPortStatusChange.setObjects(*((_D,_F),(_D,_P)))
if mibBuilder.loadTexts:esconPortStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'EsconAddressId':EsconAddressId,'EsconNodeDescription':EsconNodeDescription,'esconMIB':esconMIB,'esconMIBObjects':esconMIBObjects,'esconConfig':esconConfig,'esconPortConfigTable':esconPortConfigTable,'esconPortConfigEntry':esconPortConfigEntry,_F:esconPortConfigIndex,'esconPortConfigSrcAddress':esconPortConfigSrcAddress,'esconPortConfigSrcDescription':esconPortConfigSrcDescription,'esconPortConfigTranceiverMedia':esconPortConfigTranceiverMedia,'esconPortConfigResetPmCounters':esconPortConfigResetPmCounters,'esconPortConfigTranceiverType':esconPortConfigTranceiverType,_P:esconPortConfigStatus,'esconPortConfigValidIntervals':esconPortConfigValidIntervals,'esconPortConfigLoginState':esconPortConfigLoginState,'esconPortResetPmCounters':esconPortResetPmCounters,'esconPm':esconPm,'esconPortCurrentTable':esconPortCurrentTable,'esconPortCurrentEntry':esconPortCurrentEntry,_G:esconPortCurrentIndex,'esconPortCurrentRxOctets':esconPortCurrentRxOctets,'esconPortCurrentRxPkts':esconPortCurrentRxPkts,'esconPortCurrentRxSigLosses':esconPortCurrentRxSigLosses,'esconPortCurrentRxSyncLosses':esconPortCurrentRxSyncLosses,'esconPortCurrentRxLinkFailures':esconPortCurrentRxLinkFailures,'esconPortCurrentRxInvalidCrcs':esconPortCurrentRxInvalidCrcs,'esconPortCurrentRxDelimiterErrors':esconPortCurrentRxDelimiterErrors,'esconPortCurrentRxDisparityErrors':esconPortCurrentRxDisparityErrors,'esconPortCurrentRxSizeFrames':esconPortCurrentRxSizeFrames,'esconPortCurrentRxInvalidTxWords':esconPortCurrentRxInvalidTxWords,'esconPortCurrentTxOctets':esconPortCurrentTxOctets,'esconPortCurrentTxPkts':esconPortCurrentTxPkts,'esconPortCurrentTxHeaderError':esconPortCurrentTxHeaderError,'esconPortCurrentTxJitterUnderflow':esconPortCurrentTxJitterUnderflow,'esconPortIntervalTable':esconPortIntervalTable,'esconPortIntervalEntry':esconPortIntervalEntry,_H:esconPortIntervalIndex,_I:esconPortIntervalNumber,'esconPortIntervalRxOctets':esconPortIntervalRxOctets,'esconPortIntervalRxPkts':esconPortIntervalRxPkts,'esconPortIntervalRxSigLosses':esconPortIntervalRxSigLosses,'esconPortIntervalRxSyncLosses':esconPortIntervalRxSyncLosses,'esconPortIntervalRxLinkFailures':esconPortIntervalRxLinkFailures,'esconPortIntervalRxInvalidCrcs':esconPortIntervalRxInvalidCrcs,'esconPortIntervalRxDelimiterErrors':esconPortIntervalRxDelimiterErrors,'esconPortIntervalRxDisparityErrors':esconPortIntervalRxDisparityErrors,'esconPortIntervalRxSizeFrames':esconPortIntervalRxSizeFrames,'esconPortIntervalRxInvalidTxWords':esconPortIntervalRxInvalidTxWords,'esconPortIntervalTxOctets':esconPortIntervalTxOctets,'esconPortIntervalTxPkts':esconPortIntervalTxPkts,'esconPortIntervalTxHeaderError':esconPortIntervalTxHeaderError,'esconPortIntervalTxJitterUnderflow':esconPortIntervalTxJitterUnderflow,'esconPortIntervalValidData':esconPortIntervalValidData,'esconPortIntervalTcaFlag':esconPortIntervalTcaFlag,'esconPortTotalTable':esconPortTotalTable,'esconPortTotalEntry':esconPortTotalEntry,_J:esconPortTotalIndex,_K:esconPortTotalDayNumber,'esconPortTotalRxOctets':esconPortTotalRxOctets,'esconPortTotalRxPkts':esconPortTotalRxPkts,'esconPortTotalRxSigLosses':esconPortTotalRxSigLosses,'esconPortTotalRxSyncLosses':esconPortTotalRxSyncLosses,'esconPortTotalRxLinkFailures':esconPortTotalRxLinkFailures,'esconPortTotalRxInvalidCrcs':esconPortTotalRxInvalidCrcs,'esconPortTotalRxDelimiterErrors':esconPortTotalRxDelimiterErrors,'esconPortTotalRxDisparityErrors':esconPortTotalRxDisparityErrors,'esconPortTotalRxSizeFrames':esconPortTotalRxSizeFrames,'esconPortTotalRxInvalidTxWords':esconPortTotalRxInvalidTxWords,'esconPortTotalTxOctets':esconPortTotalTxOctets,'esconPortTotalTxPkts':esconPortTotalTxPkts,'esconPortTotalTxHeaderError':esconPortTotalTxHeaderError,'esconPortTotalTxJitterUnderflow':esconPortTotalTxJitterUnderflow,'esconPortTotalValidData':esconPortTotalValidData,'esconPortTotalTcaFlag':esconPortTotalTcaFlag,'esconPortIntervalThresholdTable':esconPortIntervalThresholdTable,'esconPortIntervalThresholdEntry':esconPortIntervalThresholdEntry,_L:esconPortIntervalThresholdIndex,'esconPortIntervalThresholdRxSigLosses':esconPortIntervalThresholdRxSigLosses,'esconPortIntervalThresholdRxSyncLosses':esconPortIntervalThresholdRxSyncLosses,'esconPortIntervalThresholdRxLinkFailures':esconPortIntervalThresholdRxLinkFailures,'esconPortIntervalThresholdRxInvalidCrcs':esconPortIntervalThresholdRxInvalidCrcs,'esconPortIntervalThresholdRxDelimiterErrors':esconPortIntervalThresholdRxDelimiterErrors,'esconPortIntervalThresholdRxDisparityErrors':esconPortIntervalThresholdRxDisparityErrors,'esconPortIntervalThresholdRxSizeFrames':esconPortIntervalThresholdRxSizeFrames,'esconPortIntervalThresholdRxInvalidTxWords':esconPortIntervalThresholdRxInvalidTxWords,'esconPortIntervalThresholdTxHeaderError':esconPortIntervalThresholdTxHeaderError,'esconPortIntervalThresholdTxJitterUnderflow':esconPortIntervalThresholdTxJitterUnderflow,'esconPortDayThresholdTable':esconPortDayThresholdTable,'esconPortDayThresholdEntry':esconPortDayThresholdEntry,_M:esconPortDayThresholdIndex,'esconPortDayThresholdRxSigLosses':esconPortDayThresholdRxSigLosses,'esconPortDayThresholdRxSyncLosses':esconPortDayThresholdRxSyncLosses,'esconPortDayThresholdRxLinkFailures':esconPortDayThresholdRxLinkFailures,'esconPortDayThresholdRxInvalidCrcs':esconPortDayThresholdRxInvalidCrcs,'esconPortDayThresholdRxDelimiterErrors':esconPortDayThresholdRxDelimiterErrors,'esconPortDayThresholdRxDisparityErrors':esconPortDayThresholdRxDisparityErrors,'esconPortDayThresholdRxSizeFrames':esconPortDayThresholdRxSizeFrames,'esconPortDayThresholdRxInvalidTxWords':esconPortDayThresholdRxInvalidTxWords,'esconPortDayThresholdTxHeaderError':esconPortDayThresholdTxHeaderError,'esconPortDayThresholdTxJitterUnderflow':esconPortDayThresholdTxJitterUnderflow,'esconTraps':esconTraps,_N:esconCounterId,_O:esconCounterValue,'esconPortThresholdCrossing':esconPortThresholdCrossing,'esconPortStatusChange':esconPortStatusChange})