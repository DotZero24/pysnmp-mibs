_b='groupTpPmRealGroup'
_a='groupTpPmGroup'
_Z='groupTpPmRealDtpTxUAS'
_Y='groupTpPmRealDtpTxSES'
_X='groupTpPmRealDtpTxES'
_W='groupTpPmRealDtpTxCV'
_V='groupTpPmRealDtpRxUAS'
_U='groupTpPmRealDtpRxSES'
_T='groupTpPmRealDtpRxES'
_S='groupTpPmRealDtpRxCV'
_R='groupTpPmDtpTxUAS'
_Q='groupTpPmDtpTxSES'
_P='groupTpPmDtpTxES'
_O='groupTpPmDtpTxCV'
_N='groupTpPmDtpRxUAS'
_M='groupTpPmDtpRxSES'
_L='groupTpPmDtpRxES'
_K='groupTpPmDtpRxCV'
_J='groupTpPmValidity'
_I='not-accessible'
_H='groupTpPmTimestamp'
_G='groupTpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-GROUPTP-MIB'
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
groupTpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,9))
if mibBuilder.loadTexts:groupTpPmMIB.setRevisions(('2008-10-20 00:00',))
_GroupTpPmRealTable_Object=MibTable
groupTpPmRealTable=_GroupTpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,9,1))
if mibBuilder.loadTexts:groupTpPmRealTable.setStatus(_A)
_GroupTpPmRealEntry_Object=MibTableRow
groupTpPmRealEntry=_GroupTpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,9,1,1))
groupTpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:groupTpPmRealEntry.setStatus(_A)
_GroupTpPmRealDtpRxCV_Type=Counter64
_GroupTpPmRealDtpRxCV_Object=MibTableColumn
groupTpPmRealDtpRxCV=_GroupTpPmRealDtpRxCV_Object((1,3,6,1,4,1,21296,2,2,2,3,9,1,1,1),_GroupTpPmRealDtpRxCV_Type())
groupTpPmRealDtpRxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmRealDtpRxCV.setStatus(_A)
_GroupTpPmRealDtpRxES_Type=Integer32
_GroupTpPmRealDtpRxES_Object=MibTableColumn
groupTpPmRealDtpRxES=_GroupTpPmRealDtpRxES_Object((1,3,6,1,4,1,21296,2,2,2,3,9,1,1,2),_GroupTpPmRealDtpRxES_Type())
groupTpPmRealDtpRxES.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmRealDtpRxES.setStatus(_A)
_GroupTpPmRealDtpRxSES_Type=Integer32
_GroupTpPmRealDtpRxSES_Object=MibTableColumn
groupTpPmRealDtpRxSES=_GroupTpPmRealDtpRxSES_Object((1,3,6,1,4,1,21296,2,2,2,3,9,1,1,3),_GroupTpPmRealDtpRxSES_Type())
groupTpPmRealDtpRxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmRealDtpRxSES.setStatus(_A)
_GroupTpPmRealDtpRxUAS_Type=Integer32
_GroupTpPmRealDtpRxUAS_Object=MibTableColumn
groupTpPmRealDtpRxUAS=_GroupTpPmRealDtpRxUAS_Object((1,3,6,1,4,1,21296,2,2,2,3,9,1,1,4),_GroupTpPmRealDtpRxUAS_Type())
groupTpPmRealDtpRxUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmRealDtpRxUAS.setStatus(_A)
_GroupTpPmRealDtpTxCV_Type=Counter64
_GroupTpPmRealDtpTxCV_Object=MibTableColumn
groupTpPmRealDtpTxCV=_GroupTpPmRealDtpTxCV_Object((1,3,6,1,4,1,21296,2,2,2,3,9,1,1,5),_GroupTpPmRealDtpTxCV_Type())
groupTpPmRealDtpTxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmRealDtpTxCV.setStatus(_A)
_GroupTpPmRealDtpTxES_Type=Integer32
_GroupTpPmRealDtpTxES_Object=MibTableColumn
groupTpPmRealDtpTxES=_GroupTpPmRealDtpTxES_Object((1,3,6,1,4,1,21296,2,2,2,3,9,1,1,6),_GroupTpPmRealDtpTxES_Type())
groupTpPmRealDtpTxES.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmRealDtpTxES.setStatus(_A)
_GroupTpPmRealDtpTxSES_Type=Integer32
_GroupTpPmRealDtpTxSES_Object=MibTableColumn
groupTpPmRealDtpTxSES=_GroupTpPmRealDtpTxSES_Object((1,3,6,1,4,1,21296,2,2,2,3,9,1,1,7),_GroupTpPmRealDtpTxSES_Type())
groupTpPmRealDtpTxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmRealDtpTxSES.setStatus(_A)
_GroupTpPmRealDtpTxUAS_Type=Integer32
_GroupTpPmRealDtpTxUAS_Object=MibTableColumn
groupTpPmRealDtpTxUAS=_GroupTpPmRealDtpTxUAS_Object((1,3,6,1,4,1,21296,2,2,2,3,9,1,1,8),_GroupTpPmRealDtpTxUAS_Type())
groupTpPmRealDtpTxUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmRealDtpTxUAS.setStatus(_A)
_GroupTpPmTable_Object=MibTable
groupTpPmTable=_GroupTpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2))
if mibBuilder.loadTexts:groupTpPmTable.setStatus(_A)
_GroupTpPmEntry_Object=MibTableRow
groupTpPmEntry=_GroupTpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1))
groupTpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:groupTpPmEntry.setStatus(_A)
class _GroupTpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_GroupTpPmTimestamp_Type.__name__=_F
_GroupTpPmTimestamp_Object=MibTableColumn
groupTpPmTimestamp=_GroupTpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1,1),_GroupTpPmTimestamp_Type())
groupTpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:groupTpPmTimestamp.setStatus(_A)
class _GroupTpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_GroupTpPmSampleDuration_Type.__name__=_F
_GroupTpPmSampleDuration_Object=MibTableColumn
groupTpPmSampleDuration=_GroupTpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1,2),_GroupTpPmSampleDuration_Type())
groupTpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:groupTpPmSampleDuration.setStatus(_A)
_GroupTpPmValidity_Type=TruthValue
_GroupTpPmValidity_Object=MibTableColumn
groupTpPmValidity=_GroupTpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1,3),_GroupTpPmValidity_Type())
groupTpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmValidity.setStatus(_A)
_GroupTpPmDtpRxCV_Type=HCPerfIntervalCount
_GroupTpPmDtpRxCV_Object=MibTableColumn
groupTpPmDtpRxCV=_GroupTpPmDtpRxCV_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1,4),_GroupTpPmDtpRxCV_Type())
groupTpPmDtpRxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmDtpRxCV.setStatus(_A)
_GroupTpPmDtpRxES_Type=Integer32
_GroupTpPmDtpRxES_Object=MibTableColumn
groupTpPmDtpRxES=_GroupTpPmDtpRxES_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1,5),_GroupTpPmDtpRxES_Type())
groupTpPmDtpRxES.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmDtpRxES.setStatus(_A)
_GroupTpPmDtpRxSES_Type=Integer32
_GroupTpPmDtpRxSES_Object=MibTableColumn
groupTpPmDtpRxSES=_GroupTpPmDtpRxSES_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1,6),_GroupTpPmDtpRxSES_Type())
groupTpPmDtpRxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmDtpRxSES.setStatus(_A)
_GroupTpPmDtpRxUAS_Type=Integer32
_GroupTpPmDtpRxUAS_Object=MibTableColumn
groupTpPmDtpRxUAS=_GroupTpPmDtpRxUAS_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1,7),_GroupTpPmDtpRxUAS_Type())
groupTpPmDtpRxUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmDtpRxUAS.setStatus(_A)
_GroupTpPmDtpTxCV_Type=HCPerfIntervalCount
_GroupTpPmDtpTxCV_Object=MibTableColumn
groupTpPmDtpTxCV=_GroupTpPmDtpTxCV_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1,8),_GroupTpPmDtpTxCV_Type())
groupTpPmDtpTxCV.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmDtpTxCV.setStatus(_A)
_GroupTpPmDtpTxES_Type=Integer32
_GroupTpPmDtpTxES_Object=MibTableColumn
groupTpPmDtpTxES=_GroupTpPmDtpTxES_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1,9),_GroupTpPmDtpTxES_Type())
groupTpPmDtpTxES.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmDtpTxES.setStatus(_A)
_GroupTpPmDtpTxSES_Type=Integer32
_GroupTpPmDtpTxSES_Object=MibTableColumn
groupTpPmDtpTxSES=_GroupTpPmDtpTxSES_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1,10),_GroupTpPmDtpTxSES_Type())
groupTpPmDtpTxSES.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmDtpTxSES.setStatus(_A)
_GroupTpPmDtpTxUAS_Type=Integer32
_GroupTpPmDtpTxUAS_Object=MibTableColumn
groupTpPmDtpTxUAS=_GroupTpPmDtpTxUAS_Object((1,3,6,1,4,1,21296,2,2,2,3,9,2,1,11),_GroupTpPmDtpTxUAS_Type())
groupTpPmDtpTxUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:groupTpPmDtpTxUAS.setStatus(_A)
_GroupTpPmConformance_ObjectIdentity=ObjectIdentity
groupTpPmConformance=_GroupTpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,9,3))
_GroupTpPmCompliances_ObjectIdentity=ObjectIdentity
groupTpPmCompliances=_GroupTpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,9,3,1))
_GroupTpPmGroups_ObjectIdentity=ObjectIdentity
groupTpPmGroups=_GroupTpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,9,3,2))
groupTpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,9,3,2,1))
groupTpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:groupTpPmGroup.setStatus(_A)
groupTpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,9,3,2,2))
groupTpPmRealGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:groupTpPmRealGroup.setStatus(_A)
groupTpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,9,3,1,1))
groupTpPmCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:groupTpPmCompliance.setStatus(_A)
groupTpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,9,3,1,2))
groupTpPmRealCompliance.setObjects((_B,_b))
if mibBuilder.loadTexts:groupTpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'groupTpPmMIB':groupTpPmMIB,'groupTpPmRealTable':groupTpPmRealTable,'groupTpPmRealEntry':groupTpPmRealEntry,_S:groupTpPmRealDtpRxCV,_T:groupTpPmRealDtpRxES,_U:groupTpPmRealDtpRxSES,_V:groupTpPmRealDtpRxUAS,_W:groupTpPmRealDtpTxCV,_X:groupTpPmRealDtpTxES,_Y:groupTpPmRealDtpTxSES,_Z:groupTpPmRealDtpTxUAS,'groupTpPmTable':groupTpPmTable,'groupTpPmEntry':groupTpPmEntry,_H:groupTpPmTimestamp,_G:groupTpPmSampleDuration,_J:groupTpPmValidity,_K:groupTpPmDtpRxCV,_L:groupTpPmDtpRxES,_M:groupTpPmDtpRxSES,_N:groupTpPmDtpRxUAS,_O:groupTpPmDtpTxCV,_P:groupTpPmDtpTxES,_Q:groupTpPmDtpTxSES,_R:groupTpPmDtpTxUAS,'groupTpPmConformance':groupTpPmConformance,'groupTpPmCompliances':groupTpPmCompliances,'groupTpPmCompliance':groupTpPmCompliance,'groupTpPmRealCompliance':groupTpPmRealCompliance,'groupTpPmGroups':groupTpPmGroups,_a:groupTpPmGroup,_b:groupTpPmRealGroup})