_A6='f3OtnPerfGroup'
_A5='f3OtnConfigGroup'
_A4='f3OtnNetPortHistoryExtOduUAS'
_A3='f3OtnNetPortHistoryExtOduBBE'
_A2='f3OtnNetPortHistoryExtOduSES'
_A1='f3OtnNetPortHistoryExtOduErrSec'
_A0='f3OtnNetPortHistoryExtOtuUAS'
_z='f3OtnNetPortHistoryExtOtuBBE'
_y='f3OtnNetPortHistoryExtOtuSES'
_x='f3OtnNetPortHistoryExtOtuErrSec'
_w='f3OtnNetPortHistoryExtFecUncorrBlockErr'
_v='f3OtnNetPortHistoryExtFecCorrErr'
_u='f3OtnNetPortHistoryExtFecSES'
_t='f3OtnNetPortHistoryExtFecErrSec'
_s='f3OtnNetPortHistoryExtBerBeforeCorr'
_r='f3OtnNetPortStatsExtOduUAS'
_q='f3OtnNetPortStatsExtOduBBE'
_p='f3OtnNetPortStatsExtOduSES'
_o='f3OtnNetPortStatsExtOduErrSec'
_n='f3OtnNetPortStatsExtOtuUAS'
_m='f3OtnNetPortStatsExtOtuBBE'
_l='f3OtnNetPortStatsExtOtuSES'
_k='f3OtnNetPortStatsExtOtuErrSec'
_j='f3OtnNetPortStatsExtFecUncorrBlockErr'
_i='f3OtnNetPortStatsExtFecCorrErr'
_h='f3OtnNetPortStatsExtFecSES'
_g='f3OtnNetPortStatsExtFecErrSec'
_f='f3OtnNetPortStatsExtBerBeforeCorr'
_e='f3OtnNetPortTtiOpSpTxOdu'
_d='f3OtnNetPortTtiDapiTxOdu'
_c='f3OtnNetPortTtiSapiTxOdu'
_b='f3OtnNetPortTtiSapiExpectedRxOdu'
_a='f3OtnNetPortTtiOpSpActualRxOdu'
_Z='f3OtnNetPortTtiDapiActualRxOdu'
_Y='f3OtnNetPortTtiSapiActualRxOdu'
_X='f3OtnNetPortTtiActualRxHexOdu'
_W='f3OtnNetPortTimAisInsertOduEnabled'
_V='f3OtnNetPortTimDetectModeOdu'
_U='f3OtnNetPortTtiOpSpTxOtu'
_T='f3OtnNetPortTtiDapiTxOtu'
_S='f3OtnNetPortTtiSapiTxOtu'
_R='f3OtnNetPortTtiSapiExpectedRxOtu'
_Q='f3OtnNetPortTtiOpSpActualRxOtu'
_P='f3OtnNetPortTtiDapiActualRxOtu'
_O='f3OtnNetPortTtiSapiActualRxOtu'
_N='f3OtnNetPortTtiActualRxHexOtu'
_M='f3OtnNetPortTimAisInsertOtuEnabled'
_L='f3OtnNetPortTimDetectModeOtu'
_K='f3OtnNetPortFec'
_J='f3OtnNetPortFacilityType'
_I='f3OtnNetPortPayloadType'
_H='f3OtnNetPortHistoryExtEntry'
_G='f3OtnNetPortStatsExtEntry'
_F='f3OtnNetPortEntry'
_E='DisplayString'
_D='read-write'
_C='read-only'
_B='F3-OTN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
CmPmIntervalType,PerfCounter64=mibBuilder.importSymbols('CM-COMMON-MIB','CmPmIntervalType','PerfCounter64')
cmEthernetNetPortEntry,=mibBuilder.importSymbols('CM-FACILITY-MIB','cmEthernetNetPortEntry')
cmEthernetNetPortHistoryEntry,cmEthernetNetPortStatsEntry=mibBuilder.importSymbols('CM-PERFORMANCE-MIB','cmEthernetNetPortHistoryEntry','cmEthernetNetPortStatsEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention','TruthValue','VariablePointer')
f3OtnMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,34))
if mibBuilder.loadTexts:f3OtnMIB.setRevisions(('2014-07-15 00:00',))
class OtnFacilityType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('otu2e-eth',1))
class OtnFecType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nofec',1),('gfec',2),('efec-1',3),('efec-2',4)))
class TimDetectMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('sapi',2),('dapi',3),('sapi-dapi',4)))
_F3OtnConfigObjects_ObjectIdentity=ObjectIdentity
f3OtnConfigObjects=_F3OtnConfigObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,34,1))
_F3OtnNetPortExtTable_Object=MibTable
f3OtnNetPortExtTable=_F3OtnNetPortExtTable_Object((1,3,6,1,4,1,2544,1,12,34,1,1))
if mibBuilder.loadTexts:f3OtnNetPortExtTable.setStatus(_A)
_F3OtnNetPortEntry_Object=MibTableRow
f3OtnNetPortEntry=_F3OtnNetPortEntry_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1))
if mibBuilder.loadTexts:f3OtnNetPortEntry.setStatus(_A)
_F3OtnNetPortPayloadType_Type=Unsigned32
_F3OtnNetPortPayloadType_Object=MibTableColumn
f3OtnNetPortPayloadType=_F3OtnNetPortPayloadType_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,1),_F3OtnNetPortPayloadType_Type())
f3OtnNetPortPayloadType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortPayloadType.setStatus(_A)
_F3OtnNetPortFacilityType_Type=OtnFacilityType
_F3OtnNetPortFacilityType_Object=MibTableColumn
f3OtnNetPortFacilityType=_F3OtnNetPortFacilityType_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,2),_F3OtnNetPortFacilityType_Type())
f3OtnNetPortFacilityType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortFacilityType.setStatus(_A)
_F3OtnNetPortFec_Type=OtnFecType
_F3OtnNetPortFec_Object=MibTableColumn
f3OtnNetPortFec=_F3OtnNetPortFec_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,3),_F3OtnNetPortFec_Type())
f3OtnNetPortFec.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortFec.setStatus(_A)
_F3OtnNetPortTimDetectModeOtu_Type=TimDetectMode
_F3OtnNetPortTimDetectModeOtu_Object=MibTableColumn
f3OtnNetPortTimDetectModeOtu=_F3OtnNetPortTimDetectModeOtu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,4),_F3OtnNetPortTimDetectModeOtu_Type())
f3OtnNetPortTimDetectModeOtu.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTimDetectModeOtu.setStatus(_A)
_F3OtnNetPortTimAisInsertOtuEnabled_Type=TruthValue
_F3OtnNetPortTimAisInsertOtuEnabled_Object=MibTableColumn
f3OtnNetPortTimAisInsertOtuEnabled=_F3OtnNetPortTimAisInsertOtuEnabled_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,5),_F3OtnNetPortTimAisInsertOtuEnabled_Type())
f3OtnNetPortTimAisInsertOtuEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTimAisInsertOtuEnabled.setStatus(_A)
_F3OtnNetPortTtiActualRxHexOtu_Type=OctetString
_F3OtnNetPortTtiActualRxHexOtu_Object=MibTableColumn
f3OtnNetPortTtiActualRxHexOtu=_F3OtnNetPortTtiActualRxHexOtu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,6),_F3OtnNetPortTtiActualRxHexOtu_Type())
f3OtnNetPortTtiActualRxHexOtu.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortTtiActualRxHexOtu.setStatus(_A)
_F3OtnNetPortTtiSapiActualRxOtu_Type=DisplayString
_F3OtnNetPortTtiSapiActualRxOtu_Object=MibTableColumn
f3OtnNetPortTtiSapiActualRxOtu=_F3OtnNetPortTtiSapiActualRxOtu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,7),_F3OtnNetPortTtiSapiActualRxOtu_Type())
f3OtnNetPortTtiSapiActualRxOtu.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortTtiSapiActualRxOtu.setStatus(_A)
_F3OtnNetPortTtiDapiActualRxOtu_Type=DisplayString
_F3OtnNetPortTtiDapiActualRxOtu_Object=MibTableColumn
f3OtnNetPortTtiDapiActualRxOtu=_F3OtnNetPortTtiDapiActualRxOtu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,8),_F3OtnNetPortTtiDapiActualRxOtu_Type())
f3OtnNetPortTtiDapiActualRxOtu.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortTtiDapiActualRxOtu.setStatus(_A)
_F3OtnNetPortTtiOpSpActualRxOtu_Type=DisplayString
_F3OtnNetPortTtiOpSpActualRxOtu_Object=MibTableColumn
f3OtnNetPortTtiOpSpActualRxOtu=_F3OtnNetPortTtiOpSpActualRxOtu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,9),_F3OtnNetPortTtiOpSpActualRxOtu_Type())
f3OtnNetPortTtiOpSpActualRxOtu.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortTtiOpSpActualRxOtu.setStatus(_A)
class _F3OtnNetPortTtiSapiExpectedRxOtu_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_F3OtnNetPortTtiSapiExpectedRxOtu_Type.__name__=_E
_F3OtnNetPortTtiSapiExpectedRxOtu_Object=MibTableColumn
f3OtnNetPortTtiSapiExpectedRxOtu=_F3OtnNetPortTtiSapiExpectedRxOtu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,10),_F3OtnNetPortTtiSapiExpectedRxOtu_Type())
f3OtnNetPortTtiSapiExpectedRxOtu.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTtiSapiExpectedRxOtu.setStatus(_A)
class _F3OtnNetPortTtiSapiTxOtu_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_F3OtnNetPortTtiSapiTxOtu_Type.__name__=_E
_F3OtnNetPortTtiSapiTxOtu_Object=MibTableColumn
f3OtnNetPortTtiSapiTxOtu=_F3OtnNetPortTtiSapiTxOtu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,11),_F3OtnNetPortTtiSapiTxOtu_Type())
f3OtnNetPortTtiSapiTxOtu.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTtiSapiTxOtu.setStatus(_A)
class _F3OtnNetPortTtiDapiTxOtu_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_F3OtnNetPortTtiDapiTxOtu_Type.__name__=_E
_F3OtnNetPortTtiDapiTxOtu_Object=MibTableColumn
f3OtnNetPortTtiDapiTxOtu=_F3OtnNetPortTtiDapiTxOtu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,12),_F3OtnNetPortTtiDapiTxOtu_Type())
f3OtnNetPortTtiDapiTxOtu.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTtiDapiTxOtu.setStatus(_A)
class _F3OtnNetPortTtiOpSpTxOtu_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_F3OtnNetPortTtiOpSpTxOtu_Type.__name__=_E
_F3OtnNetPortTtiOpSpTxOtu_Object=MibTableColumn
f3OtnNetPortTtiOpSpTxOtu=_F3OtnNetPortTtiOpSpTxOtu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,13),_F3OtnNetPortTtiOpSpTxOtu_Type())
f3OtnNetPortTtiOpSpTxOtu.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTtiOpSpTxOtu.setStatus(_A)
_F3OtnNetPortTimDetectModeOdu_Type=TimDetectMode
_F3OtnNetPortTimDetectModeOdu_Object=MibTableColumn
f3OtnNetPortTimDetectModeOdu=_F3OtnNetPortTimDetectModeOdu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,14),_F3OtnNetPortTimDetectModeOdu_Type())
f3OtnNetPortTimDetectModeOdu.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTimDetectModeOdu.setStatus(_A)
_F3OtnNetPortTimAisInsertOduEnabled_Type=TruthValue
_F3OtnNetPortTimAisInsertOduEnabled_Object=MibTableColumn
f3OtnNetPortTimAisInsertOduEnabled=_F3OtnNetPortTimAisInsertOduEnabled_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,15),_F3OtnNetPortTimAisInsertOduEnabled_Type())
f3OtnNetPortTimAisInsertOduEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTimAisInsertOduEnabled.setStatus(_A)
_F3OtnNetPortTtiActualRxHexOdu_Type=OctetString
_F3OtnNetPortTtiActualRxHexOdu_Object=MibTableColumn
f3OtnNetPortTtiActualRxHexOdu=_F3OtnNetPortTtiActualRxHexOdu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,16),_F3OtnNetPortTtiActualRxHexOdu_Type())
f3OtnNetPortTtiActualRxHexOdu.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortTtiActualRxHexOdu.setStatus(_A)
_F3OtnNetPortTtiSapiActualRxOdu_Type=DisplayString
_F3OtnNetPortTtiSapiActualRxOdu_Object=MibTableColumn
f3OtnNetPortTtiSapiActualRxOdu=_F3OtnNetPortTtiSapiActualRxOdu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,17),_F3OtnNetPortTtiSapiActualRxOdu_Type())
f3OtnNetPortTtiSapiActualRxOdu.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortTtiSapiActualRxOdu.setStatus(_A)
_F3OtnNetPortTtiDapiActualRxOdu_Type=DisplayString
_F3OtnNetPortTtiDapiActualRxOdu_Object=MibTableColumn
f3OtnNetPortTtiDapiActualRxOdu=_F3OtnNetPortTtiDapiActualRxOdu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,18),_F3OtnNetPortTtiDapiActualRxOdu_Type())
f3OtnNetPortTtiDapiActualRxOdu.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortTtiDapiActualRxOdu.setStatus(_A)
_F3OtnNetPortTtiOpSpActualRxOdu_Type=DisplayString
_F3OtnNetPortTtiOpSpActualRxOdu_Object=MibTableColumn
f3OtnNetPortTtiOpSpActualRxOdu=_F3OtnNetPortTtiOpSpActualRxOdu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,19),_F3OtnNetPortTtiOpSpActualRxOdu_Type())
f3OtnNetPortTtiOpSpActualRxOdu.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortTtiOpSpActualRxOdu.setStatus(_A)
class _F3OtnNetPortTtiSapiExpectedRxOdu_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_F3OtnNetPortTtiSapiExpectedRxOdu_Type.__name__=_E
_F3OtnNetPortTtiSapiExpectedRxOdu_Object=MibTableColumn
f3OtnNetPortTtiSapiExpectedRxOdu=_F3OtnNetPortTtiSapiExpectedRxOdu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,20),_F3OtnNetPortTtiSapiExpectedRxOdu_Type())
f3OtnNetPortTtiSapiExpectedRxOdu.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTtiSapiExpectedRxOdu.setStatus(_A)
class _F3OtnNetPortTtiSapiTxOdu_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_F3OtnNetPortTtiSapiTxOdu_Type.__name__=_E
_F3OtnNetPortTtiSapiTxOdu_Object=MibTableColumn
f3OtnNetPortTtiSapiTxOdu=_F3OtnNetPortTtiSapiTxOdu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,21),_F3OtnNetPortTtiSapiTxOdu_Type())
f3OtnNetPortTtiSapiTxOdu.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTtiSapiTxOdu.setStatus(_A)
class _F3OtnNetPortTtiDapiTxOdu_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_F3OtnNetPortTtiDapiTxOdu_Type.__name__=_E
_F3OtnNetPortTtiDapiTxOdu_Object=MibTableColumn
f3OtnNetPortTtiDapiTxOdu=_F3OtnNetPortTtiDapiTxOdu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,22),_F3OtnNetPortTtiDapiTxOdu_Type())
f3OtnNetPortTtiDapiTxOdu.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTtiDapiTxOdu.setStatus(_A)
class _F3OtnNetPortTtiOpSpTxOdu_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_F3OtnNetPortTtiOpSpTxOdu_Type.__name__=_E
_F3OtnNetPortTtiOpSpTxOdu_Object=MibTableColumn
f3OtnNetPortTtiOpSpTxOdu=_F3OtnNetPortTtiOpSpTxOdu_Object((1,3,6,1,4,1,2544,1,12,34,1,1,1,23),_F3OtnNetPortTtiOpSpTxOdu_Type())
f3OtnNetPortTtiOpSpTxOdu.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OtnNetPortTtiOpSpTxOdu.setStatus(_A)
_F3OtnPerfObjects_ObjectIdentity=ObjectIdentity
f3OtnPerfObjects=_F3OtnPerfObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,34,2))
_F3OtnNetPortStatsExtTable_Object=MibTable
f3OtnNetPortStatsExtTable=_F3OtnNetPortStatsExtTable_Object((1,3,6,1,4,1,2544,1,12,34,2,1))
if mibBuilder.loadTexts:f3OtnNetPortStatsExtTable.setStatus(_A)
_F3OtnNetPortStatsExtEntry_Object=MibTableRow
f3OtnNetPortStatsExtEntry=_F3OtnNetPortStatsExtEntry_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1))
if mibBuilder.loadTexts:f3OtnNetPortStatsExtEntry.setStatus(_A)
_F3OtnNetPortStatsExtBerBeforeCorr_Type=PerfCounter64
_F3OtnNetPortStatsExtBerBeforeCorr_Object=MibTableColumn
f3OtnNetPortStatsExtBerBeforeCorr=_F3OtnNetPortStatsExtBerBeforeCorr_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,1),_F3OtnNetPortStatsExtBerBeforeCorr_Type())
f3OtnNetPortStatsExtBerBeforeCorr.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtBerBeforeCorr.setStatus(_A)
_F3OtnNetPortStatsExtFecErrSec_Type=Integer32
_F3OtnNetPortStatsExtFecErrSec_Object=MibTableColumn
f3OtnNetPortStatsExtFecErrSec=_F3OtnNetPortStatsExtFecErrSec_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,2),_F3OtnNetPortStatsExtFecErrSec_Type())
f3OtnNetPortStatsExtFecErrSec.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtFecErrSec.setStatus(_A)
_F3OtnNetPortStatsExtFecSES_Type=Integer32
_F3OtnNetPortStatsExtFecSES_Object=MibTableColumn
f3OtnNetPortStatsExtFecSES=_F3OtnNetPortStatsExtFecSES_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,3),_F3OtnNetPortStatsExtFecSES_Type())
f3OtnNetPortStatsExtFecSES.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtFecSES.setStatus(_A)
_F3OtnNetPortStatsExtFecCorrErr_Type=PerfCounter64
_F3OtnNetPortStatsExtFecCorrErr_Object=MibTableColumn
f3OtnNetPortStatsExtFecCorrErr=_F3OtnNetPortStatsExtFecCorrErr_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,4),_F3OtnNetPortStatsExtFecCorrErr_Type())
f3OtnNetPortStatsExtFecCorrErr.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtFecCorrErr.setStatus(_A)
_F3OtnNetPortStatsExtFecUncorrBlockErr_Type=PerfCounter64
_F3OtnNetPortStatsExtFecUncorrBlockErr_Object=MibTableColumn
f3OtnNetPortStatsExtFecUncorrBlockErr=_F3OtnNetPortStatsExtFecUncorrBlockErr_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,5),_F3OtnNetPortStatsExtFecUncorrBlockErr_Type())
f3OtnNetPortStatsExtFecUncorrBlockErr.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtFecUncorrBlockErr.setStatus(_A)
_F3OtnNetPortStatsExtOtuErrSec_Type=Integer32
_F3OtnNetPortStatsExtOtuErrSec_Object=MibTableColumn
f3OtnNetPortStatsExtOtuErrSec=_F3OtnNetPortStatsExtOtuErrSec_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,6),_F3OtnNetPortStatsExtOtuErrSec_Type())
f3OtnNetPortStatsExtOtuErrSec.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtOtuErrSec.setStatus(_A)
_F3OtnNetPortStatsExtOtuSES_Type=Integer32
_F3OtnNetPortStatsExtOtuSES_Object=MibTableColumn
f3OtnNetPortStatsExtOtuSES=_F3OtnNetPortStatsExtOtuSES_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,7),_F3OtnNetPortStatsExtOtuSES_Type())
f3OtnNetPortStatsExtOtuSES.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtOtuSES.setStatus(_A)
_F3OtnNetPortStatsExtOtuBBE_Type=PerfCounter64
_F3OtnNetPortStatsExtOtuBBE_Object=MibTableColumn
f3OtnNetPortStatsExtOtuBBE=_F3OtnNetPortStatsExtOtuBBE_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,8),_F3OtnNetPortStatsExtOtuBBE_Type())
f3OtnNetPortStatsExtOtuBBE.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtOtuBBE.setStatus(_A)
_F3OtnNetPortStatsExtOtuUAS_Type=Integer32
_F3OtnNetPortStatsExtOtuUAS_Object=MibTableColumn
f3OtnNetPortStatsExtOtuUAS=_F3OtnNetPortStatsExtOtuUAS_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,9),_F3OtnNetPortStatsExtOtuUAS_Type())
f3OtnNetPortStatsExtOtuUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtOtuUAS.setStatus(_A)
_F3OtnNetPortStatsExtOduErrSec_Type=Integer32
_F3OtnNetPortStatsExtOduErrSec_Object=MibTableColumn
f3OtnNetPortStatsExtOduErrSec=_F3OtnNetPortStatsExtOduErrSec_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,10),_F3OtnNetPortStatsExtOduErrSec_Type())
f3OtnNetPortStatsExtOduErrSec.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtOduErrSec.setStatus(_A)
_F3OtnNetPortStatsExtOduSES_Type=Integer32
_F3OtnNetPortStatsExtOduSES_Object=MibTableColumn
f3OtnNetPortStatsExtOduSES=_F3OtnNetPortStatsExtOduSES_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,11),_F3OtnNetPortStatsExtOduSES_Type())
f3OtnNetPortStatsExtOduSES.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtOduSES.setStatus(_A)
_F3OtnNetPortStatsExtOduBBE_Type=PerfCounter64
_F3OtnNetPortStatsExtOduBBE_Object=MibTableColumn
f3OtnNetPortStatsExtOduBBE=_F3OtnNetPortStatsExtOduBBE_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,12),_F3OtnNetPortStatsExtOduBBE_Type())
f3OtnNetPortStatsExtOduBBE.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtOduBBE.setStatus(_A)
_F3OtnNetPortStatsExtOduUAS_Type=Integer32
_F3OtnNetPortStatsExtOduUAS_Object=MibTableColumn
f3OtnNetPortStatsExtOduUAS=_F3OtnNetPortStatsExtOduUAS_Object((1,3,6,1,4,1,2544,1,12,34,2,1,1,13),_F3OtnNetPortStatsExtOduUAS_Type())
f3OtnNetPortStatsExtOduUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortStatsExtOduUAS.setStatus(_A)
_F3OtnNetPortHistoryExtTable_Object=MibTable
f3OtnNetPortHistoryExtTable=_F3OtnNetPortHistoryExtTable_Object((1,3,6,1,4,1,2544,1,12,34,2,2))
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtTable.setStatus(_A)
_F3OtnNetPortHistoryExtEntry_Object=MibTableRow
f3OtnNetPortHistoryExtEntry=_F3OtnNetPortHistoryExtEntry_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1))
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtEntry.setStatus(_A)
_F3OtnNetPortHistoryExtBerBeforeCorr_Type=PerfCounter64
_F3OtnNetPortHistoryExtBerBeforeCorr_Object=MibTableColumn
f3OtnNetPortHistoryExtBerBeforeCorr=_F3OtnNetPortHistoryExtBerBeforeCorr_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,1),_F3OtnNetPortHistoryExtBerBeforeCorr_Type())
f3OtnNetPortHistoryExtBerBeforeCorr.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtBerBeforeCorr.setStatus(_A)
_F3OtnNetPortHistoryExtFecErrSec_Type=Integer32
_F3OtnNetPortHistoryExtFecErrSec_Object=MibTableColumn
f3OtnNetPortHistoryExtFecErrSec=_F3OtnNetPortHistoryExtFecErrSec_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,2),_F3OtnNetPortHistoryExtFecErrSec_Type())
f3OtnNetPortHistoryExtFecErrSec.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtFecErrSec.setStatus(_A)
_F3OtnNetPortHistoryExtFecSES_Type=Integer32
_F3OtnNetPortHistoryExtFecSES_Object=MibTableColumn
f3OtnNetPortHistoryExtFecSES=_F3OtnNetPortHistoryExtFecSES_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,3),_F3OtnNetPortHistoryExtFecSES_Type())
f3OtnNetPortHistoryExtFecSES.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtFecSES.setStatus(_A)
_F3OtnNetPortHistoryExtFecCorrErr_Type=PerfCounter64
_F3OtnNetPortHistoryExtFecCorrErr_Object=MibTableColumn
f3OtnNetPortHistoryExtFecCorrErr=_F3OtnNetPortHistoryExtFecCorrErr_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,4),_F3OtnNetPortHistoryExtFecCorrErr_Type())
f3OtnNetPortHistoryExtFecCorrErr.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtFecCorrErr.setStatus(_A)
_F3OtnNetPortHistoryExtFecUncorrBlockErr_Type=PerfCounter64
_F3OtnNetPortHistoryExtFecUncorrBlockErr_Object=MibTableColumn
f3OtnNetPortHistoryExtFecUncorrBlockErr=_F3OtnNetPortHistoryExtFecUncorrBlockErr_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,5),_F3OtnNetPortHistoryExtFecUncorrBlockErr_Type())
f3OtnNetPortHistoryExtFecUncorrBlockErr.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtFecUncorrBlockErr.setStatus(_A)
_F3OtnNetPortHistoryExtOtuErrSec_Type=Integer32
_F3OtnNetPortHistoryExtOtuErrSec_Object=MibTableColumn
f3OtnNetPortHistoryExtOtuErrSec=_F3OtnNetPortHistoryExtOtuErrSec_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,6),_F3OtnNetPortHistoryExtOtuErrSec_Type())
f3OtnNetPortHistoryExtOtuErrSec.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtOtuErrSec.setStatus(_A)
_F3OtnNetPortHistoryExtOtuSES_Type=Integer32
_F3OtnNetPortHistoryExtOtuSES_Object=MibTableColumn
f3OtnNetPortHistoryExtOtuSES=_F3OtnNetPortHistoryExtOtuSES_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,7),_F3OtnNetPortHistoryExtOtuSES_Type())
f3OtnNetPortHistoryExtOtuSES.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtOtuSES.setStatus(_A)
_F3OtnNetPortHistoryExtOtuBBE_Type=PerfCounter64
_F3OtnNetPortHistoryExtOtuBBE_Object=MibTableColumn
f3OtnNetPortHistoryExtOtuBBE=_F3OtnNetPortHistoryExtOtuBBE_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,8),_F3OtnNetPortHistoryExtOtuBBE_Type())
f3OtnNetPortHistoryExtOtuBBE.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtOtuBBE.setStatus(_A)
_F3OtnNetPortHistoryExtOtuUAS_Type=Integer32
_F3OtnNetPortHistoryExtOtuUAS_Object=MibTableColumn
f3OtnNetPortHistoryExtOtuUAS=_F3OtnNetPortHistoryExtOtuUAS_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,9),_F3OtnNetPortHistoryExtOtuUAS_Type())
f3OtnNetPortHistoryExtOtuUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtOtuUAS.setStatus(_A)
_F3OtnNetPortHistoryExtOduErrSec_Type=Integer32
_F3OtnNetPortHistoryExtOduErrSec_Object=MibTableColumn
f3OtnNetPortHistoryExtOduErrSec=_F3OtnNetPortHistoryExtOduErrSec_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,10),_F3OtnNetPortHistoryExtOduErrSec_Type())
f3OtnNetPortHistoryExtOduErrSec.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtOduErrSec.setStatus(_A)
_F3OtnNetPortHistoryExtOduSES_Type=Integer32
_F3OtnNetPortHistoryExtOduSES_Object=MibTableColumn
f3OtnNetPortHistoryExtOduSES=_F3OtnNetPortHistoryExtOduSES_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,11),_F3OtnNetPortHistoryExtOduSES_Type())
f3OtnNetPortHistoryExtOduSES.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtOduSES.setStatus(_A)
_F3OtnNetPortHistoryExtOduBBE_Type=PerfCounter64
_F3OtnNetPortHistoryExtOduBBE_Object=MibTableColumn
f3OtnNetPortHistoryExtOduBBE=_F3OtnNetPortHistoryExtOduBBE_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,12),_F3OtnNetPortHistoryExtOduBBE_Type())
f3OtnNetPortHistoryExtOduBBE.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtOduBBE.setStatus(_A)
_F3OtnNetPortHistoryExtOduUAS_Type=Integer32
_F3OtnNetPortHistoryExtOduUAS_Object=MibTableColumn
f3OtnNetPortHistoryExtOduUAS=_F3OtnNetPortHistoryExtOduUAS_Object((1,3,6,1,4,1,2544,1,12,34,2,2,1,13),_F3OtnNetPortHistoryExtOduUAS_Type())
f3OtnNetPortHistoryExtOduUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OtnNetPortHistoryExtOduUAS.setStatus(_A)
_F3OtnConformance_ObjectIdentity=ObjectIdentity
f3OtnConformance=_F3OtnConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,34,3))
_F3OtnCompliances_ObjectIdentity=ObjectIdentity
f3OtnCompliances=_F3OtnCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,34,3,1))
_F3OtnGroups_ObjectIdentity=ObjectIdentity
f3OtnGroups=_F3OtnGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,34,3,2))
cmEthernetNetPortEntry.registerAugmentions((_B,_F))
f3OtnNetPortEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
cmEthernetNetPortStatsEntry.registerAugmentions((_B,_G))
f3OtnNetPortStatsExtEntry.setIndexNames(*cmEthernetNetPortStatsEntry.getIndexNames())
cmEthernetNetPortHistoryEntry.registerAugmentions((_B,_H))
f3OtnNetPortHistoryExtEntry.setIndexNames(*cmEthernetNetPortHistoryEntry.getIndexNames())
f3OtnConfigGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,34,3,2,1))
f3OtnConfigGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:f3OtnConfigGroup.setStatus(_A)
f3OtnPerfGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,34,3,2,2))
f3OtnPerfGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:f3OtnPerfGroup.setStatus(_A)
f3OtnCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,34,3,1,1))
f3OtnCompliance.setObjects(*((_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:f3OtnCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OtnFacilityType':OtnFacilityType,'OtnFecType':OtnFecType,'TimDetectMode':TimDetectMode,'f3OtnMIB':f3OtnMIB,'f3OtnConfigObjects':f3OtnConfigObjects,'f3OtnNetPortExtTable':f3OtnNetPortExtTable,_F:f3OtnNetPortEntry,_I:f3OtnNetPortPayloadType,_J:f3OtnNetPortFacilityType,_K:f3OtnNetPortFec,_L:f3OtnNetPortTimDetectModeOtu,_M:f3OtnNetPortTimAisInsertOtuEnabled,_N:f3OtnNetPortTtiActualRxHexOtu,_O:f3OtnNetPortTtiSapiActualRxOtu,_P:f3OtnNetPortTtiDapiActualRxOtu,_Q:f3OtnNetPortTtiOpSpActualRxOtu,_R:f3OtnNetPortTtiSapiExpectedRxOtu,_S:f3OtnNetPortTtiSapiTxOtu,_T:f3OtnNetPortTtiDapiTxOtu,_U:f3OtnNetPortTtiOpSpTxOtu,_V:f3OtnNetPortTimDetectModeOdu,_W:f3OtnNetPortTimAisInsertOduEnabled,_X:f3OtnNetPortTtiActualRxHexOdu,_Y:f3OtnNetPortTtiSapiActualRxOdu,_Z:f3OtnNetPortTtiDapiActualRxOdu,_a:f3OtnNetPortTtiOpSpActualRxOdu,_b:f3OtnNetPortTtiSapiExpectedRxOdu,_c:f3OtnNetPortTtiSapiTxOdu,_d:f3OtnNetPortTtiDapiTxOdu,_e:f3OtnNetPortTtiOpSpTxOdu,'f3OtnPerfObjects':f3OtnPerfObjects,'f3OtnNetPortStatsExtTable':f3OtnNetPortStatsExtTable,_G:f3OtnNetPortStatsExtEntry,_f:f3OtnNetPortStatsExtBerBeforeCorr,_g:f3OtnNetPortStatsExtFecErrSec,_h:f3OtnNetPortStatsExtFecSES,_i:f3OtnNetPortStatsExtFecCorrErr,_j:f3OtnNetPortStatsExtFecUncorrBlockErr,_k:f3OtnNetPortStatsExtOtuErrSec,_l:f3OtnNetPortStatsExtOtuSES,_m:f3OtnNetPortStatsExtOtuBBE,_n:f3OtnNetPortStatsExtOtuUAS,_o:f3OtnNetPortStatsExtOduErrSec,_p:f3OtnNetPortStatsExtOduSES,_q:f3OtnNetPortStatsExtOduBBE,_r:f3OtnNetPortStatsExtOduUAS,'f3OtnNetPortHistoryExtTable':f3OtnNetPortHistoryExtTable,_H:f3OtnNetPortHistoryExtEntry,_s:f3OtnNetPortHistoryExtBerBeforeCorr,_t:f3OtnNetPortHistoryExtFecErrSec,_u:f3OtnNetPortHistoryExtFecSES,_v:f3OtnNetPortHistoryExtFecCorrErr,_w:f3OtnNetPortHistoryExtFecUncorrBlockErr,_x:f3OtnNetPortHistoryExtOtuErrSec,_y:f3OtnNetPortHistoryExtOtuSES,_z:f3OtnNetPortHistoryExtOtuBBE,_A0:f3OtnNetPortHistoryExtOtuUAS,_A1:f3OtnNetPortHistoryExtOduErrSec,_A2:f3OtnNetPortHistoryExtOduSES,_A3:f3OtnNetPortHistoryExtOduBBE,_A4:f3OtnNetPortHistoryExtOduUAS,'f3OtnConformance':f3OtnConformance,'f3OtnCompliances':f3OtnCompliances,'f3OtnCompliance':f3OtnCompliance,'f3OtnGroups':f3OtnGroups,_A5:f3OtnConfigGroup,_A6:f3OtnPerfGroup})