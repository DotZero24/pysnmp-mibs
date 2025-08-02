_O='fanPmRealInRpmRaw'
_N='fanPmInRpmAvg'
_M='fanPmInRpmMax'
_L='fanPmInRpmMin'
_K='fanPmValidity'
_J='not-accessible'
_I='fanPmTimestamp'
_H='fanPmSampleDuration'
_G='fanPmRealGroup'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-FAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
commonPerfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','commonPerfMon')
FloatTenths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fanPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,11,4))
if mibBuilder.loadTexts:fanPmMIB.setRevisions(('2015-02-06 00:00',))
_FanPmRealTable_Object=MibTable
fanPmRealTable=_FanPmRealTable_Object((1,3,6,1,4,1,21296,2,2,1,11,4,1))
if mibBuilder.loadTexts:fanPmRealTable.setStatus(_A)
_FanPmRealEntry_Object=MibTableRow
fanPmRealEntry=_FanPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,1,11,4,1,1))
fanPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fanPmRealEntry.setStatus(_A)
_FanPmRealInRpmRaw_Type=FloatTenths
_FanPmRealInRpmRaw_Object=MibTableColumn
fanPmRealInRpmRaw=_FanPmRealInRpmRaw_Object((1,3,6,1,4,1,21296,2,2,1,11,4,1,1,1),_FanPmRealInRpmRaw_Type())
fanPmRealInRpmRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:fanPmRealInRpmRaw.setStatus(_A)
_FanPmTable_Object=MibTable
fanPmTable=_FanPmTable_Object((1,3,6,1,4,1,21296,2,2,1,11,4,2))
if mibBuilder.loadTexts:fanPmTable.setStatus(_A)
_FanPmEntry_Object=MibTableRow
fanPmEntry=_FanPmEntry_Object((1,3,6,1,4,1,21296,2,2,1,11,4,2,1))
fanPmEntry.setIndexNames((0,_D,_E),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:fanPmEntry.setStatus(_A)
class _FanPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FanPmTimestamp_Type.__name__=_F
_FanPmTimestamp_Object=MibTableColumn
fanPmTimestamp=_FanPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,1,11,4,2,1,1),_FanPmTimestamp_Type())
fanPmTimestamp.setMaxAccess(_J)
if mibBuilder.loadTexts:fanPmTimestamp.setStatus(_A)
class _FanPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_FanPmSampleDuration_Type.__name__=_F
_FanPmSampleDuration_Object=MibTableColumn
fanPmSampleDuration=_FanPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,1,11,4,2,1,2),_FanPmSampleDuration_Type())
fanPmSampleDuration.setMaxAccess(_J)
if mibBuilder.loadTexts:fanPmSampleDuration.setStatus(_A)
_FanPmValidity_Type=TruthValue
_FanPmValidity_Object=MibTableColumn
fanPmValidity=_FanPmValidity_Object((1,3,6,1,4,1,21296,2,2,1,11,4,2,1,3),_FanPmValidity_Type())
fanPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:fanPmValidity.setStatus(_A)
_FanPmInRpmMin_Type=FloatTenths
_FanPmInRpmMin_Object=MibTableColumn
fanPmInRpmMin=_FanPmInRpmMin_Object((1,3,6,1,4,1,21296,2,2,1,11,4,2,1,4),_FanPmInRpmMin_Type())
fanPmInRpmMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fanPmInRpmMin.setStatus(_A)
_FanPmInRpmMax_Type=FloatTenths
_FanPmInRpmMax_Object=MibTableColumn
fanPmInRpmMax=_FanPmInRpmMax_Object((1,3,6,1,4,1,21296,2,2,1,11,4,2,1,5),_FanPmInRpmMax_Type())
fanPmInRpmMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fanPmInRpmMax.setStatus(_A)
_FanPmInRpmAvg_Type=FloatTenths
_FanPmInRpmAvg_Object=MibTableColumn
fanPmInRpmAvg=_FanPmInRpmAvg_Object((1,3,6,1,4,1,21296,2,2,1,11,4,2,1,6),_FanPmInRpmAvg_Type())
fanPmInRpmAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:fanPmInRpmAvg.setStatus(_A)
_FanPmConformance_ObjectIdentity=ObjectIdentity
fanPmConformance=_FanPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,4,3))
_FanPmCompliances_ObjectIdentity=ObjectIdentity
fanPmCompliances=_FanPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,4,3,1))
_FanPmGroups_ObjectIdentity=ObjectIdentity
fanPmGroups=_FanPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,4,3,2))
fanPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,11,4,3,2,1))
fanPmGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:fanPmGroup.setStatus(_A)
fanPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,11,4,3,2,2))
fanPmRealGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:fanPmRealGroup.setStatus(_A)
fanPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,11,4,3,1,1))
fanPmCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:fanPmCompliance.setStatus(_A)
fanPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,11,4,3,1,2))
fanPmRealCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:fanPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fanPmMIB':fanPmMIB,'fanPmRealTable':fanPmRealTable,'fanPmRealEntry':fanPmRealEntry,_O:fanPmRealInRpmRaw,'fanPmTable':fanPmTable,'fanPmEntry':fanPmEntry,_I:fanPmTimestamp,_H:fanPmSampleDuration,_K:fanPmValidity,_L:fanPmInRpmMin,_M:fanPmInRpmMax,_N:fanPmInRpmAvg,'fanPmConformance':fanPmConformance,'fanPmCompliances':fanPmCompliances,'fanPmCompliance':fanPmCompliance,'fanPmRealCompliance':fanPmRealCompliance,'fanPmGroups':fanPmGroups,'fanPmGroup':fanPmGroup,_G:fanPmRealGroup})