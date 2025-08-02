_u='ciscoAtmSwitchServcHostGroup2'
_t='ciscoatmInterfaceCurrentMinSvccVci'
_s='ciscoatmInterfaceConfMinSvccVci'
_r='ciscoatmInterfaceCurrentMaxSvccVpi'
_q='ciscoatmInterfaceConfMaxSvccVpi'
_p='ciscoatmInterfaceCurrentMaxSvpcVpi'
_o='ciscoatmInterfaceConfMaxSvpcVpi'
_n='ciscoatmSigSupportUnknownIe'
_m='ciscoatmSigSupportAALInfo'
_l='ciscoatmSigSupportBlliRepeatInd'
_k='ciscoatmSigSupportLoLyrInfo'
_j='ciscoatmSigSupportHiLyrInfo'
_i='ciscoatmSigSupportCldPtySubAddr'
_h='ciscoatmSigSupportClgPtySubAddr'
_g='ciscoatmSigSupportClgPtyNumDel'
_f='ciscoatmSigOutEstabls'
_e='ciscoatmSigInEstabls'
_d='ciscoatmSigEmitRestarts'
_c='ciscoatmSigDetectRestarts'
_b='ciscoatmSigEmitTimerExpireds'
_a='ciscoatmSigDetectTimerExpireds'
_Z='ciscoatmSigEmitClgPtyEvents'
_Y='ciscoatmSigDetectClgPtyEvents'
_X='ciscoatmSigEmitMsgErrors'
_W='ciscoatmSigDetectMsgErrors'
_V='ciscoatmSigEmitCldPtyEvents'
_U='ciscoatmSigDetectCldPtyEvents'
_T='ciscoatmSigEmitUnavailResrcs'
_S='ciscoatmSigDetectUnavailResrcs'
_R='ciscoatmSigEmitUnavailRoutes'
_Q='ciscoatmSigDetectUnavailRoutes'
_P='ciscoatmSigEmitSetupAttempts'
_O='ciscoatmSigDetectSetupAttempts'
_N='ciscoatmSigSSCOPErrdPdus'
_M='ciscoatmSigSSCOPConEvents'
_L='ciscoatmInterfaceExtEntry'
_K='ciscoAtmSwitchServcGroup'
_J='ciscoAtmSwitchServcHostGroup'
_I='ifIndex'
_H='IF-MIB'
_G='disabled'
_F='enabled'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-ATM2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmInterfaceConfEntry,=mibBuilder.importSymbols('ATM-MIB','atmInterfaceConfEntry')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoAtm2MIB=ModuleIdentity((1,3,6,1,4,1,9,10,23))
if mibBuilder.loadTexts:ciscoAtm2MIB.setRevisions(('1998-03-04 00:00',))
_Ciscoatm2MIBObjects_ObjectIdentity=ObjectIdentity
ciscoatm2MIBObjects=_Ciscoatm2MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,23,1))
_CiscoatmSigStatTable_Object=MibTable
ciscoatmSigStatTable=_CiscoatmSigStatTable_Object((1,3,6,1,4,1,9,10,23,1,1))
if mibBuilder.loadTexts:ciscoatmSigStatTable.setStatus(_A)
_CiscoatmSigStatEntry_Object=MibTableRow
ciscoatmSigStatEntry=_CiscoatmSigStatEntry_Object((1,3,6,1,4,1,9,10,23,1,1,1))
ciscoatmSigStatEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:ciscoatmSigStatEntry.setStatus(_A)
_CiscoatmSigSSCOPConEvents_Type=Counter32
_CiscoatmSigSSCOPConEvents_Object=MibTableColumn
ciscoatmSigSSCOPConEvents=_CiscoatmSigSSCOPConEvents_Object((1,3,6,1,4,1,9,10,23,1,1,1,5),_CiscoatmSigSSCOPConEvents_Type())
ciscoatmSigSSCOPConEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigSSCOPConEvents.setStatus(_A)
_CiscoatmSigSSCOPErrdPdus_Type=Counter32
_CiscoatmSigSSCOPErrdPdus_Object=MibTableColumn
ciscoatmSigSSCOPErrdPdus=_CiscoatmSigSSCOPErrdPdus_Object((1,3,6,1,4,1,9,10,23,1,1,1,6),_CiscoatmSigSSCOPErrdPdus_Type())
ciscoatmSigSSCOPErrdPdus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigSSCOPErrdPdus.setStatus(_A)
_CiscoatmSigDetectSetupAttempts_Type=Counter32
_CiscoatmSigDetectSetupAttempts_Object=MibTableColumn
ciscoatmSigDetectSetupAttempts=_CiscoatmSigDetectSetupAttempts_Object((1,3,6,1,4,1,9,10,23,1,1,1,7),_CiscoatmSigDetectSetupAttempts_Type())
ciscoatmSigDetectSetupAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigDetectSetupAttempts.setStatus(_A)
_CiscoatmSigEmitSetupAttempts_Type=Counter32
_CiscoatmSigEmitSetupAttempts_Object=MibTableColumn
ciscoatmSigEmitSetupAttempts=_CiscoatmSigEmitSetupAttempts_Object((1,3,6,1,4,1,9,10,23,1,1,1,8),_CiscoatmSigEmitSetupAttempts_Type())
ciscoatmSigEmitSetupAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigEmitSetupAttempts.setStatus(_A)
_CiscoatmSigDetectUnavailRoutes_Type=Counter32
_CiscoatmSigDetectUnavailRoutes_Object=MibTableColumn
ciscoatmSigDetectUnavailRoutes=_CiscoatmSigDetectUnavailRoutes_Object((1,3,6,1,4,1,9,10,23,1,1,1,9),_CiscoatmSigDetectUnavailRoutes_Type())
ciscoatmSigDetectUnavailRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigDetectUnavailRoutes.setStatus(_A)
_CiscoatmSigEmitUnavailRoutes_Type=Counter32
_CiscoatmSigEmitUnavailRoutes_Object=MibTableColumn
ciscoatmSigEmitUnavailRoutes=_CiscoatmSigEmitUnavailRoutes_Object((1,3,6,1,4,1,9,10,23,1,1,1,10),_CiscoatmSigEmitUnavailRoutes_Type())
ciscoatmSigEmitUnavailRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigEmitUnavailRoutes.setStatus(_A)
_CiscoatmSigDetectUnavailResrcs_Type=Counter32
_CiscoatmSigDetectUnavailResrcs_Object=MibTableColumn
ciscoatmSigDetectUnavailResrcs=_CiscoatmSigDetectUnavailResrcs_Object((1,3,6,1,4,1,9,10,23,1,1,1,11),_CiscoatmSigDetectUnavailResrcs_Type())
ciscoatmSigDetectUnavailResrcs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigDetectUnavailResrcs.setStatus(_A)
_CiscoatmSigEmitUnavailResrcs_Type=Counter32
_CiscoatmSigEmitUnavailResrcs_Object=MibTableColumn
ciscoatmSigEmitUnavailResrcs=_CiscoatmSigEmitUnavailResrcs_Object((1,3,6,1,4,1,9,10,23,1,1,1,12),_CiscoatmSigEmitUnavailResrcs_Type())
ciscoatmSigEmitUnavailResrcs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigEmitUnavailResrcs.setStatus(_A)
_CiscoatmSigDetectCldPtyEvents_Type=Counter32
_CiscoatmSigDetectCldPtyEvents_Object=MibTableColumn
ciscoatmSigDetectCldPtyEvents=_CiscoatmSigDetectCldPtyEvents_Object((1,3,6,1,4,1,9,10,23,1,1,1,13),_CiscoatmSigDetectCldPtyEvents_Type())
ciscoatmSigDetectCldPtyEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigDetectCldPtyEvents.setStatus(_A)
_CiscoatmSigEmitCldPtyEvents_Type=Counter32
_CiscoatmSigEmitCldPtyEvents_Object=MibTableColumn
ciscoatmSigEmitCldPtyEvents=_CiscoatmSigEmitCldPtyEvents_Object((1,3,6,1,4,1,9,10,23,1,1,1,14),_CiscoatmSigEmitCldPtyEvents_Type())
ciscoatmSigEmitCldPtyEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigEmitCldPtyEvents.setStatus(_A)
_CiscoatmSigDetectMsgErrors_Type=Counter32
_CiscoatmSigDetectMsgErrors_Object=MibTableColumn
ciscoatmSigDetectMsgErrors=_CiscoatmSigDetectMsgErrors_Object((1,3,6,1,4,1,9,10,23,1,1,1,15),_CiscoatmSigDetectMsgErrors_Type())
ciscoatmSigDetectMsgErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigDetectMsgErrors.setStatus(_A)
_CiscoatmSigEmitMsgErrors_Type=Counter32
_CiscoatmSigEmitMsgErrors_Object=MibTableColumn
ciscoatmSigEmitMsgErrors=_CiscoatmSigEmitMsgErrors_Object((1,3,6,1,4,1,9,10,23,1,1,1,16),_CiscoatmSigEmitMsgErrors_Type())
ciscoatmSigEmitMsgErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigEmitMsgErrors.setStatus(_A)
_CiscoatmSigDetectClgPtyEvents_Type=Counter32
_CiscoatmSigDetectClgPtyEvents_Object=MibTableColumn
ciscoatmSigDetectClgPtyEvents=_CiscoatmSigDetectClgPtyEvents_Object((1,3,6,1,4,1,9,10,23,1,1,1,17),_CiscoatmSigDetectClgPtyEvents_Type())
ciscoatmSigDetectClgPtyEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigDetectClgPtyEvents.setStatus(_A)
_CiscoatmSigEmitClgPtyEvents_Type=Counter32
_CiscoatmSigEmitClgPtyEvents_Object=MibTableColumn
ciscoatmSigEmitClgPtyEvents=_CiscoatmSigEmitClgPtyEvents_Object((1,3,6,1,4,1,9,10,23,1,1,1,18),_CiscoatmSigEmitClgPtyEvents_Type())
ciscoatmSigEmitClgPtyEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigEmitClgPtyEvents.setStatus(_A)
_CiscoatmSigDetectTimerExpireds_Type=Counter32
_CiscoatmSigDetectTimerExpireds_Object=MibTableColumn
ciscoatmSigDetectTimerExpireds=_CiscoatmSigDetectTimerExpireds_Object((1,3,6,1,4,1,9,10,23,1,1,1,19),_CiscoatmSigDetectTimerExpireds_Type())
ciscoatmSigDetectTimerExpireds.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigDetectTimerExpireds.setStatus(_A)
_CiscoatmSigEmitTimerExpireds_Type=Counter32
_CiscoatmSigEmitTimerExpireds_Object=MibTableColumn
ciscoatmSigEmitTimerExpireds=_CiscoatmSigEmitTimerExpireds_Object((1,3,6,1,4,1,9,10,23,1,1,1,20),_CiscoatmSigEmitTimerExpireds_Type())
ciscoatmSigEmitTimerExpireds.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigEmitTimerExpireds.setStatus(_A)
_CiscoatmSigDetectRestarts_Type=Counter32
_CiscoatmSigDetectRestarts_Object=MibTableColumn
ciscoatmSigDetectRestarts=_CiscoatmSigDetectRestarts_Object((1,3,6,1,4,1,9,10,23,1,1,1,21),_CiscoatmSigDetectRestarts_Type())
ciscoatmSigDetectRestarts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigDetectRestarts.setStatus(_A)
_CiscoatmSigEmitRestarts_Type=Counter32
_CiscoatmSigEmitRestarts_Object=MibTableColumn
ciscoatmSigEmitRestarts=_CiscoatmSigEmitRestarts_Object((1,3,6,1,4,1,9,10,23,1,1,1,22),_CiscoatmSigEmitRestarts_Type())
ciscoatmSigEmitRestarts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigEmitRestarts.setStatus(_A)
_CiscoatmSigInEstabls_Type=Counter32
_CiscoatmSigInEstabls_Object=MibTableColumn
ciscoatmSigInEstabls=_CiscoatmSigInEstabls_Object((1,3,6,1,4,1,9,10,23,1,1,1,23),_CiscoatmSigInEstabls_Type())
ciscoatmSigInEstabls.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigInEstabls.setStatus(_A)
_CiscoatmSigOutEstabls_Type=Counter32
_CiscoatmSigOutEstabls_Object=MibTableColumn
ciscoatmSigOutEstabls=_CiscoatmSigOutEstabls_Object((1,3,6,1,4,1,9,10,23,1,1,1,24),_CiscoatmSigOutEstabls_Type())
ciscoatmSigOutEstabls.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmSigOutEstabls.setStatus(_A)
_CiscoatmSigSupportTable_Object=MibTable
ciscoatmSigSupportTable=_CiscoatmSigSupportTable_Object((1,3,6,1,4,1,9,10,23,1,2))
if mibBuilder.loadTexts:ciscoatmSigSupportTable.setStatus(_A)
_CiscoatmSigSupportEntry_Object=MibTableRow
ciscoatmSigSupportEntry=_CiscoatmSigSupportEntry_Object((1,3,6,1,4,1,9,10,23,1,2,1))
ciscoatmSigSupportEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:ciscoatmSigSupportEntry.setStatus(_A)
class _CiscoatmSigSupportClgPtyNumDel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CiscoatmSigSupportClgPtyNumDel_Type.__name__=_D
_CiscoatmSigSupportClgPtyNumDel_Object=MibTableColumn
ciscoatmSigSupportClgPtyNumDel=_CiscoatmSigSupportClgPtyNumDel_Object((1,3,6,1,4,1,9,10,23,1,2,1,1),_CiscoatmSigSupportClgPtyNumDel_Type())
ciscoatmSigSupportClgPtyNumDel.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoatmSigSupportClgPtyNumDel.setStatus(_A)
class _CiscoatmSigSupportClgPtySubAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CiscoatmSigSupportClgPtySubAddr_Type.__name__=_D
_CiscoatmSigSupportClgPtySubAddr_Object=MibTableColumn
ciscoatmSigSupportClgPtySubAddr=_CiscoatmSigSupportClgPtySubAddr_Object((1,3,6,1,4,1,9,10,23,1,2,1,2),_CiscoatmSigSupportClgPtySubAddr_Type())
ciscoatmSigSupportClgPtySubAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoatmSigSupportClgPtySubAddr.setStatus(_A)
class _CiscoatmSigSupportCldPtySubAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CiscoatmSigSupportCldPtySubAddr_Type.__name__=_D
_CiscoatmSigSupportCldPtySubAddr_Object=MibTableColumn
ciscoatmSigSupportCldPtySubAddr=_CiscoatmSigSupportCldPtySubAddr_Object((1,3,6,1,4,1,9,10,23,1,2,1,3),_CiscoatmSigSupportCldPtySubAddr_Type())
ciscoatmSigSupportCldPtySubAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoatmSigSupportCldPtySubAddr.setStatus(_A)
class _CiscoatmSigSupportHiLyrInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CiscoatmSigSupportHiLyrInfo_Type.__name__=_D
_CiscoatmSigSupportHiLyrInfo_Object=MibTableColumn
ciscoatmSigSupportHiLyrInfo=_CiscoatmSigSupportHiLyrInfo_Object((1,3,6,1,4,1,9,10,23,1,2,1,4),_CiscoatmSigSupportHiLyrInfo_Type())
ciscoatmSigSupportHiLyrInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoatmSigSupportHiLyrInfo.setStatus(_A)
class _CiscoatmSigSupportLoLyrInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CiscoatmSigSupportLoLyrInfo_Type.__name__=_D
_CiscoatmSigSupportLoLyrInfo_Object=MibTableColumn
ciscoatmSigSupportLoLyrInfo=_CiscoatmSigSupportLoLyrInfo_Object((1,3,6,1,4,1,9,10,23,1,2,1,5),_CiscoatmSigSupportLoLyrInfo_Type())
ciscoatmSigSupportLoLyrInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoatmSigSupportLoLyrInfo.setStatus(_A)
class _CiscoatmSigSupportBlliRepeatInd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CiscoatmSigSupportBlliRepeatInd_Type.__name__=_D
_CiscoatmSigSupportBlliRepeatInd_Object=MibTableColumn
ciscoatmSigSupportBlliRepeatInd=_CiscoatmSigSupportBlliRepeatInd_Object((1,3,6,1,4,1,9,10,23,1,2,1,6),_CiscoatmSigSupportBlliRepeatInd_Type())
ciscoatmSigSupportBlliRepeatInd.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoatmSigSupportBlliRepeatInd.setStatus(_A)
class _CiscoatmSigSupportAALInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CiscoatmSigSupportAALInfo_Type.__name__=_D
_CiscoatmSigSupportAALInfo_Object=MibTableColumn
ciscoatmSigSupportAALInfo=_CiscoatmSigSupportAALInfo_Object((1,3,6,1,4,1,9,10,23,1,2,1,7),_CiscoatmSigSupportAALInfo_Type())
ciscoatmSigSupportAALInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoatmSigSupportAALInfo.setStatus(_A)
class _CiscoatmSigSupportUnknownIe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CiscoatmSigSupportUnknownIe_Type.__name__=_D
_CiscoatmSigSupportUnknownIe_Object=MibTableColumn
ciscoatmSigSupportUnknownIe=_CiscoatmSigSupportUnknownIe_Object((1,3,6,1,4,1,9,10,23,1,2,1,8),_CiscoatmSigSupportUnknownIe_Type())
ciscoatmSigSupportUnknownIe.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoatmSigSupportUnknownIe.setStatus(_A)
_CiscoatmInterfaceExtTable_Object=MibTable
ciscoatmInterfaceExtTable=_CiscoatmInterfaceExtTable_Object((1,3,6,1,4,1,9,10,23,1,3))
if mibBuilder.loadTexts:ciscoatmInterfaceExtTable.setStatus(_A)
_CiscoatmInterfaceExtEntry_Object=MibTableRow
ciscoatmInterfaceExtEntry=_CiscoatmInterfaceExtEntry_Object((1,3,6,1,4,1,9,10,23,1,3,1))
if mibBuilder.loadTexts:ciscoatmInterfaceExtEntry.setStatus(_A)
class _CiscoatmInterfaceConfMaxSvpcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoatmInterfaceConfMaxSvpcVpi_Type.__name__=_D
_CiscoatmInterfaceConfMaxSvpcVpi_Object=MibTableColumn
ciscoatmInterfaceConfMaxSvpcVpi=_CiscoatmInterfaceConfMaxSvpcVpi_Object((1,3,6,1,4,1,9,10,23,1,3,1,16),_CiscoatmInterfaceConfMaxSvpcVpi_Type())
ciscoatmInterfaceConfMaxSvpcVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoatmInterfaceConfMaxSvpcVpi.setStatus(_A)
class _CiscoatmInterfaceCurrentMaxSvpcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoatmInterfaceCurrentMaxSvpcVpi_Type.__name__=_D
_CiscoatmInterfaceCurrentMaxSvpcVpi_Object=MibTableColumn
ciscoatmInterfaceCurrentMaxSvpcVpi=_CiscoatmInterfaceCurrentMaxSvpcVpi_Object((1,3,6,1,4,1,9,10,23,1,3,1,17),_CiscoatmInterfaceCurrentMaxSvpcVpi_Type())
ciscoatmInterfaceCurrentMaxSvpcVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmInterfaceCurrentMaxSvpcVpi.setStatus(_A)
class _CiscoatmInterfaceConfMaxSvccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoatmInterfaceConfMaxSvccVpi_Type.__name__=_D
_CiscoatmInterfaceConfMaxSvccVpi_Object=MibTableColumn
ciscoatmInterfaceConfMaxSvccVpi=_CiscoatmInterfaceConfMaxSvccVpi_Object((1,3,6,1,4,1,9,10,23,1,3,1,18),_CiscoatmInterfaceConfMaxSvccVpi_Type())
ciscoatmInterfaceConfMaxSvccVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoatmInterfaceConfMaxSvccVpi.setStatus(_A)
class _CiscoatmInterfaceCurrentMaxSvccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoatmInterfaceCurrentMaxSvccVpi_Type.__name__=_D
_CiscoatmInterfaceCurrentMaxSvccVpi_Object=MibTableColumn
ciscoatmInterfaceCurrentMaxSvccVpi=_CiscoatmInterfaceCurrentMaxSvccVpi_Object((1,3,6,1,4,1,9,10,23,1,3,1,19),_CiscoatmInterfaceCurrentMaxSvccVpi_Type())
ciscoatmInterfaceCurrentMaxSvccVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmInterfaceCurrentMaxSvccVpi.setStatus(_A)
class _CiscoatmInterfaceConfMinSvccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,4095))
_CiscoatmInterfaceConfMinSvccVci_Type.__name__=_D
_CiscoatmInterfaceConfMinSvccVci_Object=MibTableColumn
ciscoatmInterfaceConfMinSvccVci=_CiscoatmInterfaceConfMinSvccVci_Object((1,3,6,1,4,1,9,10,23,1,3,1,20),_CiscoatmInterfaceConfMinSvccVci_Type())
ciscoatmInterfaceConfMinSvccVci.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoatmInterfaceConfMinSvccVci.setStatus(_A)
class _CiscoatmInterfaceCurrentMinSvccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,4095))
_CiscoatmInterfaceCurrentMinSvccVci_Type.__name__=_D
_CiscoatmInterfaceCurrentMinSvccVci_Object=MibTableColumn
ciscoatmInterfaceCurrentMinSvccVci=_CiscoatmInterfaceCurrentMinSvccVci_Object((1,3,6,1,4,1,9,10,23,1,3,1,21),_CiscoatmInterfaceCurrentMinSvccVci_Type())
ciscoatmInterfaceCurrentMinSvccVci.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoatmInterfaceCurrentMinSvccVci.setStatus(_A)
_Ciscoatm2MIBConformance_ObjectIdentity=ObjectIdentity
ciscoatm2MIBConformance=_Ciscoatm2MIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,23,3))
_Ciscoatm2MIBGroups_ObjectIdentity=ObjectIdentity
ciscoatm2MIBGroups=_Ciscoatm2MIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,23,3,1))
_Ciscoatm2MIBCompliances_ObjectIdentity=ObjectIdentity
ciscoatm2MIBCompliances=_Ciscoatm2MIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,23,3,2))
atmInterfaceConfEntry.registerAugmentions((_B,_L))
ciscoatmInterfaceExtEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
ciscoAtmSwitchServcHostGroup=ObjectGroup((1,3,6,1,4,1,9,10,23,3,1,1))
ciscoAtmSwitchServcHostGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ciscoAtmSwitchServcHostGroup.setStatus(_A)
ciscoAtmSwitchServcGroup=ObjectGroup((1,3,6,1,4,1,9,10,23,3,1,3))
ciscoAtmSwitchServcGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ciscoAtmSwitchServcGroup.setStatus(_A)
ciscoAtmSwitchServcHostGroup2=ObjectGroup((1,3,6,1,4,1,9,10,23,3,1,4))
ciscoAtmSwitchServcHostGroup2.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:ciscoAtmSwitchServcHostGroup2.setStatus(_A)
ciscoatm2MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,23,3,2,1))
ciscoatm2MIBCompliance.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoatm2MIBCompliance.setStatus('obsolete')
ciscoatm2MIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,10,23,3,2,2))
ciscoatm2MIBCompliance2.setObjects(*((_B,_J),(_B,_u),(_B,_K)))
if mibBuilder.loadTexts:ciscoatm2MIBCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoAtm2MIB':ciscoAtm2MIB,'ciscoatm2MIBObjects':ciscoatm2MIBObjects,'ciscoatmSigStatTable':ciscoatmSigStatTable,'ciscoatmSigStatEntry':ciscoatmSigStatEntry,_M:ciscoatmSigSSCOPConEvents,_N:ciscoatmSigSSCOPErrdPdus,_O:ciscoatmSigDetectSetupAttempts,_P:ciscoatmSigEmitSetupAttempts,_Q:ciscoatmSigDetectUnavailRoutes,_R:ciscoatmSigEmitUnavailRoutes,_S:ciscoatmSigDetectUnavailResrcs,_T:ciscoatmSigEmitUnavailResrcs,_U:ciscoatmSigDetectCldPtyEvents,_V:ciscoatmSigEmitCldPtyEvents,_W:ciscoatmSigDetectMsgErrors,_X:ciscoatmSigEmitMsgErrors,_Y:ciscoatmSigDetectClgPtyEvents,_Z:ciscoatmSigEmitClgPtyEvents,_a:ciscoatmSigDetectTimerExpireds,_b:ciscoatmSigEmitTimerExpireds,_c:ciscoatmSigDetectRestarts,_d:ciscoatmSigEmitRestarts,_e:ciscoatmSigInEstabls,_f:ciscoatmSigOutEstabls,'ciscoatmSigSupportTable':ciscoatmSigSupportTable,'ciscoatmSigSupportEntry':ciscoatmSigSupportEntry,_g:ciscoatmSigSupportClgPtyNumDel,_h:ciscoatmSigSupportClgPtySubAddr,_i:ciscoatmSigSupportCldPtySubAddr,_j:ciscoatmSigSupportHiLyrInfo,_k:ciscoatmSigSupportLoLyrInfo,_l:ciscoatmSigSupportBlliRepeatInd,_m:ciscoatmSigSupportAALInfo,_n:ciscoatmSigSupportUnknownIe,'ciscoatmInterfaceExtTable':ciscoatmInterfaceExtTable,_L:ciscoatmInterfaceExtEntry,_o:ciscoatmInterfaceConfMaxSvpcVpi,_p:ciscoatmInterfaceCurrentMaxSvpcVpi,_q:ciscoatmInterfaceConfMaxSvccVpi,_r:ciscoatmInterfaceCurrentMaxSvccVpi,_s:ciscoatmInterfaceConfMinSvccVci,_t:ciscoatmInterfaceCurrentMinSvccVci,'ciscoatm2MIBConformance':ciscoatm2MIBConformance,'ciscoatm2MIBGroups':ciscoatm2MIBGroups,_J:ciscoAtmSwitchServcHostGroup,_K:ciscoAtmSwitchServcGroup,_u:ciscoAtmSwitchServcHostGroup2,'ciscoatm2MIBCompliances':ciscoatm2MIBCompliances,'ciscoatm2MIBCompliance':ciscoatm2MIBCompliance,'ciscoatm2MIBCompliance2':ciscoatm2MIBCompliance2})