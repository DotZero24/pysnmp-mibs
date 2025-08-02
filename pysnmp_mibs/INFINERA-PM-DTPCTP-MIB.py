_e='dtpCtpPmRealGroup'
_d='dtpCtpPmGroup'
_c='dtpCtpPmRealInternalCV'
_b='dtpCtpPmRealPrbsErr'
_a='dtpCtpPmRealPrbsSyncErr'
_Z='dtpCtpPmRealDtpTxUAS'
_Y='dtpCtpPmRealDtpTxSES'
_X='dtpCtpPmRealDtpTxES'
_W='dtpCtpPmRealDtpTxCV'
_V='dtpCtpPmRealDtpRxUAS'
_U='dtpCtpPmRealDtpRxSES'
_T='dtpCtpPmRealDtpRxES'
_S='dtpCtpPmRealDtpRxCV'
_R='dtpCtpPmDtpTxUAS'
_Q='dtpCtpPmDtpTxSES'
_P='dtpCtpPmDtpTxES'
_O='dtpCtpPmDtpTxCV'
_N='dtpCtpPmDtpRxUAS'
_M='dtpCtpPmDtpRxSES'
_L='dtpCtpPmDtpRxES'
_K='dtpCtpPmDtpRxCV'
_J='dtpCtpPmValidity'
_I='not-accessible'
_H='dtpCtpPmTimestamp'
_G='dtpCtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-DTPCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfIntervalCount,=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfIntervalCount')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
dtpCtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,6))
if mibBuilder.loadTexts:dtpCtpPmMIB.setRevisions(('2008-10-20 00:00',))
_DtpCtpPmRealTable_Object=MibTable
dtpCtpPmRealTable=_DtpCtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1))
if mibBuilder.loadTexts:dtpCtpPmRealTable.setStatus(_A)
_DtpCtpPmRealEntry_Object=MibTableRow
dtpCtpPmRealEntry=_DtpCtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1))
dtpCtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dtpCtpPmRealEntry.setStatus(_A)
_DtpCtpPmRealDtpRxCV_Type=Counter64
_DtpCtpPmRealDtpRxCV_Object=MibTableColumn
dtpCtpPmRealDtpRxCV=_DtpCtpPmRealDtpRxCV_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1,1),_DtpCtpPmRealDtpRxCV_Type())
dtpCtpPmRealDtpRxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmRealDtpRxCV.setStatus(_A)
_DtpCtpPmRealDtpRxES_Type=Integer32
_DtpCtpPmRealDtpRxES_Object=MibTableColumn
dtpCtpPmRealDtpRxES=_DtpCtpPmRealDtpRxES_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1,2),_DtpCtpPmRealDtpRxES_Type())
dtpCtpPmRealDtpRxES.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmRealDtpRxES.setStatus(_A)
_DtpCtpPmRealDtpRxSES_Type=Integer32
_DtpCtpPmRealDtpRxSES_Object=MibTableColumn
dtpCtpPmRealDtpRxSES=_DtpCtpPmRealDtpRxSES_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1,3),_DtpCtpPmRealDtpRxSES_Type())
dtpCtpPmRealDtpRxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmRealDtpRxSES.setStatus(_A)
_DtpCtpPmRealDtpRxUAS_Type=Integer32
_DtpCtpPmRealDtpRxUAS_Object=MibTableColumn
dtpCtpPmRealDtpRxUAS=_DtpCtpPmRealDtpRxUAS_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1,4),_DtpCtpPmRealDtpRxUAS_Type())
dtpCtpPmRealDtpRxUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmRealDtpRxUAS.setStatus(_A)
_DtpCtpPmRealDtpTxCV_Type=Counter64
_DtpCtpPmRealDtpTxCV_Object=MibTableColumn
dtpCtpPmRealDtpTxCV=_DtpCtpPmRealDtpTxCV_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1,5),_DtpCtpPmRealDtpTxCV_Type())
dtpCtpPmRealDtpTxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmRealDtpTxCV.setStatus(_A)
_DtpCtpPmRealDtpTxES_Type=Integer32
_DtpCtpPmRealDtpTxES_Object=MibTableColumn
dtpCtpPmRealDtpTxES=_DtpCtpPmRealDtpTxES_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1,6),_DtpCtpPmRealDtpTxES_Type())
dtpCtpPmRealDtpTxES.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmRealDtpTxES.setStatus(_A)
_DtpCtpPmRealDtpTxSES_Type=Integer32
_DtpCtpPmRealDtpTxSES_Object=MibTableColumn
dtpCtpPmRealDtpTxSES=_DtpCtpPmRealDtpTxSES_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1,7),_DtpCtpPmRealDtpTxSES_Type())
dtpCtpPmRealDtpTxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmRealDtpTxSES.setStatus(_A)
_DtpCtpPmRealDtpTxUAS_Type=Integer32
_DtpCtpPmRealDtpTxUAS_Object=MibTableColumn
dtpCtpPmRealDtpTxUAS=_DtpCtpPmRealDtpTxUAS_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1,8),_DtpCtpPmRealDtpTxUAS_Type())
dtpCtpPmRealDtpTxUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmRealDtpTxUAS.setStatus(_A)
_DtpCtpPmRealPrbsSyncErr_Type=Integer32
_DtpCtpPmRealPrbsSyncErr_Object=MibTableColumn
dtpCtpPmRealPrbsSyncErr=_DtpCtpPmRealPrbsSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1,9),_DtpCtpPmRealPrbsSyncErr_Type())
dtpCtpPmRealPrbsSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmRealPrbsSyncErr.setStatus(_A)
_DtpCtpPmRealPrbsErr_Type=Integer32
_DtpCtpPmRealPrbsErr_Object=MibTableColumn
dtpCtpPmRealPrbsErr=_DtpCtpPmRealPrbsErr_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1,10),_DtpCtpPmRealPrbsErr_Type())
dtpCtpPmRealPrbsErr.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmRealPrbsErr.setStatus(_A)
_DtpCtpPmRealInternalCV_Type=Counter64
_DtpCtpPmRealInternalCV_Object=MibTableColumn
dtpCtpPmRealInternalCV=_DtpCtpPmRealInternalCV_Object((1,3,6,1,4,1,21296,2,2,2,3,6,1,1,11),_DtpCtpPmRealInternalCV_Type())
dtpCtpPmRealInternalCV.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmRealInternalCV.setStatus(_A)
_DtpCtpPmTable_Object=MibTable
dtpCtpPmTable=_DtpCtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2))
if mibBuilder.loadTexts:dtpCtpPmTable.setStatus(_A)
_DtpCtpPmEntry_Object=MibTableRow
dtpCtpPmEntry=_DtpCtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1))
dtpCtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:dtpCtpPmEntry.setStatus(_A)
class _DtpCtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DtpCtpPmTimestamp_Type.__name__=_F
_DtpCtpPmTimestamp_Object=MibTableColumn
dtpCtpPmTimestamp=_DtpCtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1,1),_DtpCtpPmTimestamp_Type())
dtpCtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:dtpCtpPmTimestamp.setStatus(_A)
class _DtpCtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_DtpCtpPmSampleDuration_Type.__name__=_F
_DtpCtpPmSampleDuration_Object=MibTableColumn
dtpCtpPmSampleDuration=_DtpCtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1,2),_DtpCtpPmSampleDuration_Type())
dtpCtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:dtpCtpPmSampleDuration.setStatus(_A)
_DtpCtpPmValidity_Type=TruthValue
_DtpCtpPmValidity_Object=MibTableColumn
dtpCtpPmValidity=_DtpCtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1,3),_DtpCtpPmValidity_Type())
dtpCtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmValidity.setStatus(_A)
_DtpCtpPmDtpRxCV_Type=HCPerfIntervalCount
_DtpCtpPmDtpRxCV_Object=MibTableColumn
dtpCtpPmDtpRxCV=_DtpCtpPmDtpRxCV_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1,4),_DtpCtpPmDtpRxCV_Type())
dtpCtpPmDtpRxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmDtpRxCV.setStatus(_A)
_DtpCtpPmDtpRxES_Type=Integer32
_DtpCtpPmDtpRxES_Object=MibTableColumn
dtpCtpPmDtpRxES=_DtpCtpPmDtpRxES_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1,5),_DtpCtpPmDtpRxES_Type())
dtpCtpPmDtpRxES.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmDtpRxES.setStatus(_A)
_DtpCtpPmDtpRxSES_Type=Integer32
_DtpCtpPmDtpRxSES_Object=MibTableColumn
dtpCtpPmDtpRxSES=_DtpCtpPmDtpRxSES_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1,6),_DtpCtpPmDtpRxSES_Type())
dtpCtpPmDtpRxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmDtpRxSES.setStatus(_A)
_DtpCtpPmDtpRxUAS_Type=Integer32
_DtpCtpPmDtpRxUAS_Object=MibTableColumn
dtpCtpPmDtpRxUAS=_DtpCtpPmDtpRxUAS_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1,7),_DtpCtpPmDtpRxUAS_Type())
dtpCtpPmDtpRxUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmDtpRxUAS.setStatus(_A)
_DtpCtpPmDtpTxCV_Type=HCPerfIntervalCount
_DtpCtpPmDtpTxCV_Object=MibTableColumn
dtpCtpPmDtpTxCV=_DtpCtpPmDtpTxCV_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1,8),_DtpCtpPmDtpTxCV_Type())
dtpCtpPmDtpTxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmDtpTxCV.setStatus(_A)
_DtpCtpPmDtpTxES_Type=Integer32
_DtpCtpPmDtpTxES_Object=MibTableColumn
dtpCtpPmDtpTxES=_DtpCtpPmDtpTxES_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1,9),_DtpCtpPmDtpTxES_Type())
dtpCtpPmDtpTxES.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmDtpTxES.setStatus(_A)
_DtpCtpPmDtpTxSES_Type=Integer32
_DtpCtpPmDtpTxSES_Object=MibTableColumn
dtpCtpPmDtpTxSES=_DtpCtpPmDtpTxSES_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1,10),_DtpCtpPmDtpTxSES_Type())
dtpCtpPmDtpTxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmDtpTxSES.setStatus(_A)
_DtpCtpPmDtpTxUAS_Type=Integer32
_DtpCtpPmDtpTxUAS_Object=MibTableColumn
dtpCtpPmDtpTxUAS=_DtpCtpPmDtpTxUAS_Object((1,3,6,1,4,1,21296,2,2,2,3,6,2,1,11),_DtpCtpPmDtpTxUAS_Type())
dtpCtpPmDtpTxUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmDtpTxUAS.setStatus(_A)
_DtpCtpPmConformance_ObjectIdentity=ObjectIdentity
dtpCtpPmConformance=_DtpCtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,6,3))
_DtpCtpPmCompliances_ObjectIdentity=ObjectIdentity
dtpCtpPmCompliances=_DtpCtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,6,3,1))
_DtpCtpPmGroups_ObjectIdentity=ObjectIdentity
dtpCtpPmGroups=_DtpCtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,6,3,2))
dtpCtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,6,3,2,1))
dtpCtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:dtpCtpPmGroup.setStatus(_A)
dtpCtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,6,3,2,2))
dtpCtpPmRealGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:dtpCtpPmRealGroup.setStatus(_A)
dtpCtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,6,3,1,1))
dtpCtpPmCompliance.setObjects((_B,_d))
if mibBuilder.loadTexts:dtpCtpPmCompliance.setStatus(_A)
dtpCtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,6,3,1,2))
dtpCtpPmRealCompliance.setObjects((_B,_e))
if mibBuilder.loadTexts:dtpCtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dtpCtpPmMIB':dtpCtpPmMIB,'dtpCtpPmRealTable':dtpCtpPmRealTable,'dtpCtpPmRealEntry':dtpCtpPmRealEntry,_S:dtpCtpPmRealDtpRxCV,_T:dtpCtpPmRealDtpRxES,_U:dtpCtpPmRealDtpRxSES,_V:dtpCtpPmRealDtpRxUAS,_W:dtpCtpPmRealDtpTxCV,_X:dtpCtpPmRealDtpTxES,_Y:dtpCtpPmRealDtpTxSES,_Z:dtpCtpPmRealDtpTxUAS,_a:dtpCtpPmRealPrbsSyncErr,_b:dtpCtpPmRealPrbsErr,_c:dtpCtpPmRealInternalCV,'dtpCtpPmTable':dtpCtpPmTable,'dtpCtpPmEntry':dtpCtpPmEntry,_H:dtpCtpPmTimestamp,_G:dtpCtpPmSampleDuration,_J:dtpCtpPmValidity,_K:dtpCtpPmDtpRxCV,_L:dtpCtpPmDtpRxES,_M:dtpCtpPmDtpRxSES,_N:dtpCtpPmDtpRxUAS,_O:dtpCtpPmDtpTxCV,_P:dtpCtpPmDtpTxES,_Q:dtpCtpPmDtpTxSES,_R:dtpCtpPmDtpTxUAS,'dtpCtpPmConformance':dtpCtpPmConformance,'dtpCtpPmCompliances':dtpCtpPmCompliances,'dtpCtpPmCompliance':dtpCtpPmCompliance,'dtpCtpPmRealCompliance':dtpCtpPmRealCompliance,'dtpCtpPmGroups':dtpCtpPmGroups,_d:dtpCtpPmGroup,_e:dtpCtpPmRealGroup})