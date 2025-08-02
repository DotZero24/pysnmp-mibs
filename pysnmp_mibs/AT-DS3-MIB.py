_I='ds3TrapInterval'
_H='ds3TrapLoc'
_G='ds3TrapError'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='AT-DS3-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB','DisplayStringUnsized','modules')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ds3=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,109))
if mibBuilder.loadTexts:ds3.setRevisions(('2006-06-28 12:22',))
_Ds3Traps_ObjectIdentity=ObjectIdentity
ds3Traps=_Ds3Traps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,109,0))
_Ds3TrapTable_Object=MibTable
ds3TrapTable=_Ds3TrapTable_Object((1,3,6,1,4,1,207,8,4,4,4,109,1))
if mibBuilder.loadTexts:ds3TrapTable.setStatus(_A)
_Ds3TrapEntry_Object=MibTableRow
ds3TrapEntry=_Ds3TrapEntry_Object((1,3,6,1,4,1,207,8,4,4,4,109,1,1))
ds3TrapEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ds3TrapEntry.setStatus(_A)
class _Ds3TcaTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Ds3TcaTrapEnable_Type.__name__=_B
_Ds3TcaTrapEnable_Object=MibTableColumn
ds3TcaTrapEnable=_Ds3TcaTrapEnable_Object((1,3,6,1,4,1,207,8,4,4,4,109,1,1,1),_Ds3TcaTrapEnable_Type())
ds3TcaTrapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:ds3TcaTrapEnable.setStatus(_A)
class _Ds3TrapError_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('ds3NoError',1),('ds3PES',2),('ds3PSES',3),('ds3SEFs',4),('ds3UAS',5),('ds3LCVs',6),('ds3PCVs',7),('ds3LESs',8),('ds3CCVs',9),('ds3CESs',10),('ds3CSESs',11)))
_Ds3TrapError_Type.__name__=_B
_Ds3TrapError_Object=MibTableColumn
ds3TrapError=_Ds3TrapError_Object((1,3,6,1,4,1,207,8,4,4,4,109,1,1,2),_Ds3TrapError_Type())
ds3TrapError.setMaxAccess(_D)
if mibBuilder.loadTexts:ds3TrapError.setStatus(_A)
class _Ds3TrapLoc_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ds3NoLoc',1),('ds3Near',2),('ds3Far',3)))
_Ds3TrapLoc_Type.__name__=_B
_Ds3TrapLoc_Object=MibTableColumn
ds3TrapLoc=_Ds3TrapLoc_Object((1,3,6,1,4,1,207,8,4,4,4,109,1,1,3),_Ds3TrapLoc_Type())
ds3TrapLoc.setMaxAccess(_D)
if mibBuilder.loadTexts:ds3TrapLoc.setStatus(_A)
class _Ds3TrapInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ds3NoInt',1),('ds3Fifteen',2),('ds3Twentyfour',3)))
_Ds3TrapInterval_Type.__name__=_B
_Ds3TrapInterval_Object=MibTableColumn
ds3TrapInterval=_Ds3TrapInterval_Object((1,3,6,1,4,1,207,8,4,4,4,109,1,1,4),_Ds3TrapInterval_Type())
ds3TrapInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ds3TrapInterval.setStatus(_A)
tcaTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,109,0,1))
tcaTrap.setObjects(*((_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:tcaTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ds3':ds3,'ds3Traps':ds3Traps,'tcaTrap':tcaTrap,'ds3TrapTable':ds3TrapTable,'ds3TrapEntry':ds3TrapEntry,'ds3TcaTrapEnable':ds3TcaTrapEnable,_G:ds3TrapError,_H:ds3TrapLoc,_I:ds3TrapInterval})