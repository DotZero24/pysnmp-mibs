_K='fxsMeterPulseGroupVer1'
_J='fxsMeterPulseFreq'
_I='fxsMeterPauseDuration'
_H='fxsMeterPulseDuration'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='Unsigned32'
_B='MX-FXS-METER-PULSE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fxsMeterPulseMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,30))
if mibBuilder.loadTexts:fxsMeterPulseMIB.setRevisions(('1902-11-04 00:00',))
_FxsMeterPulseMIBObjects_ObjectIdentity=ObjectIdentity
fxsMeterPulseMIBObjects=_FxsMeterPulseMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,30,1))
_FxsMeterPulseTable_Object=MibTable
fxsMeterPulseTable=_FxsMeterPulseTable_Object((1,3,6,1,4,1,4935,99,30,1,30))
if mibBuilder.loadTexts:fxsMeterPulseTable.setStatus(_A)
_FxsMeterPulseEntry_Object=MibTableRow
fxsMeterPulseEntry=_FxsMeterPulseEntry_Object((1,3,6,1,4,1,4935,99,30,1,30,1))
fxsMeterPulseEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fxsMeterPulseEntry.setStatus(_A)
class _FxsMeterPulseDuration_Type(Unsigned32):defaultValue=160;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,220))
_FxsMeterPulseDuration_Type.__name__=_C
_FxsMeterPulseDuration_Object=MibTableColumn
fxsMeterPulseDuration=_FxsMeterPulseDuration_Object((1,3,6,1,4,1,4935,99,30,1,30,1,10),_FxsMeterPulseDuration_Type())
fxsMeterPulseDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:fxsMeterPulseDuration.setStatus(_A)
class _FxsMeterPauseDuration_Type(Unsigned32):defaultValue=360;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,600))
_FxsMeterPauseDuration_Type.__name__=_C
_FxsMeterPauseDuration_Object=MibTableColumn
fxsMeterPauseDuration=_FxsMeterPauseDuration_Object((1,3,6,1,4,1,4935,99,30,1,30,1,15),_FxsMeterPauseDuration_Type())
fxsMeterPauseDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:fxsMeterPauseDuration.setStatus(_A)
class _FxsMeterPulseFreq_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('freq-12-kHz',1),('freq-16-kHz',2)))
_FxsMeterPulseFreq_Type.__name__=_G
_FxsMeterPulseFreq_Object=MibScalar
fxsMeterPulseFreq=_FxsMeterPulseFreq_Object((1,3,6,1,4,1,4935,99,30,1,35),_FxsMeterPulseFreq_Type())
fxsMeterPulseFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:fxsMeterPulseFreq.setStatus(_A)
_FxsMeterPulseConformance_ObjectIdentity=ObjectIdentity
fxsMeterPulseConformance=_FxsMeterPulseConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,30,2))
_FxsMeterPulseCompliances_ObjectIdentity=ObjectIdentity
fxsMeterPulseCompliances=_FxsMeterPulseCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,30,2,1))
_FxsMeterPulseGroups_ObjectIdentity=ObjectIdentity
fxsMeterPulseGroups=_FxsMeterPulseGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,30,2,2))
fxsMeterPulseGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,30,2,2,1))
fxsMeterPulseGroupVer1.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:fxsMeterPulseGroupVer1.setStatus(_A)
fxsMeterPulseBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,30,2,1,1))
fxsMeterPulseBasicComplVer1.setObjects((_B,_K))
if mibBuilder.loadTexts:fxsMeterPulseBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fxsMeterPulseMIB':fxsMeterPulseMIB,'fxsMeterPulseMIBObjects':fxsMeterPulseMIBObjects,'fxsMeterPulseTable':fxsMeterPulseTable,'fxsMeterPulseEntry':fxsMeterPulseEntry,_H:fxsMeterPulseDuration,_I:fxsMeterPauseDuration,_J:fxsMeterPulseFreq,'fxsMeterPulseConformance':fxsMeterPulseConformance,'fxsMeterPulseCompliances':fxsMeterPulseCompliances,'fxsMeterPulseBasicComplVer1':fxsMeterPulseBasicComplVer1,'fxsMeterPulseGroups':fxsMeterPulseGroups,_K:fxsMeterPulseGroupVer1})