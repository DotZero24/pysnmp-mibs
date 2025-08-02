_E='read-only'
_D='nbsFecCfgIfIndex'
_C='NBS-FEC-MIB'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsFecMib=ModuleIdentity((1,3,6,1,4,1,629,232))
class NbsFecCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('notSupported',0),('noFec',1),('zero',2),('gfec',3),('ufec7',4),('ufec10',5),('ufec25',6),('hgfec7',7),('sdfec0',8),('sdfec1',9),('sdfec2',10),('sdfec3',11),('g975i4',12),('g975i7',13),('xfec7',14),('sdfec15',15),('staircase',16)))
_NbsFecCfgGrp_ObjectIdentity=ObjectIdentity
nbsFecCfgGrp=_NbsFecCfgGrp_ObjectIdentity((1,3,6,1,4,1,629,232,1))
if mibBuilder.loadTexts:nbsFecCfgGrp.setStatus(_A)
_NbsFecCfgTable_Object=MibTable
nbsFecCfgTable=_NbsFecCfgTable_Object((1,3,6,1,4,1,629,232,1,1))
if mibBuilder.loadTexts:nbsFecCfgTable.setStatus(_A)
_NbsFecCfgEntry_Object=MibTableRow
nbsFecCfgEntry=_NbsFecCfgEntry_Object((1,3,6,1,4,1,629,232,1,1,1))
nbsFecCfgEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:nbsFecCfgEntry.setStatus(_A)
_NbsFecCfgIfIndex_Type=InterfaceIndex
_NbsFecCfgIfIndex_Object=MibTableColumn
nbsFecCfgIfIndex=_NbsFecCfgIfIndex_Object((1,3,6,1,4,1,629,232,1,1,1,1),_NbsFecCfgIfIndex_Type())
nbsFecCfgIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nbsFecCfgIfIndex.setStatus(_A)
class _NbsFecCfgCodeCaps_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_NbsFecCfgCodeCaps_Type.__name__=_B
_NbsFecCfgCodeCaps_Object=MibTableColumn
nbsFecCfgCodeCaps=_NbsFecCfgCodeCaps_Object((1,3,6,1,4,1,629,232,1,1,1,2),_NbsFecCfgCodeCaps_Type())
nbsFecCfgCodeCaps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsFecCfgCodeCaps.setStatus(_A)
_NbsFecCfgCodeAdmin_Type=NbsFecCode
_NbsFecCfgCodeAdmin_Object=MibTableColumn
nbsFecCfgCodeAdmin=_NbsFecCfgCodeAdmin_Object((1,3,6,1,4,1,629,232,1,1,1,3),_NbsFecCfgCodeAdmin_Type())
nbsFecCfgCodeAdmin.setMaxAccess('read-write')
if mibBuilder.loadTexts:nbsFecCfgCodeAdmin.setStatus(_A)
_NbsFecCfgCodeOper_Type=NbsFecCode
_NbsFecCfgCodeOper_Object=MibTableColumn
nbsFecCfgCodeOper=_NbsFecCfgCodeOper_Object((1,3,6,1,4,1,629,232,1,1,1,4),_NbsFecCfgCodeOper_Type())
nbsFecCfgCodeOper.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsFecCfgCodeOper.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'NbsFecCode':NbsFecCode,'nbsFecMib':nbsFecMib,'nbsFecCfgGrp':nbsFecCfgGrp,'nbsFecCfgTable':nbsFecCfgTable,'nbsFecCfgEntry':nbsFecCfgEntry,_D:nbsFecCfgIfIndex,'nbsFecCfgCodeCaps':nbsFecCfgCodeCaps,'nbsFecCfgCodeAdmin':nbsFecCfgCodeAdmin,'nbsFecCfgCodeOper':nbsFecCfgCodeOper})