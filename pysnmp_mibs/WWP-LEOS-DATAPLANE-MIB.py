_Z='wwpLeosDpTsFrameCosMapRColorValue'
_Y='wwpLeosDpTsFrameCosMapRCosValue'
_X='wwpLeosDpTsMplsTcCosMapMplsTcValue'
_W='wwpLeosDpTsDot1dDeiCosMapDeiValue'
_V='wwpLeosDpTsDot1dDeiCosMapDot1dValue'
_U='wwpLeosDpTsDscpCosMapDscpValue'
_T='wwpLeosDpTsDot1dCosMapDot1dValue'
_S='deprecated'
_R='wwpLeosDpTsQueueMapId'
_Q='wwpLeosDpTsQEgressPortQueueGroupStatsQueueId'
_P='wwpLeosDpTsQEgressPortQueueGroupQueueId'
_O='wwpLeosDpTsQCAProfileWREDSimpleId'
_N='wwpLeosDpTsQCAProfileSREDId'
_M='drop-100-percent'
_L='wwpLeosDpTsFrameCosMapProfileId'
_K='wwpLeosDpTsQEgressPortQueueGroupId'
_J='read-only'
_I='wwpLeosDpTsCosMapProfileId'
_H='DisplayString'
_G='Unsigned32'
_F='not-accessible'
_E='read-write'
_D='WWP-LEOS-DATAPLANE-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosDataplaneMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,500))
if mibBuilder.loadTexts:wwpLeosDataplaneMIB.setRevisions(('2012-06-08 00:50','2011-06-13 00:50','2011-05-10 00:50','2010-07-28 00:00','2010-02-12 00:00','2008-11-11 17:00'))
class DpTsQSredDropProbability(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),('drop-6-25-percent',2),('drop-3-125-percent',3),('drop-1-5625-percent',4),('drop-0-78125-percent',5),('drop-0-390625-percent',6),('drop-0-1953125-percent',7),('drop-0-0976562-percent',8)))
class DpTsQWredSimpleMaxDropProbability(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_M,1),('drop-75-percent',2),('drop-50-percent',3),('drop-25-percent',4),('drop-10-percent',5),('drop-9-percent',6),('drop-8-percent',7),('drop-7-percent',8),('drop-6-percent',9),('drop-5-percent',10),('drop-4-percent',11),('drop-3-percent',12),('drop-2-percent',13),('drop-1-percent',14),('drop-0-percent',15)))
class DpTsRCosMappingColor(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('green',1),('yellow',2)))
_WwpLeosDpMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosDpMIBObjects=_WwpLeosDpMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,500,1))
_WwpLeosDpTs_ObjectIdentity=ObjectIdentity
wwpLeosDpTs=_WwpLeosDpTs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,500,1,1))
_WwpLeosDpTsQueuing_ObjectIdentity=ObjectIdentity
wwpLeosDpTsQueuing=_WwpLeosDpTsQueuing_ObjectIdentity((1,3,6,1,4,1,6141,2,60,500,1,1,1))
_WwpLeosDpTsQCongestionAvoidanceProfile_ObjectIdentity=ObjectIdentity
wwpLeosDpTsQCongestionAvoidanceProfile=_WwpLeosDpTsQCongestionAvoidanceProfile_ObjectIdentity((1,3,6,1,4,1,6141,2,60,500,1,1,1,1))
_WwpLeosDpTsQCAProfileSREDTable_Object=MibTable
wwpLeosDpTsQCAProfileSREDTable=_WwpLeosDpTsQCAProfileSREDTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,1))
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileSREDTable.setStatus(_A)
_WwpLeosDpTsQCAProfileSREDEntry_Object=MibTableRow
wwpLeosDpTsQCAProfileSREDEntry=_WwpLeosDpTsQCAProfileSREDEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,1,1))
wwpLeosDpTsQCAProfileSREDEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileSREDEntry.setStatus(_A)
class _WwpLeosDpTsQCAProfileSREDId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosDpTsQCAProfileSREDId_Type.__name__=_C
_WwpLeosDpTsQCAProfileSREDId_Object=MibTableColumn
wwpLeosDpTsQCAProfileSREDId=_WwpLeosDpTsQCAProfileSREDId_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,1,1,1),_WwpLeosDpTsQCAProfileSREDId_Type())
wwpLeosDpTsQCAProfileSREDId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileSREDId.setStatus(_A)
class _WwpLeosDpTsQCAProfileSREDName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_WwpLeosDpTsQCAProfileSREDName_Type.__name__=_H
_WwpLeosDpTsQCAProfileSREDName_Object=MibTableColumn
wwpLeosDpTsQCAProfileSREDName=_WwpLeosDpTsQCAProfileSREDName_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,1,1,2),_WwpLeosDpTsQCAProfileSREDName_Type())
wwpLeosDpTsQCAProfileSREDName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileSREDName.setStatus(_A)
_WwpLeosDpTsQCAProfileSREDGreenThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileSREDGreenThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileSREDGreenThreshold=_WwpLeosDpTsQCAProfileSREDGreenThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,1,1,4),_WwpLeosDpTsQCAProfileSREDGreenThreshold_Type())
wwpLeosDpTsQCAProfileSREDGreenThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileSREDGreenThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileSREDGreenDropProbability_Type=DpTsQSredDropProbability
_WwpLeosDpTsQCAProfileSREDGreenDropProbability_Object=MibTableColumn
wwpLeosDpTsQCAProfileSREDGreenDropProbability=_WwpLeosDpTsQCAProfileSREDGreenDropProbability_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,1,1,5),_WwpLeosDpTsQCAProfileSREDGreenDropProbability_Type())
wwpLeosDpTsQCAProfileSREDGreenDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileSREDGreenDropProbability.setStatus(_A)
_WwpLeosDpTsQCAProfileSREDYellowThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileSREDYellowThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileSREDYellowThreshold=_WwpLeosDpTsQCAProfileSREDYellowThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,1,1,6),_WwpLeosDpTsQCAProfileSREDYellowThreshold_Type())
wwpLeosDpTsQCAProfileSREDYellowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileSREDYellowThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileSREDYellowDropProbability_Type=DpTsQSredDropProbability
_WwpLeosDpTsQCAProfileSREDYellowDropProbability_Object=MibTableColumn
wwpLeosDpTsQCAProfileSREDYellowDropProbability=_WwpLeosDpTsQCAProfileSREDYellowDropProbability_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,1,1,7),_WwpLeosDpTsQCAProfileSREDYellowDropProbability_Type())
wwpLeosDpTsQCAProfileSREDYellowDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileSREDYellowDropProbability.setStatus(_A)
_WwpLeosDpTsQCAProfileSREDRowStatus_Type=RowStatus
_WwpLeosDpTsQCAProfileSREDRowStatus_Object=MibTableColumn
wwpLeosDpTsQCAProfileSREDRowStatus=_WwpLeosDpTsQCAProfileSREDRowStatus_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,1,1,9),_WwpLeosDpTsQCAProfileSREDRowStatus_Type())
wwpLeosDpTsQCAProfileSREDRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileSREDRowStatus.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleTable_Object=MibTable
wwpLeosDpTsQCAProfileWREDSimpleTable=_WwpLeosDpTsQCAProfileWREDSimpleTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2))
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleTable.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleEntry_Object=MibTableRow
wwpLeosDpTsQCAProfileWREDSimpleEntry=_WwpLeosDpTsQCAProfileWREDSimpleEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1))
wwpLeosDpTsQCAProfileWREDSimpleEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleEntry.setStatus(_A)
class _WwpLeosDpTsQCAProfileWREDSimpleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosDpTsQCAProfileWREDSimpleId_Type.__name__=_C
_WwpLeosDpTsQCAProfileWREDSimpleId_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleId=_WwpLeosDpTsQCAProfileWREDSimpleId_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,1),_WwpLeosDpTsQCAProfileWREDSimpleId_Type())
wwpLeosDpTsQCAProfileWREDSimpleId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleId.setStatus(_A)
class _WwpLeosDpTsQCAProfileWREDSimpleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_WwpLeosDpTsQCAProfileWREDSimpleName_Type.__name__=_H
_WwpLeosDpTsQCAProfileWREDSimpleName_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleName=_WwpLeosDpTsQCAProfileWREDSimpleName_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,2),_WwpLeosDpTsQCAProfileWREDSimpleName_Type())
wwpLeosDpTsQCAProfileWREDSimpleName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleName.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold=_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,3),_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold_Type())
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold=_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,4),_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold_Type())
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability_Type=DpTsQWredSimpleMaxDropProbability
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability=_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,5),_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability_Type())
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold=_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,6),_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold_Type())
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold=_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,7),_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold_Type())
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability_Type=DpTsQWredSimpleMaxDropProbability
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability=_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,8),_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability_Type())
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleRowStatus_Type=RowStatus
_WwpLeosDpTsQCAProfileWREDSimpleRowStatus_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleRowStatus=_WwpLeosDpTsQCAProfileWREDSimpleRowStatus_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,9),_WwpLeosDpTsQCAProfileWREDSimpleRowStatus_Type())
wwpLeosDpTsQCAProfileWREDSimpleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleRowStatus.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold=_WwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,10),_WwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold_Type())
wwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold=_WwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,11),_WwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold_Type())
wwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability_Type=DpTsQWredSimpleMaxDropProbability
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability=_WwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,12),_WwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability_Type())
wwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold=_WwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,13),_WwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold_Type())
wwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold=_WwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,14),_WwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold_Type())
wwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability_Type=DpTsQWredSimpleMaxDropProbability
_WwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability=_WwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,15),_WwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability_Type())
wwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold=_WwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,16),_WwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold_Type())
wwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold_Type=Integer32
_WwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold=_WwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,17),_WwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold_Type())
wwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability_Type=DpTsQWredSimpleMaxDropProbability
_WwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability=_WwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,18),_WwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability_Type())
wwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability.setStatus(_A)
_WwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit_Type=Integer32
_WwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit_Object=MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit=_WwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,1,2,1,19),_WwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit_Type())
wwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroup_ObjectIdentity=ObjectIdentity
wwpLeosDpTsQEgressPortQueueGroup=_WwpLeosDpTsQEgressPortQueueGroup_ObjectIdentity((1,3,6,1,4,1,6141,2,60,500,1,1,1,2))
_WwpLeosDpTsQEgressPortQueueGroupTable_Object=MibTable
wwpLeosDpTsQEgressPortQueueGroupTable=_WwpLeosDpTsQEgressPortQueueGroupTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,1))
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupTable.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupEntry_Object=MibTableRow
wwpLeosDpTsQEgressPortQueueGroupEntry=_WwpLeosDpTsQEgressPortQueueGroupEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,1,1))
wwpLeosDpTsQEgressPortQueueGroupEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupEntry.setStatus(_A)
class _WwpLeosDpTsQEgressPortQueueGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosDpTsQEgressPortQueueGroupId_Type.__name__=_C
_WwpLeosDpTsQEgressPortQueueGroupId_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupId=_WwpLeosDpTsQEgressPortQueueGroupId_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,1,1,1),_WwpLeosDpTsQEgressPortQueueGroupId_Type())
wwpLeosDpTsQEgressPortQueueGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupId.setStatus(_A)
class _WwpLeosDpTsQEgressPortQueueGroupQCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WwpLeosDpTsQEgressPortQueueGroupQCount_Type.__name__=_C
_WwpLeosDpTsQEgressPortQueueGroupQCount_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQCount=_WwpLeosDpTsQEgressPortQueueGroupQCount_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,1,1,2),_WwpLeosDpTsQEgressPortQueueGroupQCount_Type())
wwpLeosDpTsQEgressPortQueueGroupQCount.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQCount.setStatus(_A)
class _WwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,99)));namedValues=NamedValues(*(('strictpriority',1),('weightedfairqueuing',2),('roundrobin',3),('weighteddeficitroundrobin',4),('weightedroundrobin',5),('unknown',99)))
_WwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm_Type.__name__=_C
_WwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm=_WwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,1,1,3),_WwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm_Type())
wwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupShaperBandwidth_Type=Unsigned32
_WwpLeosDpTsQEgressPortQueueGroupShaperBandwidth_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth=_WwpLeosDpTsQEgressPortQueueGroupShaperBandwidth_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,1,1,4),_WwpLeosDpTsQEgressPortQueueGroupShaperBandwidth_Type())
wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth.setUnits('kbps')
class _WwpLeosDpTsQEgressPortQueueGroupBurstSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,262144))
_WwpLeosDpTsQEgressPortQueueGroupBurstSize_Type.__name__=_G
_WwpLeosDpTsQEgressPortQueueGroupBurstSize_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupBurstSize=_WwpLeosDpTsQEgressPortQueueGroupBurstSize_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,1,1,5),_WwpLeosDpTsQEgressPortQueueGroupBurstSize_Type())
wwpLeosDpTsQEgressPortQueueGroupBurstSize.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupBurstSize.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupBurstSize.setUnits('kb')
class _WwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,1600))
_WwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity_Type.__name__=_G
_WwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity=_WwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,1,1,6),_WwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity_Type())
wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity.setUnits('kb')
_WwpLeosDpTsQEgressPortQueueGroupQConfigTable_Object=MibTable
wwpLeosDpTsQEgressPortQueueGroupQConfigTable=_WwpLeosDpTsQEgressPortQueueGroupQConfigTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,2))
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQConfigTable.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQConfigEntry_Object=MibTableRow
wwpLeosDpTsQEgressPortQueueGroupQConfigEntry=_WwpLeosDpTsQEgressPortQueueGroupQConfigEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,2,1))
wwpLeosDpTsQEgressPortQueueGroupQConfigEntry.setIndexNames((0,_D,_K),(0,_D,_P))
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQConfigEntry.setStatus(_A)
class _WwpLeosDpTsQEgressPortQueueGroupQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsQEgressPortQueueGroupQueueId_Type.__name__=_C
_WwpLeosDpTsQEgressPortQueueGroupQueueId_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueId=_WwpLeosDpTsQEgressPortQueueGroupQueueId_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,2,1,1),_WwpLeosDpTsQEgressPortQueueGroupQueueId_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueId.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQueueCAPId_Type=Integer32
_WwpLeosDpTsQEgressPortQueueGroupQueueCAPId_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueCAPId=_WwpLeosDpTsQEgressPortQueueGroupQueueCAPId_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,2,1,2),_WwpLeosDpTsQEgressPortQueueGroupQueueCAPId_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueCAPId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueCAPId.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQueuePriorityId_Type=Unsigned32
_WwpLeosDpTsQEgressPortQueueGroupQueuePriorityId_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueuePriorityId=_WwpLeosDpTsQEgressPortQueueGroupQueuePriorityId_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,2,1,3),_WwpLeosDpTsQEgressPortQueueGroupQueuePriorityId_Type())
wwpLeosDpTsQEgressPortQueueGroupQueuePriorityId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueuePriorityId.setStatus(_A)
class _WwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_WwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight_Type.__name__=_G
_WwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight=_WwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,2,1,4),_WwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQueueSize_Type=Unsigned32
_WwpLeosDpTsQEgressPortQueueGroupQueueSize_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueSize=_WwpLeosDpTsQEgressPortQueueGroupQueueSize_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,2,1,5),_WwpLeosDpTsQEgressPortQueueGroupQueueSize_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueSize.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueSize.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQueueCIR_Type=Unsigned32
_WwpLeosDpTsQEgressPortQueueGroupQueueCIR_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueCIR=_WwpLeosDpTsQEgressPortQueueGroupQueueCIR_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,2,1,6),_WwpLeosDpTsQEgressPortQueueGroupQueueCIR_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueCIR.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueCIR.setStatus(_A)
class _WwpLeosDpTsQEgressPortQueueGroupQueueCBS_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262144))
_WwpLeosDpTsQEgressPortQueueGroupQueueCBS_Type.__name__=_G
_WwpLeosDpTsQEgressPortQueueGroupQueueCBS_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueCBS=_WwpLeosDpTsQEgressPortQueueGroupQueueCBS_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,2,1,7),_WwpLeosDpTsQEgressPortQueueGroupQueueCBS_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueCBS.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueCBS.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQueueEIR_Type=Unsigned32
_WwpLeosDpTsQEgressPortQueueGroupQueueEIR_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueEIR=_WwpLeosDpTsQEgressPortQueueGroupQueueEIR_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,2,1,8),_WwpLeosDpTsQEgressPortQueueGroupQueueEIR_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueEIR.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueEIR.setStatus(_A)
class _WwpLeosDpTsQEgressPortQueueGroupQueueEBS_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262144))
_WwpLeosDpTsQEgressPortQueueGroupQueueEBS_Type.__name__=_G
_WwpLeosDpTsQEgressPortQueueGroupQueueEBS_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueEBS=_WwpLeosDpTsQEgressPortQueueGroupQueueEBS_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,2,1,9),_WwpLeosDpTsQEgressPortQueueGroupQueueEBS_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueEBS.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueEBS.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQStatsTable_Object=MibTable
wwpLeosDpTsQEgressPortQueueGroupQStatsTable=_WwpLeosDpTsQEgressPortQueueGroupQStatsTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,3))
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQStatsTable.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQStatsEntry_Object=MibTableRow
wwpLeosDpTsQEgressPortQueueGroupQStatsEntry=_WwpLeosDpTsQEgressPortQueueGroupQStatsEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,3,1))
wwpLeosDpTsQEgressPortQueueGroupQStatsEntry.setIndexNames((0,_D,_K),(0,_D,_Q))
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQStatsEntry.setStatus(_A)
class _WwpLeosDpTsQEgressPortQueueGroupStatsQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsQEgressPortQueueGroupStatsQueueId_Type.__name__=_C
_WwpLeosDpTsQEgressPortQueueGroupStatsQueueId_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupStatsQueueId=_WwpLeosDpTsQEgressPortQueueGroupStatsQueueId_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,3,1,1),_WwpLeosDpTsQEgressPortQueueGroupStatsQueueId_Type())
wwpLeosDpTsQEgressPortQueueGroupStatsQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupStatsQueueId.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes_Type=Counter64
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes=_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,3,1,2),_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts_Type=Counter64
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts=_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,3,1,3),_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes_Type=Counter64
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes=_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,3,1,4),_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts_Type=Counter64
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts=_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,3,1,5),_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts.setStatus(_A)
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsClear_Type=TruthValue
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsClear_Object=MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueStatsClear=_WwpLeosDpTsQEgressPortQueueGroupQueueStatsClear_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,2,3,1,6),_WwpLeosDpTsQEgressPortQueueGroupQueueStatsClear_Type())
wwpLeosDpTsQEgressPortQueueGroupQueueStatsClear.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsQEgressPortQueueGroupQueueStatsClear.setStatus(_A)
_WwpLeosDpTsQRcosToCosQueueMap_ObjectIdentity=ObjectIdentity
wwpLeosDpTsQRcosToCosQueueMap=_WwpLeosDpTsQRcosToCosQueueMap_ObjectIdentity((1,3,6,1,4,1,6141,2,60,500,1,1,1,3))
_WwpLeosDpTsQueueMapTable_Object=MibTable
wwpLeosDpTsQueueMapTable=_WwpLeosDpTsQueueMapTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2))
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapTable.setStatus(_A)
_WwpLeosDpTsQueueMapEntry_Object=MibTableRow
wwpLeosDpTsQueueMapEntry=_WwpLeosDpTsQueueMapEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1))
wwpLeosDpTsQueueMapEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapEntry.setStatus(_A)
class _WwpLeosDpTsQueueMapId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosDpTsQueueMapId_Type.__name__=_C
_WwpLeosDpTsQueueMapId_Object=MibTableColumn
wwpLeosDpTsQueueMapId=_WwpLeosDpTsQueueMapId_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,1),_WwpLeosDpTsQueueMapId_Type())
wwpLeosDpTsQueueMapId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapId.setStatus(_A)
class _WwpLeosDpTsQueueMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosDpTsQueueMapName_Type.__name__=_H
_WwpLeosDpTsQueueMapName_Object=MibTableColumn
wwpLeosDpTsQueueMapName=_WwpLeosDpTsQueueMapName_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,2),_WwpLeosDpTsQueueMapName_Type())
wwpLeosDpTsQueueMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapName.setStatus(_A)
_WwpLeosDpTsQueueMapQCount_Type=Integer32
_WwpLeosDpTsQueueMapQCount_Object=MibTableColumn
wwpLeosDpTsQueueMapQCount=_WwpLeosDpTsQueueMapQCount_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,3),_WwpLeosDpTsQueueMapQCount_Type())
wwpLeosDpTsQueueMapQCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapQCount.setStatus(_A)
_WwpLeosDpTsQueueMapRCOS0_Type=Integer32
_WwpLeosDpTsQueueMapRCOS0_Object=MibTableColumn
wwpLeosDpTsQueueMapRCOS0=_WwpLeosDpTsQueueMapRCOS0_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,4),_WwpLeosDpTsQueueMapRCOS0_Type())
wwpLeosDpTsQueueMapRCOS0.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapRCOS0.setStatus(_A)
_WwpLeosDpTsQueueMapRCOS1_Type=Integer32
_WwpLeosDpTsQueueMapRCOS1_Object=MibTableColumn
wwpLeosDpTsQueueMapRCOS1=_WwpLeosDpTsQueueMapRCOS1_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,5),_WwpLeosDpTsQueueMapRCOS1_Type())
wwpLeosDpTsQueueMapRCOS1.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapRCOS1.setStatus(_A)
_WwpLeosDpTsQueueMapRCOS2_Type=Integer32
_WwpLeosDpTsQueueMapRCOS2_Object=MibTableColumn
wwpLeosDpTsQueueMapRCOS2=_WwpLeosDpTsQueueMapRCOS2_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,6),_WwpLeosDpTsQueueMapRCOS2_Type())
wwpLeosDpTsQueueMapRCOS2.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapRCOS2.setStatus(_A)
_WwpLeosDpTsQueueMapRCOS3_Type=Integer32
_WwpLeosDpTsQueueMapRCOS3_Object=MibTableColumn
wwpLeosDpTsQueueMapRCOS3=_WwpLeosDpTsQueueMapRCOS3_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,7),_WwpLeosDpTsQueueMapRCOS3_Type())
wwpLeosDpTsQueueMapRCOS3.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapRCOS3.setStatus(_A)
_WwpLeosDpTsQueueMapRCOS4_Type=Integer32
_WwpLeosDpTsQueueMapRCOS4_Object=MibTableColumn
wwpLeosDpTsQueueMapRCOS4=_WwpLeosDpTsQueueMapRCOS4_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,8),_WwpLeosDpTsQueueMapRCOS4_Type())
wwpLeosDpTsQueueMapRCOS4.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapRCOS4.setStatus(_A)
_WwpLeosDpTsQueueMapRCOS5_Type=Integer32
_WwpLeosDpTsQueueMapRCOS5_Object=MibTableColumn
wwpLeosDpTsQueueMapRCOS5=_WwpLeosDpTsQueueMapRCOS5_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,9),_WwpLeosDpTsQueueMapRCOS5_Type())
wwpLeosDpTsQueueMapRCOS5.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapRCOS5.setStatus(_A)
_WwpLeosDpTsQueueMapRCOS6_Type=Integer32
_WwpLeosDpTsQueueMapRCOS6_Object=MibTableColumn
wwpLeosDpTsQueueMapRCOS6=_WwpLeosDpTsQueueMapRCOS6_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,10),_WwpLeosDpTsQueueMapRCOS6_Type())
wwpLeosDpTsQueueMapRCOS6.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapRCOS6.setStatus(_A)
_WwpLeosDpTsQueueMapRCOS7_Type=Integer32
_WwpLeosDpTsQueueMapRCOS7_Object=MibTableColumn
wwpLeosDpTsQueueMapRCOS7=_WwpLeosDpTsQueueMapRCOS7_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,11),_WwpLeosDpTsQueueMapRCOS7_Type())
wwpLeosDpTsQueueMapRCOS7.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapRCOS7.setStatus(_A)
_WwpLeosDpTsQueueMapRowStatus_Type=RowStatus
_WwpLeosDpTsQueueMapRowStatus_Object=MibTableColumn
wwpLeosDpTsQueueMapRowStatus=_WwpLeosDpTsQueueMapRowStatus_Object((1,3,6,1,4,1,6141,2,60,500,1,1,1,3,2,1,12),_WwpLeosDpTsQueueMapRowStatus_Type())
wwpLeosDpTsQueueMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsQueueMapRowStatus.setStatus(_A)
_WwpLeosDpTsCosMapping_ObjectIdentity=ObjectIdentity
wwpLeosDpTsCosMapping=_WwpLeosDpTsCosMapping_ObjectIdentity((1,3,6,1,4,1,6141,2,60,500,1,1,2))
_WwpLeosDpTsCosMapProfileTable_Object=MibTable
wwpLeosDpTsCosMapProfileTable=_WwpLeosDpTsCosMapProfileTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,1))
if mibBuilder.loadTexts:wwpLeosDpTsCosMapProfileTable.setStatus(_A)
_WwpLeosDpTsCosMapProfileEntry_Object=MibTableRow
wwpLeosDpTsCosMapProfileEntry=_WwpLeosDpTsCosMapProfileEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,1,1))
wwpLeosDpTsCosMapProfileEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:wwpLeosDpTsCosMapProfileEntry.setStatus(_A)
class _WwpLeosDpTsCosMapProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosDpTsCosMapProfileId_Type.__name__=_C
_WwpLeosDpTsCosMapProfileId_Object=MibTableColumn
wwpLeosDpTsCosMapProfileId=_WwpLeosDpTsCosMapProfileId_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,1,1,1),_WwpLeosDpTsCosMapProfileId_Type())
wwpLeosDpTsCosMapProfileId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsCosMapProfileId.setStatus(_A)
class _WwpLeosDpTsCosMapProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_WwpLeosDpTsCosMapProfileName_Type.__name__=_H
_WwpLeosDpTsCosMapProfileName_Object=MibTableColumn
wwpLeosDpTsCosMapProfileName=_WwpLeosDpTsCosMapProfileName_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,1,1,2),_WwpLeosDpTsCosMapProfileName_Type())
wwpLeosDpTsCosMapProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsCosMapProfileName.setStatus(_A)
_WwpLeosDpTsCosMapRowStatus_Type=RowStatus
_WwpLeosDpTsCosMapRowStatus_Object=MibTableColumn
wwpLeosDpTsCosMapRowStatus=_WwpLeosDpTsCosMapRowStatus_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,1,1,3),_WwpLeosDpTsCosMapRowStatus_Type())
wwpLeosDpTsCosMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsCosMapRowStatus.setStatus(_A)
_WwpLeosDpTsDot1dCosMapTable_Object=MibTable
wwpLeosDpTsDot1dCosMapTable=_WwpLeosDpTsDot1dCosMapTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,2))
if mibBuilder.loadTexts:wwpLeosDpTsDot1dCosMapTable.setStatus(_S)
_WwpLeosDpTsDot1dCosMapEntry_Object=MibTableRow
wwpLeosDpTsDot1dCosMapEntry=_WwpLeosDpTsDot1dCosMapEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,2,1))
wwpLeosDpTsDot1dCosMapEntry.setIndexNames((0,_D,_I),(0,_D,_T))
if mibBuilder.loadTexts:wwpLeosDpTsDot1dCosMapEntry.setStatus(_S)
class _WwpLeosDpTsDot1dCosMapDot1dValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsDot1dCosMapDot1dValue_Type.__name__=_C
_WwpLeosDpTsDot1dCosMapDot1dValue_Object=MibTableColumn
wwpLeosDpTsDot1dCosMapDot1dValue=_WwpLeosDpTsDot1dCosMapDot1dValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,2,1,1),_WwpLeosDpTsDot1dCosMapDot1dValue_Type())
wwpLeosDpTsDot1dCosMapDot1dValue.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsDot1dCosMapDot1dValue.setStatus(_A)
class _WwpLeosDpTsDot1dCosMapRCOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsDot1dCosMapRCOS_Type.__name__=_C
_WwpLeosDpTsDot1dCosMapRCOS_Object=MibTableColumn
wwpLeosDpTsDot1dCosMapRCOS=_WwpLeosDpTsDot1dCosMapRCOS_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,2,1,2),_WwpLeosDpTsDot1dCosMapRCOS_Type())
wwpLeosDpTsDot1dCosMapRCOS.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsDot1dCosMapRCOS.setStatus(_A)
_WwpLeosDpTsDscpCosMapTable_Object=MibTable
wwpLeosDpTsDscpCosMapTable=_WwpLeosDpTsDscpCosMapTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,3))
if mibBuilder.loadTexts:wwpLeosDpTsDscpCosMapTable.setStatus(_A)
_WwpLeosDpTsDscpCosMapEntry_Object=MibTableRow
wwpLeosDpTsDscpCosMapEntry=_WwpLeosDpTsDscpCosMapEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,3,1))
wwpLeosDpTsDscpCosMapEntry.setIndexNames((0,_D,_I),(0,_D,_U))
if mibBuilder.loadTexts:wwpLeosDpTsDscpCosMapEntry.setStatus(_A)
class _WwpLeosDpTsDscpCosMapDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_WwpLeosDpTsDscpCosMapDscpValue_Type.__name__=_C
_WwpLeosDpTsDscpCosMapDscpValue_Object=MibTableColumn
wwpLeosDpTsDscpCosMapDscpValue=_WwpLeosDpTsDscpCosMapDscpValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,3,1,1),_WwpLeosDpTsDscpCosMapDscpValue_Type())
wwpLeosDpTsDscpCosMapDscpValue.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsDscpCosMapDscpValue.setStatus(_A)
class _WwpLeosDpTsDscpCosMapRCOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsDscpCosMapRCOS_Type.__name__=_C
_WwpLeosDpTsDscpCosMapRCOS_Object=MibTableColumn
wwpLeosDpTsDscpCosMapRCOS=_WwpLeosDpTsDscpCosMapRCOS_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,3,1,2),_WwpLeosDpTsDscpCosMapRCOS_Type())
wwpLeosDpTsDscpCosMapRCOS.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsDscpCosMapRCOS.setStatus(_A)
_WwpLeosDpTsDscpCosMapRColorValue_Type=DpTsRCosMappingColor
_WwpLeosDpTsDscpCosMapRColorValue_Object=MibTableColumn
wwpLeosDpTsDscpCosMapRColorValue=_WwpLeosDpTsDscpCosMapRColorValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,3,1,3),_WwpLeosDpTsDscpCosMapRColorValue_Type())
wwpLeosDpTsDscpCosMapRColorValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsDscpCosMapRColorValue.setStatus(_A)
_WwpLeosDpTsDot1dDeiCosMapTable_Object=MibTable
wwpLeosDpTsDot1dDeiCosMapTable=_WwpLeosDpTsDot1dDeiCosMapTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,4))
if mibBuilder.loadTexts:wwpLeosDpTsDot1dDeiCosMapTable.setStatus(_A)
_WwpLeosDpTsDot1dDeiCosMapEntry_Object=MibTableRow
wwpLeosDpTsDot1dDeiCosMapEntry=_WwpLeosDpTsDot1dDeiCosMapEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,4,1))
wwpLeosDpTsDot1dDeiCosMapEntry.setIndexNames((0,_D,_I),(0,_D,_V),(0,_D,_W))
if mibBuilder.loadTexts:wwpLeosDpTsDot1dDeiCosMapEntry.setStatus(_A)
class _WwpLeosDpTsDot1dDeiCosMapDot1dValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsDot1dDeiCosMapDot1dValue_Type.__name__=_C
_WwpLeosDpTsDot1dDeiCosMapDot1dValue_Object=MibTableColumn
wwpLeosDpTsDot1dDeiCosMapDot1dValue=_WwpLeosDpTsDot1dDeiCosMapDot1dValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,4,1,1),_WwpLeosDpTsDot1dDeiCosMapDot1dValue_Type())
wwpLeosDpTsDot1dDeiCosMapDot1dValue.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsDot1dDeiCosMapDot1dValue.setStatus(_A)
class _WwpLeosDpTsDot1dDeiCosMapDeiValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WwpLeosDpTsDot1dDeiCosMapDeiValue_Type.__name__=_C
_WwpLeosDpTsDot1dDeiCosMapDeiValue_Object=MibTableColumn
wwpLeosDpTsDot1dDeiCosMapDeiValue=_WwpLeosDpTsDot1dDeiCosMapDeiValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,4,1,2),_WwpLeosDpTsDot1dDeiCosMapDeiValue_Type())
wwpLeosDpTsDot1dDeiCosMapDeiValue.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsDot1dDeiCosMapDeiValue.setStatus(_A)
class _WwpLeosDpTsDot1dDeiCosMapRCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsDot1dDeiCosMapRCosValue_Type.__name__=_C
_WwpLeosDpTsDot1dDeiCosMapRCosValue_Object=MibTableColumn
wwpLeosDpTsDot1dDeiCosMapRCosValue=_WwpLeosDpTsDot1dDeiCosMapRCosValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,4,1,3),_WwpLeosDpTsDot1dDeiCosMapRCosValue_Type())
wwpLeosDpTsDot1dDeiCosMapRCosValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsDot1dDeiCosMapRCosValue.setStatus(_A)
_WwpLeosDpTsDot1dDeiCosMapRColorValue_Type=DpTsRCosMappingColor
_WwpLeosDpTsDot1dDeiCosMapRColorValue_Object=MibTableColumn
wwpLeosDpTsDot1dDeiCosMapRColorValue=_WwpLeosDpTsDot1dDeiCosMapRColorValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,4,1,4),_WwpLeosDpTsDot1dDeiCosMapRColorValue_Type())
wwpLeosDpTsDot1dDeiCosMapRColorValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsDot1dDeiCosMapRColorValue.setStatus(_A)
_WwpLeosDpTsMplsTcCosMapTable_Object=MibTable
wwpLeosDpTsMplsTcCosMapTable=_WwpLeosDpTsMplsTcCosMapTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,5))
if mibBuilder.loadTexts:wwpLeosDpTsMplsTcCosMapTable.setStatus(_A)
_WwpLeosDpTsMplsTcCosMapEntry_Object=MibTableRow
wwpLeosDpTsMplsTcCosMapEntry=_WwpLeosDpTsMplsTcCosMapEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,5,1))
wwpLeosDpTsMplsTcCosMapEntry.setIndexNames((0,_D,_I),(0,_D,_X))
if mibBuilder.loadTexts:wwpLeosDpTsMplsTcCosMapEntry.setStatus(_A)
class _WwpLeosDpTsMplsTcCosMapMplsTcValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsMplsTcCosMapMplsTcValue_Type.__name__=_C
_WwpLeosDpTsMplsTcCosMapMplsTcValue_Object=MibTableColumn
wwpLeosDpTsMplsTcCosMapMplsTcValue=_WwpLeosDpTsMplsTcCosMapMplsTcValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,5,1,1),_WwpLeosDpTsMplsTcCosMapMplsTcValue_Type())
wwpLeosDpTsMplsTcCosMapMplsTcValue.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsMplsTcCosMapMplsTcValue.setStatus(_A)
class _WwpLeosDpTsMplsTcCosMapRCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsMplsTcCosMapRCosValue_Type.__name__=_C
_WwpLeosDpTsMplsTcCosMapRCosValue_Object=MibTableColumn
wwpLeosDpTsMplsTcCosMapRCosValue=_WwpLeosDpTsMplsTcCosMapRCosValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,5,1,2),_WwpLeosDpTsMplsTcCosMapRCosValue_Type())
wwpLeosDpTsMplsTcCosMapRCosValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsMplsTcCosMapRCosValue.setStatus(_A)
_WwpLeosDpTsMplsTcCosMapRColorValue_Type=DpTsRCosMappingColor
_WwpLeosDpTsMplsTcCosMapRColorValue_Object=MibTableColumn
wwpLeosDpTsMplsTcCosMapRColorValue=_WwpLeosDpTsMplsTcCosMapRColorValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,2,5,1,3),_WwpLeosDpTsMplsTcCosMapRColorValue_Type())
wwpLeosDpTsMplsTcCosMapRColorValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsMplsTcCosMapRColorValue.setStatus(_A)
_WwpLeosDpTsFrameCosMapping_ObjectIdentity=ObjectIdentity
wwpLeosDpTsFrameCosMapping=_WwpLeosDpTsFrameCosMapping_ObjectIdentity((1,3,6,1,4,1,6141,2,60,500,1,1,3))
_WwpLeosDpTsFrameCosMapProfileTable_Object=MibTable
wwpLeosDpTsFrameCosMapProfileTable=_WwpLeosDpTsFrameCosMapProfileTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,1))
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapProfileTable.setStatus(_A)
_WwpLeosDpTsFrameCosMapProfileEntry_Object=MibTableRow
wwpLeosDpTsFrameCosMapProfileEntry=_WwpLeosDpTsFrameCosMapProfileEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,1,1))
wwpLeosDpTsFrameCosMapProfileEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapProfileEntry.setStatus(_A)
class _WwpLeosDpTsFrameCosMapProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosDpTsFrameCosMapProfileId_Type.__name__=_C
_WwpLeosDpTsFrameCosMapProfileId_Object=MibTableColumn
wwpLeosDpTsFrameCosMapProfileId=_WwpLeosDpTsFrameCosMapProfileId_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,1,1,1),_WwpLeosDpTsFrameCosMapProfileId_Type())
wwpLeosDpTsFrameCosMapProfileId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapProfileId.setStatus(_A)
class _WwpLeosDpTsFrameCosMapProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_WwpLeosDpTsFrameCosMapProfileName_Type.__name__=_H
_WwpLeosDpTsFrameCosMapProfileName_Object=MibTableColumn
wwpLeosDpTsFrameCosMapProfileName=_WwpLeosDpTsFrameCosMapProfileName_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,1,1,2),_WwpLeosDpTsFrameCosMapProfileName_Type())
wwpLeosDpTsFrameCosMapProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapProfileName.setStatus(_A)
_WwpLeosDpTsFrameCosMapRowStatus_Type=RowStatus
_WwpLeosDpTsFrameCosMapRowStatus_Object=MibTableColumn
wwpLeosDpTsFrameCosMapRowStatus=_WwpLeosDpTsFrameCosMapRowStatus_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,1,1,3),_WwpLeosDpTsFrameCosMapRowStatus_Type())
wwpLeosDpTsFrameCosMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapRowStatus.setStatus(_A)
_WwpLeosDpTsFrameCosMapTable_Object=MibTable
wwpLeosDpTsFrameCosMapTable=_WwpLeosDpTsFrameCosMapTable_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,2))
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapTable.setStatus(_A)
_WwpLeosDpTsFrameCosMapEntry_Object=MibTableRow
wwpLeosDpTsFrameCosMapEntry=_WwpLeosDpTsFrameCosMapEntry_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,2,1))
wwpLeosDpTsFrameCosMapEntry.setIndexNames((0,_D,_L),(0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapEntry.setStatus(_A)
class _WwpLeosDpTsFrameCosMapRCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsFrameCosMapRCosValue_Type.__name__=_C
_WwpLeosDpTsFrameCosMapRCosValue_Object=MibTableColumn
wwpLeosDpTsFrameCosMapRCosValue=_WwpLeosDpTsFrameCosMapRCosValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,2,1,1),_WwpLeosDpTsFrameCosMapRCosValue_Type())
wwpLeosDpTsFrameCosMapRCosValue.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapRCosValue.setStatus(_A)
_WwpLeosDpTsFrameCosMapRColorValue_Type=DpTsRCosMappingColor
_WwpLeosDpTsFrameCosMapRColorValue_Object=MibTableColumn
wwpLeosDpTsFrameCosMapRColorValue=_WwpLeosDpTsFrameCosMapRColorValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,2,1,2),_WwpLeosDpTsFrameCosMapRColorValue_Type())
wwpLeosDpTsFrameCosMapRColorValue.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapRColorValue.setStatus(_A)
class _WwpLeosDpTsFrameCosMapDot1dValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsFrameCosMapDot1dValue_Type.__name__=_C
_WwpLeosDpTsFrameCosMapDot1dValue_Object=MibTableColumn
wwpLeosDpTsFrameCosMapDot1dValue=_WwpLeosDpTsFrameCosMapDot1dValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,2,1,3),_WwpLeosDpTsFrameCosMapDot1dValue_Type())
wwpLeosDpTsFrameCosMapDot1dValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapDot1dValue.setStatus(_A)
class _WwpLeosDpTsFrameCosMapDot1dDeiValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WwpLeosDpTsFrameCosMapDot1dDeiValue_Type.__name__=_C
_WwpLeosDpTsFrameCosMapDot1dDeiValue_Object=MibTableColumn
wwpLeosDpTsFrameCosMapDot1dDeiValue=_WwpLeosDpTsFrameCosMapDot1dDeiValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,2,1,4),_WwpLeosDpTsFrameCosMapDot1dDeiValue_Type())
wwpLeosDpTsFrameCosMapDot1dDeiValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapDot1dDeiValue.setStatus(_A)
class _WwpLeosDpTsFrameCosMapMplsTcValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosDpTsFrameCosMapMplsTcValue_Type.__name__=_C
_WwpLeosDpTsFrameCosMapMplsTcValue_Object=MibTableColumn
wwpLeosDpTsFrameCosMapMplsTcValue=_WwpLeosDpTsFrameCosMapMplsTcValue_Object((1,3,6,1,4,1,6141,2,60,500,1,1,3,2,1,5),_WwpLeosDpTsFrameCosMapMplsTcValue_Type())
wwpLeosDpTsFrameCosMapMplsTcValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosDpTsFrameCosMapMplsTcValue.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'DpTsQSredDropProbability':DpTsQSredDropProbability,'DpTsQWredSimpleMaxDropProbability':DpTsQWredSimpleMaxDropProbability,'DpTsRCosMappingColor':DpTsRCosMappingColor,'wwpLeosDataplaneMIB':wwpLeosDataplaneMIB,'wwpLeosDpMIBObjects':wwpLeosDpMIBObjects,'wwpLeosDpTs':wwpLeosDpTs,'wwpLeosDpTsQueuing':wwpLeosDpTsQueuing,'wwpLeosDpTsQCongestionAvoidanceProfile':wwpLeosDpTsQCongestionAvoidanceProfile,'wwpLeosDpTsQCAProfileSREDTable':wwpLeosDpTsQCAProfileSREDTable,'wwpLeosDpTsQCAProfileSREDEntry':wwpLeosDpTsQCAProfileSREDEntry,_N:wwpLeosDpTsQCAProfileSREDId,'wwpLeosDpTsQCAProfileSREDName':wwpLeosDpTsQCAProfileSREDName,'wwpLeosDpTsQCAProfileSREDGreenThreshold':wwpLeosDpTsQCAProfileSREDGreenThreshold,'wwpLeosDpTsQCAProfileSREDGreenDropProbability':wwpLeosDpTsQCAProfileSREDGreenDropProbability,'wwpLeosDpTsQCAProfileSREDYellowThreshold':wwpLeosDpTsQCAProfileSREDYellowThreshold,'wwpLeosDpTsQCAProfileSREDYellowDropProbability':wwpLeosDpTsQCAProfileSREDYellowDropProbability,'wwpLeosDpTsQCAProfileSREDRowStatus':wwpLeosDpTsQCAProfileSREDRowStatus,'wwpLeosDpTsQCAProfileWREDSimpleTable':wwpLeosDpTsQCAProfileWREDSimpleTable,'wwpLeosDpTsQCAProfileWREDSimpleEntry':wwpLeosDpTsQCAProfileWREDSimpleEntry,_O:wwpLeosDpTsQCAProfileWREDSimpleId,'wwpLeosDpTsQCAProfileWREDSimpleName':wwpLeosDpTsQCAProfileWREDSimpleName,'wwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold':wwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold,'wwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold':wwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold,'wwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability':wwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability,'wwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold':wwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold,'wwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold':wwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold,'wwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability':wwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability,'wwpLeosDpTsQCAProfileWREDSimpleRowStatus':wwpLeosDpTsQCAProfileWREDSimpleRowStatus,'wwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold':wwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold,'wwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold':wwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold,'wwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability':wwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability,'wwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold':wwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold,'wwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold':wwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold,'wwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability':wwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability,'wwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold':wwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold,'wwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold':wwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold,'wwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability':wwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability,'wwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit':wwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit,'wwpLeosDpTsQEgressPortQueueGroup':wwpLeosDpTsQEgressPortQueueGroup,'wwpLeosDpTsQEgressPortQueueGroupTable':wwpLeosDpTsQEgressPortQueueGroupTable,'wwpLeosDpTsQEgressPortQueueGroupEntry':wwpLeosDpTsQEgressPortQueueGroupEntry,_K:wwpLeosDpTsQEgressPortQueueGroupId,'wwpLeosDpTsQEgressPortQueueGroupQCount':wwpLeosDpTsQEgressPortQueueGroupQCount,'wwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm':wwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm,'wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth':wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth,'wwpLeosDpTsQEgressPortQueueGroupBurstSize':wwpLeosDpTsQEgressPortQueueGroupBurstSize,'wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity':wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity,'wwpLeosDpTsQEgressPortQueueGroupQConfigTable':wwpLeosDpTsQEgressPortQueueGroupQConfigTable,'wwpLeosDpTsQEgressPortQueueGroupQConfigEntry':wwpLeosDpTsQEgressPortQueueGroupQConfigEntry,_P:wwpLeosDpTsQEgressPortQueueGroupQueueId,'wwpLeosDpTsQEgressPortQueueGroupQueueCAPId':wwpLeosDpTsQEgressPortQueueGroupQueueCAPId,'wwpLeosDpTsQEgressPortQueueGroupQueuePriorityId':wwpLeosDpTsQEgressPortQueueGroupQueuePriorityId,'wwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight':wwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight,'wwpLeosDpTsQEgressPortQueueGroupQueueSize':wwpLeosDpTsQEgressPortQueueGroupQueueSize,'wwpLeosDpTsQEgressPortQueueGroupQueueCIR':wwpLeosDpTsQEgressPortQueueGroupQueueCIR,'wwpLeosDpTsQEgressPortQueueGroupQueueCBS':wwpLeosDpTsQEgressPortQueueGroupQueueCBS,'wwpLeosDpTsQEgressPortQueueGroupQueueEIR':wwpLeosDpTsQEgressPortQueueGroupQueueEIR,'wwpLeosDpTsQEgressPortQueueGroupQueueEBS':wwpLeosDpTsQEgressPortQueueGroupQueueEBS,'wwpLeosDpTsQEgressPortQueueGroupQStatsTable':wwpLeosDpTsQEgressPortQueueGroupQStatsTable,'wwpLeosDpTsQEgressPortQueueGroupQStatsEntry':wwpLeosDpTsQEgressPortQueueGroupQStatsEntry,_Q:wwpLeosDpTsQEgressPortQueueGroupStatsQueueId,'wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes':wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes,'wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts':wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts,'wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes':wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes,'wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts':wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts,'wwpLeosDpTsQEgressPortQueueGroupQueueStatsClear':wwpLeosDpTsQEgressPortQueueGroupQueueStatsClear,'wwpLeosDpTsQRcosToCosQueueMap':wwpLeosDpTsQRcosToCosQueueMap,'wwpLeosDpTsQueueMapTable':wwpLeosDpTsQueueMapTable,'wwpLeosDpTsQueueMapEntry':wwpLeosDpTsQueueMapEntry,_R:wwpLeosDpTsQueueMapId,'wwpLeosDpTsQueueMapName':wwpLeosDpTsQueueMapName,'wwpLeosDpTsQueueMapQCount':wwpLeosDpTsQueueMapQCount,'wwpLeosDpTsQueueMapRCOS0':wwpLeosDpTsQueueMapRCOS0,'wwpLeosDpTsQueueMapRCOS1':wwpLeosDpTsQueueMapRCOS1,'wwpLeosDpTsQueueMapRCOS2':wwpLeosDpTsQueueMapRCOS2,'wwpLeosDpTsQueueMapRCOS3':wwpLeosDpTsQueueMapRCOS3,'wwpLeosDpTsQueueMapRCOS4':wwpLeosDpTsQueueMapRCOS4,'wwpLeosDpTsQueueMapRCOS5':wwpLeosDpTsQueueMapRCOS5,'wwpLeosDpTsQueueMapRCOS6':wwpLeosDpTsQueueMapRCOS6,'wwpLeosDpTsQueueMapRCOS7':wwpLeosDpTsQueueMapRCOS7,'wwpLeosDpTsQueueMapRowStatus':wwpLeosDpTsQueueMapRowStatus,'wwpLeosDpTsCosMapping':wwpLeosDpTsCosMapping,'wwpLeosDpTsCosMapProfileTable':wwpLeosDpTsCosMapProfileTable,'wwpLeosDpTsCosMapProfileEntry':wwpLeosDpTsCosMapProfileEntry,_I:wwpLeosDpTsCosMapProfileId,'wwpLeosDpTsCosMapProfileName':wwpLeosDpTsCosMapProfileName,'wwpLeosDpTsCosMapRowStatus':wwpLeosDpTsCosMapRowStatus,'wwpLeosDpTsDot1dCosMapTable':wwpLeosDpTsDot1dCosMapTable,'wwpLeosDpTsDot1dCosMapEntry':wwpLeosDpTsDot1dCosMapEntry,_T:wwpLeosDpTsDot1dCosMapDot1dValue,'wwpLeosDpTsDot1dCosMapRCOS':wwpLeosDpTsDot1dCosMapRCOS,'wwpLeosDpTsDscpCosMapTable':wwpLeosDpTsDscpCosMapTable,'wwpLeosDpTsDscpCosMapEntry':wwpLeosDpTsDscpCosMapEntry,_U:wwpLeosDpTsDscpCosMapDscpValue,'wwpLeosDpTsDscpCosMapRCOS':wwpLeosDpTsDscpCosMapRCOS,'wwpLeosDpTsDscpCosMapRColorValue':wwpLeosDpTsDscpCosMapRColorValue,'wwpLeosDpTsDot1dDeiCosMapTable':wwpLeosDpTsDot1dDeiCosMapTable,'wwpLeosDpTsDot1dDeiCosMapEntry':wwpLeosDpTsDot1dDeiCosMapEntry,_V:wwpLeosDpTsDot1dDeiCosMapDot1dValue,_W:wwpLeosDpTsDot1dDeiCosMapDeiValue,'wwpLeosDpTsDot1dDeiCosMapRCosValue':wwpLeosDpTsDot1dDeiCosMapRCosValue,'wwpLeosDpTsDot1dDeiCosMapRColorValue':wwpLeosDpTsDot1dDeiCosMapRColorValue,'wwpLeosDpTsMplsTcCosMapTable':wwpLeosDpTsMplsTcCosMapTable,'wwpLeosDpTsMplsTcCosMapEntry':wwpLeosDpTsMplsTcCosMapEntry,_X:wwpLeosDpTsMplsTcCosMapMplsTcValue,'wwpLeosDpTsMplsTcCosMapRCosValue':wwpLeosDpTsMplsTcCosMapRCosValue,'wwpLeosDpTsMplsTcCosMapRColorValue':wwpLeosDpTsMplsTcCosMapRColorValue,'wwpLeosDpTsFrameCosMapping':wwpLeosDpTsFrameCosMapping,'wwpLeosDpTsFrameCosMapProfileTable':wwpLeosDpTsFrameCosMapProfileTable,'wwpLeosDpTsFrameCosMapProfileEntry':wwpLeosDpTsFrameCosMapProfileEntry,_L:wwpLeosDpTsFrameCosMapProfileId,'wwpLeosDpTsFrameCosMapProfileName':wwpLeosDpTsFrameCosMapProfileName,'wwpLeosDpTsFrameCosMapRowStatus':wwpLeosDpTsFrameCosMapRowStatus,'wwpLeosDpTsFrameCosMapTable':wwpLeosDpTsFrameCosMapTable,'wwpLeosDpTsFrameCosMapEntry':wwpLeosDpTsFrameCosMapEntry,_Y:wwpLeosDpTsFrameCosMapRCosValue,_Z:wwpLeosDpTsFrameCosMapRColorValue,'wwpLeosDpTsFrameCosMapDot1dValue':wwpLeosDpTsFrameCosMapDot1dValue,'wwpLeosDpTsFrameCosMapDot1dDeiValue':wwpLeosDpTsFrameCosMapDot1dDeiValue,'wwpLeosDpTsFrameCosMapMplsTcValue':wwpLeosDpTsFrameCosMapMplsTcValue})