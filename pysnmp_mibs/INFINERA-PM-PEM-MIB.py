_W='pemPmRealInPRaw'
_V='pemPmRealInCRaw'
_U='pemPmRealInVRaw'
_T='pemPmInPAvg'
_S='pemPmInPMax'
_R='pemPmInPMin'
_Q='pemPmInCAvg'
_P='pemPmInCMax'
_O='pemPmInCMin'
_N='pemPmInVAvg'
_M='pemPmInVMax'
_L='pemPmInVMin'
_K='pemPmValidity'
_J='not-accessible'
_I='pemPmTimestamp'
_H='pemPmSampleDuration'
_G='pemPmRealGroup'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-PEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
commonPerfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','commonPerfMon')
FloatThousandths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatThousandths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
pemPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,11,5))
if mibBuilder.loadTexts:pemPmMIB.setRevisions(('2015-02-06 00:00',))
_PemPmRealTable_Object=MibTable
pemPmRealTable=_PemPmRealTable_Object((1,3,6,1,4,1,21296,2,2,1,11,5,1))
if mibBuilder.loadTexts:pemPmRealTable.setStatus(_A)
_PemPmRealEntry_Object=MibTableRow
pemPmRealEntry=_PemPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,1,11,5,1,1))
pemPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pemPmRealEntry.setStatus(_A)
_PemPmRealInVRaw_Type=FloatThousandths
_PemPmRealInVRaw_Object=MibTableColumn
pemPmRealInVRaw=_PemPmRealInVRaw_Object((1,3,6,1,4,1,21296,2,2,1,11,5,1,1,1),_PemPmRealInVRaw_Type())
pemPmRealInVRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmRealInVRaw.setStatus(_A)
_PemPmRealInCRaw_Type=FloatThousandths
_PemPmRealInCRaw_Object=MibTableColumn
pemPmRealInCRaw=_PemPmRealInCRaw_Object((1,3,6,1,4,1,21296,2,2,1,11,5,1,1,2),_PemPmRealInCRaw_Type())
pemPmRealInCRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmRealInCRaw.setStatus(_A)
_PemPmRealInPRaw_Type=FloatThousandths
_PemPmRealInPRaw_Object=MibTableColumn
pemPmRealInPRaw=_PemPmRealInPRaw_Object((1,3,6,1,4,1,21296,2,2,1,11,5,1,1,3),_PemPmRealInPRaw_Type())
pemPmRealInPRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmRealInPRaw.setStatus(_A)
_PemPmTable_Object=MibTable
pemPmTable=_PemPmTable_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2))
if mibBuilder.loadTexts:pemPmTable.setStatus(_A)
_PemPmEntry_Object=MibTableRow
pemPmEntry=_PemPmEntry_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1))
pemPmEntry.setIndexNames((0,_D,_E),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:pemPmEntry.setStatus(_A)
class _PemPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PemPmTimestamp_Type.__name__=_F
_PemPmTimestamp_Object=MibTableColumn
pemPmTimestamp=_PemPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,1),_PemPmTimestamp_Type())
pemPmTimestamp.setMaxAccess(_J)
if mibBuilder.loadTexts:pemPmTimestamp.setStatus(_A)
class _PemPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_PemPmSampleDuration_Type.__name__=_F
_PemPmSampleDuration_Object=MibTableColumn
pemPmSampleDuration=_PemPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,2),_PemPmSampleDuration_Type())
pemPmSampleDuration.setMaxAccess(_J)
if mibBuilder.loadTexts:pemPmSampleDuration.setStatus(_A)
_PemPmValidity_Type=TruthValue
_PemPmValidity_Object=MibTableColumn
pemPmValidity=_PemPmValidity_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,3),_PemPmValidity_Type())
pemPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmValidity.setStatus(_A)
_PemPmInVMin_Type=FloatThousandths
_PemPmInVMin_Object=MibTableColumn
pemPmInVMin=_PemPmInVMin_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,4),_PemPmInVMin_Type())
pemPmInVMin.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmInVMin.setStatus(_A)
_PemPmInVMax_Type=FloatThousandths
_PemPmInVMax_Object=MibTableColumn
pemPmInVMax=_PemPmInVMax_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,5),_PemPmInVMax_Type())
pemPmInVMax.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmInVMax.setStatus(_A)
_PemPmInVAvg_Type=FloatThousandths
_PemPmInVAvg_Object=MibTableColumn
pemPmInVAvg=_PemPmInVAvg_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,6),_PemPmInVAvg_Type())
pemPmInVAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmInVAvg.setStatus(_A)
_PemPmInCMin_Type=FloatThousandths
_PemPmInCMin_Object=MibTableColumn
pemPmInCMin=_PemPmInCMin_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,7),_PemPmInCMin_Type())
pemPmInCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmInCMin.setStatus(_A)
_PemPmInCMax_Type=FloatThousandths
_PemPmInCMax_Object=MibTableColumn
pemPmInCMax=_PemPmInCMax_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,8),_PemPmInCMax_Type())
pemPmInCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmInCMax.setStatus(_A)
_PemPmInCAvg_Type=FloatThousandths
_PemPmInCAvg_Object=MibTableColumn
pemPmInCAvg=_PemPmInCAvg_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,9),_PemPmInCAvg_Type())
pemPmInCAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmInCAvg.setStatus(_A)
_PemPmInPMin_Type=FloatThousandths
_PemPmInPMin_Object=MibTableColumn
pemPmInPMin=_PemPmInPMin_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,10),_PemPmInPMin_Type())
pemPmInPMin.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmInPMin.setStatus(_A)
_PemPmInPMax_Type=FloatThousandths
_PemPmInPMax_Object=MibTableColumn
pemPmInPMax=_PemPmInPMax_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,11),_PemPmInPMax_Type())
pemPmInPMax.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmInPMax.setStatus(_A)
_PemPmInPAvg_Type=FloatThousandths
_PemPmInPAvg_Object=MibTableColumn
pemPmInPAvg=_PemPmInPAvg_Object((1,3,6,1,4,1,21296,2,2,1,11,5,2,1,12),_PemPmInPAvg_Type())
pemPmInPAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:pemPmInPAvg.setStatus(_A)
_PemPmConformance_ObjectIdentity=ObjectIdentity
pemPmConformance=_PemPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,5,3))
_PemPmCompliances_ObjectIdentity=ObjectIdentity
pemPmCompliances=_PemPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,5,3,1))
_PemPmGroups_ObjectIdentity=ObjectIdentity
pemPmGroups=_PemPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,5,3,2))
pemPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,11,5,3,2,1))
pemPmGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:pemPmGroup.setStatus(_A)
pemPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,11,5,3,2,2))
pemPmRealGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:pemPmRealGroup.setStatus(_A)
pemPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,11,5,3,1,1))
pemPmCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:pemPmCompliance.setStatus(_A)
pemPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,11,5,3,1,2))
pemPmRealCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:pemPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pemPmMIB':pemPmMIB,'pemPmRealTable':pemPmRealTable,'pemPmRealEntry':pemPmRealEntry,_U:pemPmRealInVRaw,_V:pemPmRealInCRaw,_W:pemPmRealInPRaw,'pemPmTable':pemPmTable,'pemPmEntry':pemPmEntry,_I:pemPmTimestamp,_H:pemPmSampleDuration,_K:pemPmValidity,_L:pemPmInVMin,_M:pemPmInVMax,_N:pemPmInVAvg,_O:pemPmInCMin,_P:pemPmInCMax,_Q:pemPmInCAvg,_R:pemPmInPMin,_S:pemPmInPMax,_T:pemPmInPAvg,'pemPmConformance':pemPmConformance,'pemPmCompliances':pemPmCompliances,'pemPmCompliance':pemPmCompliance,'pemPmRealCompliance':pemPmRealCompliance,'pemPmGroups':pemPmGroups,'pemPmGroup':pemPmGroup,_G:pemPmRealGroup})