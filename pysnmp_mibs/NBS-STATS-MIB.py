_H='read-write'
_G='clearing'
_F='counting'
_E='notSupported'
_D='nbsStatInfoIndex'
_C='NBS-STATS-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsStatsMib=ModuleIdentity((1,3,6,1,4,1,629,233))
_NbsStatInfoGrp_ObjectIdentity=ObjectIdentity
nbsStatInfoGrp=_NbsStatInfoGrp_ObjectIdentity((1,3,6,1,4,1,629,233,1))
if mibBuilder.loadTexts:nbsStatInfoGrp.setStatus(_A)
_NbsStatInfoTable_Object=MibTable
nbsStatInfoTable=_NbsStatInfoTable_Object((1,3,6,1,4,1,629,233,1,10))
if mibBuilder.loadTexts:nbsStatInfoTable.setStatus(_A)
_NbsStatInfoEntry_Object=MibTableRow
nbsStatInfoEntry=_NbsStatInfoEntry_Object((1,3,6,1,4,1,629,233,1,10,1))
nbsStatInfoEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:nbsStatInfoEntry.setStatus(_A)
_NbsStatInfoIndex_Type=InterfaceIndex
_NbsStatInfoIndex_Object=MibTableColumn
nbsStatInfoIndex=_NbsStatInfoIndex_Object((1,3,6,1,4,1,629,233,1,10,1,1),_NbsStatInfoIndex_Type())
nbsStatInfoIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:nbsStatInfoIndex.setStatus(_A)
class _NbsStatInfoCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NbsStatInfoCounters_Type.__name__=_B
_NbsStatInfoCounters_Object=MibTableColumn
nbsStatInfoCounters=_NbsStatInfoCounters_Object((1,3,6,1,4,1,629,233,1,10,1,2),_NbsStatInfoCounters_Type())
nbsStatInfoCounters.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsStatInfoCounters.setStatus(_A)
class _NbsStatInfoPmData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NbsStatInfoPmData_Type.__name__=_B
_NbsStatInfoPmData_Object=MibTableColumn
nbsStatInfoPmData=_NbsStatInfoPmData_Object((1,3,6,1,4,1,629,233,1,10,1,3),_NbsStatInfoPmData_Type())
nbsStatInfoPmData.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsStatInfoPmData.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nbsStatsMib':nbsStatsMib,'nbsStatInfoGrp':nbsStatInfoGrp,'nbsStatInfoTable':nbsStatInfoTable,'nbsStatInfoEntry':nbsStatInfoEntry,_D:nbsStatInfoIndex,'nbsStatInfoCounters':nbsStatInfoCounters,'nbsStatInfoPmData':nbsStatInfoPmData})