_r='apCodecPairTranscodingHigh'
_q='apCodecPairTranscodingCurrent'
_p='apCodecName'
_o='apCodecTranscodingInUsePercentHigh'
_n='apCodecTranscodingInUsePercentCurrent'
_m='apCodecTranscodingResourcesHigh'
_l='apCodecTranscodingResourcesCurrent'
_k='apCodecTranscodingResourcesTotal'
_j='apCodecRealmCountEVRC'
_i='apCodecRealmCountAMR'
_h='apCodecRealmSessionsTranscoded'
_g='apCodecRealmSessionsTransrated'
_f='apCodecRealmSessionsTransparent'
_e='apCodecRealmCountT38'
_d='apCodecRealmCountH263'
_c='apCodecRealmCountH261'
_b='apCodecRealmCountILBC'
_a='apCodecRealmCountGSM'
_Z='apCodecRealmCountG729'
_Y='apCodecRealmCountG728'
_X='apCodecRealmCountG726-40'
_W='apCodecRealmCountG726-32'
_V='apCodecRealmCountG726-24'
_U='apCodecRealmCountG726-16'
_T='apCodecRealmCountG723'
_S='apCodecRealmCountG722'
_R='apCodecRealmCountPCMA'
_Q='apCodecRealmCountPCMU'
_P='apCodecRealmCountOther'
_O='apCodecTranscodingRealmStatsEntry'
_N='apCodecRealmStatsEntry'
_M='apCodecPairBDigitType'
_L='apCodecPairADigitType'
_K='apCodecPairBPValue'
_J='apCodecPairAPValue'
_I='apCodecPairBIndex'
_H='apCodecPairAIndex'
_G='apCodecIndex'
_F='DisplayString'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='APCODEC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
ApPercentage,=mibBuilder.importSymbols('ACMEPACKET-TC','ApPercentage')
apSigRealmStatsEntry,=mibBuilder.importSymbols('APSYSMGMT-MIB','apSigRealmStatsEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
apCodecModule=ModuleIdentity((1,3,6,1,4,1,9148,3,7))
if mibBuilder.loadTexts:apCodecModule.setRevisions(('2012-07-16 00:00','2012-06-22 10:00'))
class ApCodecDigitTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',0),('none',1),('inband',2),('rfc2833',3),('noneDual',4),('inbandTrans',5),('inbandDual',6),('rfc2833Trans',7),('rfc2833Dual',8)))
_ApCodecMIBObjects_ObjectIdentity=ObjectIdentity
apCodecMIBObjects=_ApCodecMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,7,1))
_ApCodecRealmStatsTable_Object=MibTable
apCodecRealmStatsTable=_ApCodecRealmStatsTable_Object((1,3,6,1,4,1,9148,3,7,1,1))
if mibBuilder.loadTexts:apCodecRealmStatsTable.setStatus(_A)
_ApCodecRealmStatsEntry_Object=MibTableRow
apCodecRealmStatsEntry=_ApCodecRealmStatsEntry_Object((1,3,6,1,4,1,9148,3,7,1,1,1))
if mibBuilder.loadTexts:apCodecRealmStatsEntry.setStatus(_A)
_ApCodecRealmCountOther_Type=Counter32
_ApCodecRealmCountOther_Object=MibTableColumn
apCodecRealmCountOther=_ApCodecRealmCountOther_Object((1,3,6,1,4,1,9148,3,7,1,1,1,1),_ApCodecRealmCountOther_Type())
apCodecRealmCountOther.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountOther.setStatus(_A)
_ApCodecRealmCountPCMU_Type=Counter32
_ApCodecRealmCountPCMU_Object=MibTableColumn
apCodecRealmCountPCMU=_ApCodecRealmCountPCMU_Object((1,3,6,1,4,1,9148,3,7,1,1,1,2),_ApCodecRealmCountPCMU_Type())
apCodecRealmCountPCMU.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountPCMU.setStatus(_A)
_ApCodecRealmCountPCMA_Type=Counter32
_ApCodecRealmCountPCMA_Object=MibTableColumn
apCodecRealmCountPCMA=_ApCodecRealmCountPCMA_Object((1,3,6,1,4,1,9148,3,7,1,1,1,3),_ApCodecRealmCountPCMA_Type())
apCodecRealmCountPCMA.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountPCMA.setStatus(_A)
_ApCodecRealmCountG722_Type=Counter32
_ApCodecRealmCountG722_Object=MibTableColumn
apCodecRealmCountG722=_ApCodecRealmCountG722_Object((1,3,6,1,4,1,9148,3,7,1,1,1,4),_ApCodecRealmCountG722_Type())
apCodecRealmCountG722.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountG722.setStatus(_A)
_ApCodecRealmCountG723_Type=Counter32
_ApCodecRealmCountG723_Object=MibTableColumn
apCodecRealmCountG723=_ApCodecRealmCountG723_Object((1,3,6,1,4,1,9148,3,7,1,1,1,5),_ApCodecRealmCountG723_Type())
apCodecRealmCountG723.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountG723.setStatus(_A)
_ApCodecRealmCountG726_16_Type=Counter32
_ApCodecRealmCountG726_16_Object=MibTableColumn
apCodecRealmCountG726_16=_ApCodecRealmCountG726_16_Object((1,3,6,1,4,1,9148,3,7,1,1,1,6),_ApCodecRealmCountG726_16_Type())
apCodecRealmCountG726_16.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountG726_16.setStatus(_A)
_ApCodecRealmCountG726_24_Type=Counter32
_ApCodecRealmCountG726_24_Object=MibTableColumn
apCodecRealmCountG726_24=_ApCodecRealmCountG726_24_Object((1,3,6,1,4,1,9148,3,7,1,1,1,7),_ApCodecRealmCountG726_24_Type())
apCodecRealmCountG726_24.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountG726_24.setStatus(_A)
_ApCodecRealmCountG726_32_Type=Counter32
_ApCodecRealmCountG726_32_Object=MibTableColumn
apCodecRealmCountG726_32=_ApCodecRealmCountG726_32_Object((1,3,6,1,4,1,9148,3,7,1,1,1,8),_ApCodecRealmCountG726_32_Type())
apCodecRealmCountG726_32.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountG726_32.setStatus(_A)
_ApCodecRealmCountG726_40_Type=Counter32
_ApCodecRealmCountG726_40_Object=MibTableColumn
apCodecRealmCountG726_40=_ApCodecRealmCountG726_40_Object((1,3,6,1,4,1,9148,3,7,1,1,1,9),_ApCodecRealmCountG726_40_Type())
apCodecRealmCountG726_40.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountG726_40.setStatus(_A)
_ApCodecRealmCountG728_Type=Counter32
_ApCodecRealmCountG728_Object=MibTableColumn
apCodecRealmCountG728=_ApCodecRealmCountG728_Object((1,3,6,1,4,1,9148,3,7,1,1,1,10),_ApCodecRealmCountG728_Type())
apCodecRealmCountG728.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountG728.setStatus(_A)
_ApCodecRealmCountG729_Type=Counter32
_ApCodecRealmCountG729_Object=MibTableColumn
apCodecRealmCountG729=_ApCodecRealmCountG729_Object((1,3,6,1,4,1,9148,3,7,1,1,1,11),_ApCodecRealmCountG729_Type())
apCodecRealmCountG729.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountG729.setStatus(_A)
_ApCodecRealmCountGSM_Type=Counter32
_ApCodecRealmCountGSM_Object=MibTableColumn
apCodecRealmCountGSM=_ApCodecRealmCountGSM_Object((1,3,6,1,4,1,9148,3,7,1,1,1,12),_ApCodecRealmCountGSM_Type())
apCodecRealmCountGSM.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountGSM.setStatus(_A)
_ApCodecRealmCountILBC_Type=Counter32
_ApCodecRealmCountILBC_Object=MibTableColumn
apCodecRealmCountILBC=_ApCodecRealmCountILBC_Object((1,3,6,1,4,1,9148,3,7,1,1,1,13),_ApCodecRealmCountILBC_Type())
apCodecRealmCountILBC.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountILBC.setStatus(_A)
_ApCodecRealmCountAMR_Type=Counter32
_ApCodecRealmCountAMR_Object=MibTableColumn
apCodecRealmCountAMR=_ApCodecRealmCountAMR_Object((1,3,6,1,4,1,9148,3,7,1,1,1,14),_ApCodecRealmCountAMR_Type())
apCodecRealmCountAMR.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountAMR.setStatus(_A)
_ApCodecRealmCountEVRC_Type=Counter32
_ApCodecRealmCountEVRC_Object=MibTableColumn
apCodecRealmCountEVRC=_ApCodecRealmCountEVRC_Object((1,3,6,1,4,1,9148,3,7,1,1,1,15),_ApCodecRealmCountEVRC_Type())
apCodecRealmCountEVRC.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountEVRC.setStatus(_A)
_ApCodecRealmCountH261_Type=Counter32
_ApCodecRealmCountH261_Object=MibTableColumn
apCodecRealmCountH261=_ApCodecRealmCountH261_Object((1,3,6,1,4,1,9148,3,7,1,1,1,16),_ApCodecRealmCountH261_Type())
apCodecRealmCountH261.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountH261.setStatus(_A)
_ApCodecRealmCountH263_Type=Counter32
_ApCodecRealmCountH263_Object=MibTableColumn
apCodecRealmCountH263=_ApCodecRealmCountH263_Object((1,3,6,1,4,1,9148,3,7,1,1,1,17),_ApCodecRealmCountH263_Type())
apCodecRealmCountH263.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountH263.setStatus(_A)
_ApCodecRealmCountT38_Type=Counter32
_ApCodecRealmCountT38_Object=MibTableColumn
apCodecRealmCountT38=_ApCodecRealmCountT38_Object((1,3,6,1,4,1,9148,3,7,1,1,1,18),_ApCodecRealmCountT38_Type())
apCodecRealmCountT38.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmCountT38.setStatus(_A)
_ApCodecTranscodingMIBObjects_ObjectIdentity=ObjectIdentity
apCodecTranscodingMIBObjects=_ApCodecTranscodingMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,7,2))
_ApCodecTranscodingRealmStatsTable_Object=MibTable
apCodecTranscodingRealmStatsTable=_ApCodecTranscodingRealmStatsTable_Object((1,3,6,1,4,1,9148,3,7,2,1))
if mibBuilder.loadTexts:apCodecTranscodingRealmStatsTable.setStatus(_A)
_ApCodecTranscodingRealmStatsEntry_Object=MibTableRow
apCodecTranscodingRealmStatsEntry=_ApCodecTranscodingRealmStatsEntry_Object((1,3,6,1,4,1,9148,3,7,2,1,1))
if mibBuilder.loadTexts:apCodecTranscodingRealmStatsEntry.setStatus(_A)
_ApCodecRealmSessionsTransparent_Type=Counter32
_ApCodecRealmSessionsTransparent_Object=MibTableColumn
apCodecRealmSessionsTransparent=_ApCodecRealmSessionsTransparent_Object((1,3,6,1,4,1,9148,3,7,2,1,1,1),_ApCodecRealmSessionsTransparent_Type())
apCodecRealmSessionsTransparent.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmSessionsTransparent.setStatus(_A)
_ApCodecRealmSessionsTransrated_Type=Counter32
_ApCodecRealmSessionsTransrated_Object=MibTableColumn
apCodecRealmSessionsTransrated=_ApCodecRealmSessionsTransrated_Object((1,3,6,1,4,1,9148,3,7,2,1,1,2),_ApCodecRealmSessionsTransrated_Type())
apCodecRealmSessionsTransrated.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmSessionsTransrated.setStatus(_A)
_ApCodecRealmSessionsTranscoded_Type=Counter32
_ApCodecRealmSessionsTranscoded_Object=MibTableColumn
apCodecRealmSessionsTranscoded=_ApCodecRealmSessionsTranscoded_Object((1,3,6,1,4,1,9148,3,7,2,1,1,3),_ApCodecRealmSessionsTranscoded_Type())
apCodecRealmSessionsTranscoded.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecRealmSessionsTranscoded.setStatus(_A)
_ApCodecTranscodingResourceMIBObjects_ObjectIdentity=ObjectIdentity
apCodecTranscodingResourceMIBObjects=_ApCodecTranscodingResourceMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,7,2,2))
class _ApCodecTranscodingResourcesTotal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ApCodecTranscodingResourcesTotal_Type.__name__=_E
_ApCodecTranscodingResourcesTotal_Object=MibScalar
apCodecTranscodingResourcesTotal=_ApCodecTranscodingResourcesTotal_Object((1,3,6,1,4,1,9148,3,7,2,2,1),_ApCodecTranscodingResourcesTotal_Type())
apCodecTranscodingResourcesTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecTranscodingResourcesTotal.setStatus(_A)
_ApCodecTranscodingResourcesCurrent_Type=Gauge32
_ApCodecTranscodingResourcesCurrent_Object=MibScalar
apCodecTranscodingResourcesCurrent=_ApCodecTranscodingResourcesCurrent_Object((1,3,6,1,4,1,9148,3,7,2,2,2),_ApCodecTranscodingResourcesCurrent_Type())
apCodecTranscodingResourcesCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecTranscodingResourcesCurrent.setStatus(_A)
_ApCodecTranscodingResourcesHigh_Type=Counter32
_ApCodecTranscodingResourcesHigh_Object=MibScalar
apCodecTranscodingResourcesHigh=_ApCodecTranscodingResourcesHigh_Object((1,3,6,1,4,1,9148,3,7,2,2,3),_ApCodecTranscodingResourcesHigh_Type())
apCodecTranscodingResourcesHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecTranscodingResourcesHigh.setStatus(_A)
_ApCodecTranscodingInUsePercentCurrent_Type=ApPercentage
_ApCodecTranscodingInUsePercentCurrent_Object=MibScalar
apCodecTranscodingInUsePercentCurrent=_ApCodecTranscodingInUsePercentCurrent_Object((1,3,6,1,4,1,9148,3,7,2,2,4),_ApCodecTranscodingInUsePercentCurrent_Type())
apCodecTranscodingInUsePercentCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecTranscodingInUsePercentCurrent.setStatus(_A)
_ApCodecTranscodingInUsePercentHigh_Type=ApPercentage
_ApCodecTranscodingInUsePercentHigh_Object=MibScalar
apCodecTranscodingInUsePercentHigh=_ApCodecTranscodingInUsePercentHigh_Object((1,3,6,1,4,1,9148,3,7,2,2,5),_ApCodecTranscodingInUsePercentHigh_Type())
apCodecTranscodingInUsePercentHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecTranscodingInUsePercentHigh.setStatus(_A)
_ApCodecTable_Object=MibTable
apCodecTable=_ApCodecTable_Object((1,3,6,1,4,1,9148,3,7,2,3))
if mibBuilder.loadTexts:apCodecTable.setStatus(_A)
_ApCodecEntry_Object=MibTableRow
apCodecEntry=_ApCodecEntry_Object((1,3,6,1,4,1,9148,3,7,2,3,1))
apCodecEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:apCodecEntry.setStatus(_A)
class _ApCodecIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ApCodecIndex_Type.__name__=_E
_ApCodecIndex_Object=MibTableColumn
apCodecIndex=_ApCodecIndex_Object((1,3,6,1,4,1,9148,3,7,2,3,1,1),_ApCodecIndex_Type())
apCodecIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:apCodecIndex.setStatus(_A)
class _ApCodecName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApCodecName_Type.__name__=_F
_ApCodecName_Object=MibTableColumn
apCodecName=_ApCodecName_Object((1,3,6,1,4,1,9148,3,7,2,3,1,2),_ApCodecName_Type())
apCodecName.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecName.setStatus(_A)
_ApCodecPairStatsTable_Object=MibTable
apCodecPairStatsTable=_ApCodecPairStatsTable_Object((1,3,6,1,4,1,9148,3,7,2,4))
if mibBuilder.loadTexts:apCodecPairStatsTable.setStatus(_A)
_ApCodecPairStatsEntry_Object=MibTableRow
apCodecPairStatsEntry=_ApCodecPairStatsEntry_Object((1,3,6,1,4,1,9148,3,7,2,4,1))
apCodecPairStatsEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:apCodecPairStatsEntry.setStatus(_A)
_ApCodecPairAIndex_Type=Integer32
_ApCodecPairAIndex_Object=MibTableColumn
apCodecPairAIndex=_ApCodecPairAIndex_Object((1,3,6,1,4,1,9148,3,7,2,4,1,1),_ApCodecPairAIndex_Type())
apCodecPairAIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:apCodecPairAIndex.setStatus(_A)
_ApCodecPairBIndex_Type=Integer32
_ApCodecPairBIndex_Object=MibTableColumn
apCodecPairBIndex=_ApCodecPairBIndex_Object((1,3,6,1,4,1,9148,3,7,2,4,1,2),_ApCodecPairBIndex_Type())
apCodecPairBIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:apCodecPairBIndex.setStatus(_A)
class _ApCodecPairAPValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ApCodecPairAPValue_Type.__name__=_E
_ApCodecPairAPValue_Object=MibTableColumn
apCodecPairAPValue=_ApCodecPairAPValue_Object((1,3,6,1,4,1,9148,3,7,2,4,1,3),_ApCodecPairAPValue_Type())
apCodecPairAPValue.setMaxAccess(_D)
if mibBuilder.loadTexts:apCodecPairAPValue.setStatus(_A)
class _ApCodecPairBPValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ApCodecPairBPValue_Type.__name__=_E
_ApCodecPairBPValue_Object=MibTableColumn
apCodecPairBPValue=_ApCodecPairBPValue_Object((1,3,6,1,4,1,9148,3,7,2,4,1,4),_ApCodecPairBPValue_Type())
apCodecPairBPValue.setMaxAccess(_D)
if mibBuilder.loadTexts:apCodecPairBPValue.setStatus(_A)
_ApCodecPairADigitType_Type=ApCodecDigitTypes
_ApCodecPairADigitType_Object=MibTableColumn
apCodecPairADigitType=_ApCodecPairADigitType_Object((1,3,6,1,4,1,9148,3,7,2,4,1,5),_ApCodecPairADigitType_Type())
apCodecPairADigitType.setMaxAccess(_D)
if mibBuilder.loadTexts:apCodecPairADigitType.setStatus(_A)
_ApCodecPairBDigitType_Type=ApCodecDigitTypes
_ApCodecPairBDigitType_Object=MibTableColumn
apCodecPairBDigitType=_ApCodecPairBDigitType_Object((1,3,6,1,4,1,9148,3,7,2,4,1,6),_ApCodecPairBDigitType_Type())
apCodecPairBDigitType.setMaxAccess(_D)
if mibBuilder.loadTexts:apCodecPairBDigitType.setStatus(_A)
_ApCodecPairTranscodingCurrent_Type=Gauge32
_ApCodecPairTranscodingCurrent_Object=MibTableColumn
apCodecPairTranscodingCurrent=_ApCodecPairTranscodingCurrent_Object((1,3,6,1,4,1,9148,3,7,2,4,1,7),_ApCodecPairTranscodingCurrent_Type())
apCodecPairTranscodingCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecPairTranscodingCurrent.setStatus(_A)
_ApCodecPairTranscodingHigh_Type=Counter32
_ApCodecPairTranscodingHigh_Object=MibTableColumn
apCodecPairTranscodingHigh=_ApCodecPairTranscodingHigh_Object((1,3,6,1,4,1,9148,3,7,2,4,1,8),_ApCodecPairTranscodingHigh_Type())
apCodecPairTranscodingHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:apCodecPairTranscodingHigh.setStatus(_A)
_ApCodecNotificationObjects_ObjectIdentity=ObjectIdentity
apCodecNotificationObjects=_ApCodecNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,7,3))
_ApCodecNotificationPrefix_ObjectIdentity=ObjectIdentity
apCodecNotificationPrefix=_ApCodecNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,7,4))
_ApCodecNotifications_ObjectIdentity=ObjectIdentity
apCodecNotifications=_ApCodecNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,7,4,0))
_ApCodecConformance_ObjectIdentity=ObjectIdentity
apCodecConformance=_ApCodecConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,7,5))
_ApCodecCompliances_ObjectIdentity=ObjectIdentity
apCodecCompliances=_ApCodecCompliances_ObjectIdentity((1,3,6,1,4,1,9148,3,7,5,1))
_ApCodecGroups_ObjectIdentity=ObjectIdentity
apCodecGroups=_ApCodecGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,7,5,2))
_ApCodecNotificationsGroups_ObjectIdentity=ObjectIdentity
apCodecNotificationsGroups=_ApCodecNotificationsGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,7,5,3))
apSigRealmStatsEntry.registerAugmentions((_B,_N))
apCodecRealmStatsEntry.setIndexNames(*apSigRealmStatsEntry.getIndexNames())
apSigRealmStatsEntry.registerAugmentions((_B,_O))
apCodecTranscodingRealmStatsEntry.setIndexNames(*apSigRealmStatsEntry.getIndexNames())
apCodecRealmStatsObjectsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,7,5,2,1))
apCodecRealmStatsObjectsGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:apCodecRealmStatsObjectsGroup.setStatus(_A)
apCodecMediaProcessingObjectsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,7,5,2,2))
apCodecMediaProcessingObjectsGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:apCodecMediaProcessingObjectsGroup.setStatus(_A)
apCodecRealmStatsObjectsGroup2=ObjectGroup((1,3,6,1,4,1,9148,3,7,5,2,3))
apCodecRealmStatsObjectsGroup2.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:apCodecRealmStatsObjectsGroup2.setStatus(_A)
apCodecTranscodingStatsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,7,5,2,4))
apCodecTranscodingStatsGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:apCodecTranscodingStatsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ApCodecDigitTypes':ApCodecDigitTypes,'apCodecModule':apCodecModule,'apCodecMIBObjects':apCodecMIBObjects,'apCodecRealmStatsTable':apCodecRealmStatsTable,_N:apCodecRealmStatsEntry,_P:apCodecRealmCountOther,_Q:apCodecRealmCountPCMU,_R:apCodecRealmCountPCMA,_S:apCodecRealmCountG722,_T:apCodecRealmCountG723,_U:apCodecRealmCountG726_16,_V:apCodecRealmCountG726_24,_W:apCodecRealmCountG726_32,_X:apCodecRealmCountG726_40,_Y:apCodecRealmCountG728,_Z:apCodecRealmCountG729,_a:apCodecRealmCountGSM,_b:apCodecRealmCountILBC,_i:apCodecRealmCountAMR,_j:apCodecRealmCountEVRC,_c:apCodecRealmCountH261,_d:apCodecRealmCountH263,_e:apCodecRealmCountT38,'apCodecTranscodingMIBObjects':apCodecTranscodingMIBObjects,'apCodecTranscodingRealmStatsTable':apCodecTranscodingRealmStatsTable,_O:apCodecTranscodingRealmStatsEntry,_f:apCodecRealmSessionsTransparent,_g:apCodecRealmSessionsTransrated,_h:apCodecRealmSessionsTranscoded,'apCodecTranscodingResourceMIBObjects':apCodecTranscodingResourceMIBObjects,_k:apCodecTranscodingResourcesTotal,_l:apCodecTranscodingResourcesCurrent,_m:apCodecTranscodingResourcesHigh,_n:apCodecTranscodingInUsePercentCurrent,_o:apCodecTranscodingInUsePercentHigh,'apCodecTable':apCodecTable,'apCodecEntry':apCodecEntry,_G:apCodecIndex,_p:apCodecName,'apCodecPairStatsTable':apCodecPairStatsTable,'apCodecPairStatsEntry':apCodecPairStatsEntry,_H:apCodecPairAIndex,_I:apCodecPairBIndex,_J:apCodecPairAPValue,_K:apCodecPairBPValue,_L:apCodecPairADigitType,_M:apCodecPairBDigitType,_q:apCodecPairTranscodingCurrent,_r:apCodecPairTranscodingHigh,'apCodecNotificationObjects':apCodecNotificationObjects,'apCodecNotificationPrefix':apCodecNotificationPrefix,'apCodecNotifications':apCodecNotifications,'apCodecConformance':apCodecConformance,'apCodecCompliances':apCodecCompliances,'apCodecGroups':apCodecGroups,'apCodecRealmStatsObjectsGroup':apCodecRealmStatsObjectsGroup,'apCodecMediaProcessingObjectsGroup':apCodecMediaProcessingObjectsGroup,'apCodecRealmStatsObjectsGroup2':apCodecRealmStatsObjectsGroup2,'apCodecTranscodingStatsGroup':apCodecTranscodingStatsGroup,'apCodecNotificationsGroups':apCodecNotificationsGroups})