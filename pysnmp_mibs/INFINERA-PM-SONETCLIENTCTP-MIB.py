_q='sonetClientCtpPmRealGroup'
_p='sonetClientCtpPmGroup'
_o='sonetClientCtpPmRealTxBER'
_n='sonetClientCtpPmRealRxBER'
_m='sonetClientCtpPmRealLinePRBSErr'
_l='sonetClientCtpPmRealLinePRBSSyncErr'
_k='sonetClientCtpPmRealTribPRBSErr'
_j='sonetClientCtpPmRealTribPRBSSyncErr'
_i='sonetClientCtpPmRealCktId'
_h='sonetClientCtpPmRealTxSEFS'
_g='sonetClientCtpPmRealTxSES'
_f='sonetClientCtpPmRealTxES'
_e='sonetClientCtpPmRealTxCV'
_d='sonetClientCtpPmRealRxSEFS'
_c='sonetClientCtpPmRealRxSES'
_b='sonetClientCtpPmRealRxES'
_a='sonetClientCtpPmRealRxCV'
_Z='sonetClientCtpPmTxBER'
_Y='sonetClientCtpPmRxBER'
_X='sonetClientCtpPmLinePRBSErr'
_W='sonetClientCtpPmLinePRBSSyncErr'
_V='sonetClientCtpPmPayloadType'
_U='sonetClientCtpPmTribPRBSErr'
_T='sonetClientCtpPmTribPRBSSyncErr'
_S='sonetClientCtpPmCktId'
_R='sonetClientCtpPmTxSEFS'
_Q='sonetClientCtpPmTxSES'
_P='sonetClientCtpPmTxES'
_O='sonetClientCtpPmTxCV'
_N='sonetClientCtpPmRxSEFS'
_M='sonetClientCtpPmRxSES'
_L='sonetClientCtpPmRxES'
_K='sonetClientCtpPmRxCV'
_J='sonetClientCtpPmValidity'
_I='not-accessible'
_H='sonetClientCtpPmTimestamp'
_G='sonetClientCtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-SONETCLIENTCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfIntervalCount,=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfIntervalCount')
ifIndex,=mibBuilder.importSymbols(_D,_E)
commonPerfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','commonPerfMon')
FloatArbitraryPrecision,FloatHundredths,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths','InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
sonetClientCtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,11,2))
if mibBuilder.loadTexts:sonetClientCtpPmMIB.setRevisions(('2008-10-20 00:00',))
_SonetClientCtpPmRealTable_Object=MibTable
sonetClientCtpPmRealTable=_SonetClientCtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1))
if mibBuilder.loadTexts:sonetClientCtpPmRealTable.setStatus(_A)
_SonetClientCtpPmRealEntry_Object=MibTableRow
sonetClientCtpPmRealEntry=_SonetClientCtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1))
sonetClientCtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:sonetClientCtpPmRealEntry.setStatus(_A)
_SonetClientCtpPmRealRxCV_Type=Counter64
_SonetClientCtpPmRealRxCV_Object=MibTableColumn
sonetClientCtpPmRealRxCV=_SonetClientCtpPmRealRxCV_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,1),_SonetClientCtpPmRealRxCV_Type())
sonetClientCtpPmRealRxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealRxCV.setStatus(_A)
_SonetClientCtpPmRealRxES_Type=Integer32
_SonetClientCtpPmRealRxES_Object=MibTableColumn
sonetClientCtpPmRealRxES=_SonetClientCtpPmRealRxES_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,2),_SonetClientCtpPmRealRxES_Type())
sonetClientCtpPmRealRxES.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealRxES.setStatus(_A)
_SonetClientCtpPmRealRxSES_Type=Integer32
_SonetClientCtpPmRealRxSES_Object=MibTableColumn
sonetClientCtpPmRealRxSES=_SonetClientCtpPmRealRxSES_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,3),_SonetClientCtpPmRealRxSES_Type())
sonetClientCtpPmRealRxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealRxSES.setStatus(_A)
_SonetClientCtpPmRealRxSEFS_Type=Integer32
_SonetClientCtpPmRealRxSEFS_Object=MibTableColumn
sonetClientCtpPmRealRxSEFS=_SonetClientCtpPmRealRxSEFS_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,4),_SonetClientCtpPmRealRxSEFS_Type())
sonetClientCtpPmRealRxSEFS.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealRxSEFS.setStatus(_A)
_SonetClientCtpPmRealTxCV_Type=Counter64
_SonetClientCtpPmRealTxCV_Object=MibTableColumn
sonetClientCtpPmRealTxCV=_SonetClientCtpPmRealTxCV_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,5),_SonetClientCtpPmRealTxCV_Type())
sonetClientCtpPmRealTxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealTxCV.setStatus(_A)
_SonetClientCtpPmRealTxES_Type=Integer32
_SonetClientCtpPmRealTxES_Object=MibTableColumn
sonetClientCtpPmRealTxES=_SonetClientCtpPmRealTxES_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,6),_SonetClientCtpPmRealTxES_Type())
sonetClientCtpPmRealTxES.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealTxES.setStatus(_A)
_SonetClientCtpPmRealTxSES_Type=Integer32
_SonetClientCtpPmRealTxSES_Object=MibTableColumn
sonetClientCtpPmRealTxSES=_SonetClientCtpPmRealTxSES_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,7),_SonetClientCtpPmRealTxSES_Type())
sonetClientCtpPmRealTxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealTxSES.setStatus(_A)
_SonetClientCtpPmRealTxSEFS_Type=Integer32
_SonetClientCtpPmRealTxSEFS_Object=MibTableColumn
sonetClientCtpPmRealTxSEFS=_SonetClientCtpPmRealTxSEFS_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,8),_SonetClientCtpPmRealTxSEFS_Type())
sonetClientCtpPmRealTxSEFS.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealTxSEFS.setStatus(_A)
_SonetClientCtpPmRealCktId_Type=DisplayString
_SonetClientCtpPmRealCktId_Object=MibTableColumn
sonetClientCtpPmRealCktId=_SonetClientCtpPmRealCktId_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,9),_SonetClientCtpPmRealCktId_Type())
sonetClientCtpPmRealCktId.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealCktId.setStatus(_A)
_SonetClientCtpPmRealTribPRBSSyncErr_Type=Integer32
_SonetClientCtpPmRealTribPRBSSyncErr_Object=MibTableColumn
sonetClientCtpPmRealTribPRBSSyncErr=_SonetClientCtpPmRealTribPRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,10),_SonetClientCtpPmRealTribPRBSSyncErr_Type())
sonetClientCtpPmRealTribPRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealTribPRBSSyncErr.setStatus(_A)
_SonetClientCtpPmRealTribPRBSErr_Type=HCPerfIntervalCount
_SonetClientCtpPmRealTribPRBSErr_Object=MibTableColumn
sonetClientCtpPmRealTribPRBSErr=_SonetClientCtpPmRealTribPRBSErr_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,11),_SonetClientCtpPmRealTribPRBSErr_Type())
sonetClientCtpPmRealTribPRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealTribPRBSErr.setStatus(_A)
_SonetClientCtpPmRealLinePRBSSyncErr_Type=Integer32
_SonetClientCtpPmRealLinePRBSSyncErr_Object=MibTableColumn
sonetClientCtpPmRealLinePRBSSyncErr=_SonetClientCtpPmRealLinePRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,12),_SonetClientCtpPmRealLinePRBSSyncErr_Type())
sonetClientCtpPmRealLinePRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealLinePRBSSyncErr.setStatus(_A)
_SonetClientCtpPmRealLinePRBSErr_Type=HCPerfIntervalCount
_SonetClientCtpPmRealLinePRBSErr_Object=MibTableColumn
sonetClientCtpPmRealLinePRBSErr=_SonetClientCtpPmRealLinePRBSErr_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,13),_SonetClientCtpPmRealLinePRBSErr_Type())
sonetClientCtpPmRealLinePRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealLinePRBSErr.setStatus(_A)
_SonetClientCtpPmRealRxBER_Type=FloatArbitraryPrecision
_SonetClientCtpPmRealRxBER_Object=MibTableColumn
sonetClientCtpPmRealRxBER=_SonetClientCtpPmRealRxBER_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,14),_SonetClientCtpPmRealRxBER_Type())
sonetClientCtpPmRealRxBER.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealRxBER.setStatus(_A)
_SonetClientCtpPmRealTxBER_Type=FloatArbitraryPrecision
_SonetClientCtpPmRealTxBER_Object=MibTableColumn
sonetClientCtpPmRealTxBER=_SonetClientCtpPmRealTxBER_Object((1,3,6,1,4,1,21296,2,2,1,11,2,1,1,15),_SonetClientCtpPmRealTxBER_Type())
sonetClientCtpPmRealTxBER.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRealTxBER.setStatus(_A)
_SonetClientCtpPmTable_Object=MibTable
sonetClientCtpPmTable=_SonetClientCtpPmTable_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2))
if mibBuilder.loadTexts:sonetClientCtpPmTable.setStatus(_A)
_SonetClientCtpPmEntry_Object=MibTableRow
sonetClientCtpPmEntry=_SonetClientCtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1))
sonetClientCtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:sonetClientCtpPmEntry.setStatus(_A)
class _SonetClientCtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SonetClientCtpPmTimestamp_Type.__name__=_F
_SonetClientCtpPmTimestamp_Object=MibTableColumn
sonetClientCtpPmTimestamp=_SonetClientCtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,1),_SonetClientCtpPmTimestamp_Type())
sonetClientCtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:sonetClientCtpPmTimestamp.setStatus(_A)
class _SonetClientCtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_SonetClientCtpPmSampleDuration_Type.__name__=_F
_SonetClientCtpPmSampleDuration_Object=MibTableColumn
sonetClientCtpPmSampleDuration=_SonetClientCtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,2),_SonetClientCtpPmSampleDuration_Type())
sonetClientCtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:sonetClientCtpPmSampleDuration.setStatus(_A)
_SonetClientCtpPmValidity_Type=TruthValue
_SonetClientCtpPmValidity_Object=MibTableColumn
sonetClientCtpPmValidity=_SonetClientCtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,3),_SonetClientCtpPmValidity_Type())
sonetClientCtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmValidity.setStatus(_A)
_SonetClientCtpPmRxCV_Type=HCPerfIntervalCount
_SonetClientCtpPmRxCV_Object=MibTableColumn
sonetClientCtpPmRxCV=_SonetClientCtpPmRxCV_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,4),_SonetClientCtpPmRxCV_Type())
sonetClientCtpPmRxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRxCV.setStatus(_A)
_SonetClientCtpPmRxES_Type=Integer32
_SonetClientCtpPmRxES_Object=MibTableColumn
sonetClientCtpPmRxES=_SonetClientCtpPmRxES_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,5),_SonetClientCtpPmRxES_Type())
sonetClientCtpPmRxES.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRxES.setStatus(_A)
_SonetClientCtpPmRxSES_Type=Integer32
_SonetClientCtpPmRxSES_Object=MibTableColumn
sonetClientCtpPmRxSES=_SonetClientCtpPmRxSES_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,6),_SonetClientCtpPmRxSES_Type())
sonetClientCtpPmRxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRxSES.setStatus(_A)
_SonetClientCtpPmRxSEFS_Type=Integer32
_SonetClientCtpPmRxSEFS_Object=MibTableColumn
sonetClientCtpPmRxSEFS=_SonetClientCtpPmRxSEFS_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,7),_SonetClientCtpPmRxSEFS_Type())
sonetClientCtpPmRxSEFS.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRxSEFS.setStatus(_A)
_SonetClientCtpPmTxCV_Type=HCPerfIntervalCount
_SonetClientCtpPmTxCV_Object=MibTableColumn
sonetClientCtpPmTxCV=_SonetClientCtpPmTxCV_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,8),_SonetClientCtpPmTxCV_Type())
sonetClientCtpPmTxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmTxCV.setStatus(_A)
_SonetClientCtpPmTxES_Type=Integer32
_SonetClientCtpPmTxES_Object=MibTableColumn
sonetClientCtpPmTxES=_SonetClientCtpPmTxES_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,9),_SonetClientCtpPmTxES_Type())
sonetClientCtpPmTxES.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmTxES.setStatus(_A)
_SonetClientCtpPmTxSES_Type=Integer32
_SonetClientCtpPmTxSES_Object=MibTableColumn
sonetClientCtpPmTxSES=_SonetClientCtpPmTxSES_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,10),_SonetClientCtpPmTxSES_Type())
sonetClientCtpPmTxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmTxSES.setStatus(_A)
_SonetClientCtpPmTxSEFS_Type=Integer32
_SonetClientCtpPmTxSEFS_Object=MibTableColumn
sonetClientCtpPmTxSEFS=_SonetClientCtpPmTxSEFS_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,11),_SonetClientCtpPmTxSEFS_Type())
sonetClientCtpPmTxSEFS.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmTxSEFS.setStatus(_A)
_SonetClientCtpPmCktId_Type=DisplayString
_SonetClientCtpPmCktId_Object=MibTableColumn
sonetClientCtpPmCktId=_SonetClientCtpPmCktId_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,12),_SonetClientCtpPmCktId_Type())
sonetClientCtpPmCktId.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmCktId.setStatus(_A)
_SonetClientCtpPmTribPRBSSyncErr_Type=Integer32
_SonetClientCtpPmTribPRBSSyncErr_Object=MibTableColumn
sonetClientCtpPmTribPRBSSyncErr=_SonetClientCtpPmTribPRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,13),_SonetClientCtpPmTribPRBSSyncErr_Type())
sonetClientCtpPmTribPRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmTribPRBSSyncErr.setStatus(_A)
_SonetClientCtpPmTribPRBSErr_Type=HCPerfIntervalCount
_SonetClientCtpPmTribPRBSErr_Object=MibTableColumn
sonetClientCtpPmTribPRBSErr=_SonetClientCtpPmTribPRBSErr_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,14),_SonetClientCtpPmTribPRBSErr_Type())
sonetClientCtpPmTribPRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmTribPRBSErr.setStatus(_A)
_SonetClientCtpPmPayloadType_Type=InfnServiceType
_SonetClientCtpPmPayloadType_Object=MibTableColumn
sonetClientCtpPmPayloadType=_SonetClientCtpPmPayloadType_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,15),_SonetClientCtpPmPayloadType_Type())
sonetClientCtpPmPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmPayloadType.setStatus(_A)
_SonetClientCtpPmLinePRBSSyncErr_Type=Integer32
_SonetClientCtpPmLinePRBSSyncErr_Object=MibTableColumn
sonetClientCtpPmLinePRBSSyncErr=_SonetClientCtpPmLinePRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,16),_SonetClientCtpPmLinePRBSSyncErr_Type())
sonetClientCtpPmLinePRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmLinePRBSSyncErr.setStatus(_A)
_SonetClientCtpPmLinePRBSErr_Type=HCPerfIntervalCount
_SonetClientCtpPmLinePRBSErr_Object=MibTableColumn
sonetClientCtpPmLinePRBSErr=_SonetClientCtpPmLinePRBSErr_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,17),_SonetClientCtpPmLinePRBSErr_Type())
sonetClientCtpPmLinePRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmLinePRBSErr.setStatus(_A)
_SonetClientCtpPmRxBER_Type=FloatArbitraryPrecision
_SonetClientCtpPmRxBER_Object=MibTableColumn
sonetClientCtpPmRxBER=_SonetClientCtpPmRxBER_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,18),_SonetClientCtpPmRxBER_Type())
sonetClientCtpPmRxBER.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmRxBER.setStatus(_A)
_SonetClientCtpPmTxBER_Type=FloatArbitraryPrecision
_SonetClientCtpPmTxBER_Object=MibTableColumn
sonetClientCtpPmTxBER=_SonetClientCtpPmTxBER_Object((1,3,6,1,4,1,21296,2,2,1,11,2,2,1,19),_SonetClientCtpPmTxBER_Type())
sonetClientCtpPmTxBER.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmTxBER.setStatus(_A)
_SonetClientCtpPmConformance_ObjectIdentity=ObjectIdentity
sonetClientCtpPmConformance=_SonetClientCtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,2,3))
_SonetClientCtpPmCompliances_ObjectIdentity=ObjectIdentity
sonetClientCtpPmCompliances=_SonetClientCtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,2,3,1))
_SonetClientCtpPmGroups_ObjectIdentity=ObjectIdentity
sonetClientCtpPmGroups=_SonetClientCtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,2,3,2))
sonetClientCtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,11,2,3,2,1))
sonetClientCtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:sonetClientCtpPmGroup.setStatus(_A)
sonetClientCtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,11,2,3,2,2))
sonetClientCtpPmRealGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:sonetClientCtpPmRealGroup.setStatus(_A)
sonetClientCtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,11,2,3,1,1))
sonetClientCtpPmCompliance.setObjects((_B,_p))
if mibBuilder.loadTexts:sonetClientCtpPmCompliance.setStatus(_A)
sonetClientCtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,11,2,3,1,2))
sonetClientCtpPmRealCompliance.setObjects((_B,_q))
if mibBuilder.loadTexts:sonetClientCtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sonetClientCtpPmMIB':sonetClientCtpPmMIB,'sonetClientCtpPmRealTable':sonetClientCtpPmRealTable,'sonetClientCtpPmRealEntry':sonetClientCtpPmRealEntry,_a:sonetClientCtpPmRealRxCV,_b:sonetClientCtpPmRealRxES,_c:sonetClientCtpPmRealRxSES,_d:sonetClientCtpPmRealRxSEFS,_e:sonetClientCtpPmRealTxCV,_f:sonetClientCtpPmRealTxES,_g:sonetClientCtpPmRealTxSES,_h:sonetClientCtpPmRealTxSEFS,_i:sonetClientCtpPmRealCktId,_j:sonetClientCtpPmRealTribPRBSSyncErr,_k:sonetClientCtpPmRealTribPRBSErr,_l:sonetClientCtpPmRealLinePRBSSyncErr,_m:sonetClientCtpPmRealLinePRBSErr,_n:sonetClientCtpPmRealRxBER,_o:sonetClientCtpPmRealTxBER,'sonetClientCtpPmTable':sonetClientCtpPmTable,'sonetClientCtpPmEntry':sonetClientCtpPmEntry,_H:sonetClientCtpPmTimestamp,_G:sonetClientCtpPmSampleDuration,_J:sonetClientCtpPmValidity,_K:sonetClientCtpPmRxCV,_L:sonetClientCtpPmRxES,_M:sonetClientCtpPmRxSES,_N:sonetClientCtpPmRxSEFS,_O:sonetClientCtpPmTxCV,_P:sonetClientCtpPmTxES,_Q:sonetClientCtpPmTxSES,_R:sonetClientCtpPmTxSEFS,_S:sonetClientCtpPmCktId,_T:sonetClientCtpPmTribPRBSSyncErr,_U:sonetClientCtpPmTribPRBSErr,_V:sonetClientCtpPmPayloadType,_W:sonetClientCtpPmLinePRBSSyncErr,_X:sonetClientCtpPmLinePRBSErr,_Y:sonetClientCtpPmRxBER,_Z:sonetClientCtpPmTxBER,'sonetClientCtpPmConformance':sonetClientCtpPmConformance,'sonetClientCtpPmCompliances':sonetClientCtpPmCompliances,'sonetClientCtpPmCompliance':sonetClientCtpPmCompliance,'sonetClientCtpPmRealCompliance':sonetClientCtpPmRealCompliance,'sonetClientCtpPmGroups':sonetClientCtpPmGroups,_p:sonetClientCtpPmGroup,_q:sonetClientCtpPmRealGroup})