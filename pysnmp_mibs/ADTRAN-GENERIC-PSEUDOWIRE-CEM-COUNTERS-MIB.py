_E='read-write'
_D='ifIndex'
_C='IF-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPseudowireCEMPerfID,adGenPseudowireCEMPerformance=mibBuilder.importSymbols('ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB','adGenPseudowireCEMPerfID','adGenPseudowireCEMPerformance')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenPseudowireCEMPerfModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,30,2,1))
if mibBuilder.loadTexts:adGenPseudowireCEMPerfModuleIdentity.setRevisions(('2011-04-28 00:00',))
_AdGenPseudowireCEMPerfProv_ObjectIdentity=ObjectIdentity
adGenPseudowireCEMPerfProv=_AdGenPseudowireCEMPerfProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,30,5,1))
_AdGenPseudowireCEMPerfProvTable_Object=MibTable
adGenPseudowireCEMPerfProvTable=_AdGenPseudowireCEMPerfProvTable_Object((1,3,6,1,4,1,664,5,70,30,5,1,1))
if mibBuilder.loadTexts:adGenPseudowireCEMPerfProvTable.setStatus(_A)
_AdGenPseudowireCEMPerfProvTableEntry_Object=MibTableRow
adGenPseudowireCEMPerfProvTableEntry=_AdGenPseudowireCEMPerfProvTableEntry_Object((1,3,6,1,4,1,664,5,70,30,5,1,1,1))
adGenPseudowireCEMPerfProvTableEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenPseudowireCEMPerfProvTableEntry.setStatus(_A)
_AdGenPseudowireCEMPerfErrorStr_Type=DisplayString
_AdGenPseudowireCEMPerfErrorStr_Object=MibTableColumn
adGenPseudowireCEMPerfErrorStr=_AdGenPseudowireCEMPerfErrorStr_Object((1,3,6,1,4,1,664,5,70,30,5,1,1,1,1),_AdGenPseudowireCEMPerfErrorStr_Type())
adGenPseudowireCEMPerfErrorStr.setMaxAccess('read-only')
if mibBuilder.loadTexts:adGenPseudowireCEMPerfErrorStr.setStatus(_A)
class _AdGenPseudowireCEMPerfClear15MinCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenPseudowireCEMPerfClear15MinCounters_Type.__name__=_B
_AdGenPseudowireCEMPerfClear15MinCounters_Object=MibTableColumn
adGenPseudowireCEMPerfClear15MinCounters=_AdGenPseudowireCEMPerfClear15MinCounters_Object((1,3,6,1,4,1,664,5,70,30,5,1,1,1,2),_AdGenPseudowireCEMPerfClear15MinCounters_Type())
adGenPseudowireCEMPerfClear15MinCounters.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPseudowireCEMPerfClear15MinCounters.setStatus(_A)
class _AdGenPseudowireCEMPerfClear24HrCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenPseudowireCEMPerfClear24HrCounters_Type.__name__=_B
_AdGenPseudowireCEMPerfClear24HrCounters_Object=MibTableColumn
adGenPseudowireCEMPerfClear24HrCounters=_AdGenPseudowireCEMPerfClear24HrCounters_Object((1,3,6,1,4,1,664,5,70,30,5,1,1,1,3),_AdGenPseudowireCEMPerfClear24HrCounters_Type())
adGenPseudowireCEMPerfClear24HrCounters.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPseudowireCEMPerfClear24HrCounters.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-MIB',**{'adGenPseudowireCEMPerfProv':adGenPseudowireCEMPerfProv,'adGenPseudowireCEMPerfProvTable':adGenPseudowireCEMPerfProvTable,'adGenPseudowireCEMPerfProvTableEntry':adGenPseudowireCEMPerfProvTableEntry,'adGenPseudowireCEMPerfErrorStr':adGenPseudowireCEMPerfErrorStr,'adGenPseudowireCEMPerfClear15MinCounters':adGenPseudowireCEMPerfClear15MinCounters,'adGenPseudowireCEMPerfClear24HrCounters':adGenPseudowireCEMPerfClear24HrCounters,'adGenPseudowireCEMPerfModuleIdentity':adGenPseudowireCEMPerfModuleIdentity})