_F='eltIfExtEntry'
_E='ELTEX-MES-MIB-OBJECTS'
_D='DisplayString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIfMIBObjects,=mibBuilder.importSymbols('ELTEX-MES-IF-MIB','eltMesIfMIBObjects')
ifEntry,=mibBuilder.importSymbols('IF-MIB','ifEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_EltIfExtTable_Object=MibTable
eltIfExtTable=_EltIfExtTable_Object((1,3,6,1,4,1,35265,1,23,1,1,31,1,1))
if mibBuilder.loadTexts:eltIfExtTable.setStatus(_A)
_EltIfExtEntry_Object=MibTableRow
eltIfExtEntry=_EltIfExtEntry_Object((1,3,6,1,4,1,35265,1,23,1,1,31,1,1,1))
if mibBuilder.loadTexts:eltIfExtEntry.setStatus(_A)
class _EltIfLongDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_EltIfLongDescr_Type.__name__=_D
_EltIfLongDescr_Object=MibTableColumn
eltIfLongDescr=_EltIfLongDescr_Object((1,3,6,1,4,1,35265,1,23,1,1,31,1,1,1,1),_EltIfLongDescr_Type())
eltIfLongDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIfLongDescr.setStatus(_A)
class _EltIfAdminMtu_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(128,9000))
_EltIfAdminMtu_Type.__name__=_B
_EltIfAdminMtu_Object=MibTableColumn
eltIfAdminMtu=_EltIfAdminMtu_Object((1,3,6,1,4,1,35265,1,23,1,1,31,1,1,1,2),_EltIfAdminMtu_Type())
eltIfAdminMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIfAdminMtu.setStatus(_A)
class _EltIfUpDownTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_EltIfUpDownTrapEnable_Type.__name__=_B
_EltIfUpDownTrapEnable_Object=MibScalar
eltIfUpDownTrapEnable=_EltIfUpDownTrapEnable_Object((1,3,6,1,4,1,35265,1,23,1,1,31,1,7),_EltIfUpDownTrapEnable_Type())
eltIfUpDownTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIfUpDownTrapEnable.setStatus(_A)
ifEntry.registerAugmentions((_E,_F))
eltIfExtEntry.setIndexNames(*ifEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'eltIfExtTable':eltIfExtTable,_F:eltIfExtEntry,'eltIfLongDescr':eltIfLongDescr,'eltIfAdminMtu':eltIfAdminMtu,'eltIfUpDownTrapEnable':eltIfUpDownTrapEnable})