_O='oscPtpPmRealGroup'
_N='oscPtpPmGroup'
_M='oscPtpPmRealOscOPR'
_L='oscPtpPmOscOPRAve'
_K='oscPtpPmOscOPRMax'
_J='oscPtpPmOscOPRMin'
_I='not-accessible'
_H='oscPtpPmTimestamp'
_G='oscPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-OSCPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
oscPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,34))
if mibBuilder.loadTexts:oscPtpPmMIB.setRevisions(('2012-10-20 00:00',))
_OscPtpPmRealTable_Object=MibTable
oscPtpPmRealTable=_OscPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,34,1))
if mibBuilder.loadTexts:oscPtpPmRealTable.setStatus(_A)
_OscPtpPmRealEntry_Object=MibTableRow
oscPtpPmRealEntry=_OscPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,34,1,1))
oscPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oscPtpPmRealEntry.setStatus(_A)
_OscPtpPmRealOscOPR_Type=FloatHundredths
_OscPtpPmRealOscOPR_Object=MibTableColumn
oscPtpPmRealOscOPR=_OscPtpPmRealOscOPR_Object((1,3,6,1,4,1,21296,2,2,2,3,34,1,1,1),_OscPtpPmRealOscOPR_Type())
oscPtpPmRealOscOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:oscPtpPmRealOscOPR.setStatus(_A)
_OscPtpPmTable_Object=MibTable
oscPtpPmTable=_OscPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,34,2))
if mibBuilder.loadTexts:oscPtpPmTable.setStatus(_A)
_OscPtpPmEntry_Object=MibTableRow
oscPtpPmEntry=_OscPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,34,2,1))
oscPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:oscPtpPmEntry.setStatus(_A)
class _OscPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OscPtpPmTimestamp_Type.__name__=_F
_OscPtpPmTimestamp_Object=MibTableColumn
oscPtpPmTimestamp=_OscPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,34,2,1,1),_OscPtpPmTimestamp_Type())
oscPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:oscPtpPmTimestamp.setStatus(_A)
class _OscPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_OscPtpPmSampleDuration_Type.__name__=_F
_OscPtpPmSampleDuration_Object=MibTableColumn
oscPtpPmSampleDuration=_OscPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,34,2,1,2),_OscPtpPmSampleDuration_Type())
oscPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:oscPtpPmSampleDuration.setStatus(_A)
_OscPtpPmOscOPRMin_Type=FloatHundredths
_OscPtpPmOscOPRMin_Object=MibTableColumn
oscPtpPmOscOPRMin=_OscPtpPmOscOPRMin_Object((1,3,6,1,4,1,21296,2,2,2,3,34,2,1,3),_OscPtpPmOscOPRMin_Type())
oscPtpPmOscOPRMin.setMaxAccess(_C)
if mibBuilder.loadTexts:oscPtpPmOscOPRMin.setStatus(_A)
_OscPtpPmOscOPRMax_Type=FloatHundredths
_OscPtpPmOscOPRMax_Object=MibTableColumn
oscPtpPmOscOPRMax=_OscPtpPmOscOPRMax_Object((1,3,6,1,4,1,21296,2,2,2,3,34,2,1,4),_OscPtpPmOscOPRMax_Type())
oscPtpPmOscOPRMax.setMaxAccess(_C)
if mibBuilder.loadTexts:oscPtpPmOscOPRMax.setStatus(_A)
_OscPtpPmOscOPRAve_Type=FloatHundredths
_OscPtpPmOscOPRAve_Object=MibTableColumn
oscPtpPmOscOPRAve=_OscPtpPmOscOPRAve_Object((1,3,6,1,4,1,21296,2,2,2,3,34,2,1,5),_OscPtpPmOscOPRAve_Type())
oscPtpPmOscOPRAve.setMaxAccess(_C)
if mibBuilder.loadTexts:oscPtpPmOscOPRAve.setStatus(_A)
_OscPtpPmConformance_ObjectIdentity=ObjectIdentity
oscPtpPmConformance=_OscPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,34,3))
_OscPtpPmCompliances_ObjectIdentity=ObjectIdentity
oscPtpPmCompliances=_OscPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,34,3,1))
_OscPtpPmGroups_ObjectIdentity=ObjectIdentity
oscPtpPmGroups=_OscPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,34,3,2))
oscPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,34,3,2,1))
oscPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:oscPtpPmGroup.setStatus(_A)
oscPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,34,3,2,2))
oscPtpPmRealGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:oscPtpPmRealGroup.setStatus(_A)
oscPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,34,3,1,1))
oscPtpPmCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:oscPtpPmCompliance.setStatus(_A)
oscPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,34,3,1,2))
oscPtpPmRealCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:oscPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oscPtpPmMIB':oscPtpPmMIB,'oscPtpPmRealTable':oscPtpPmRealTable,'oscPtpPmRealEntry':oscPtpPmRealEntry,_M:oscPtpPmRealOscOPR,'oscPtpPmTable':oscPtpPmTable,'oscPtpPmEntry':oscPtpPmEntry,_H:oscPtpPmTimestamp,_G:oscPtpPmSampleDuration,_J:oscPtpPmOscOPRMin,_K:oscPtpPmOscOPRMax,_L:oscPtpPmOscOPRAve,'oscPtpPmConformance':oscPtpPmConformance,'oscPtpPmCompliances':oscPtpPmCompliances,'oscPtpPmCompliance':oscPtpPmCompliance,'oscPtpPmRealCompliance':oscPtpPmRealCompliance,'oscPtpPmGroups':oscPtpPmGroups,_N:oscPtpPmGroup,_O:oscPtpPmRealGroup})