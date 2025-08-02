_E='eltOspfIfAddress'
_D='ELTEX-IP-OSPF-IF-MIB'
_C='TruthValue'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
eltMesOspf,=mibBuilder.importSymbols('ELTEX-MES-IP','eltMesOspf')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_C)
_EltIpOspfIfTable_Object=MibTable
eltIpOspfIfTable=_EltIpOspfIfTable_Object((1,3,6,1,4,1,35265,1,23,91,1,2))
if mibBuilder.loadTexts:eltIpOspfIfTable.setStatus(_A)
_EltIpOspfIfEntry_Object=MibTableRow
eltIpOspfIfEntry=_EltIpOspfIfEntry_Object((1,3,6,1,4,1,35265,1,23,91,1,2,1))
eltIpOspfIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:eltIpOspfIfEntry.setStatus(_A)
_EltOspfIfAddress_Type=IpAddress
_EltOspfIfAddress_Object=MibTableColumn
eltOspfIfAddress=_EltOspfIfAddress_Object((1,3,6,1,4,1,35265,1,23,91,1,2,1,1),_EltOspfIfAddress_Type())
eltOspfIfAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eltOspfIfAddress.setStatus(_A)
class _EltOspfIfPassiveDefault_Type(TruthValue):defaultValue=2
_EltOspfIfPassiveDefault_Type.__name__=_C
_EltOspfIfPassiveDefault_Object=MibTableColumn
eltOspfIfPassiveDefault=_EltOspfIfPassiveDefault_Object((1,3,6,1,4,1,35265,1,23,91,1,2,1,2),_EltOspfIfPassiveDefault_Type())
eltOspfIfPassiveDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:eltOspfIfPassiveDefault.setStatus(_A)
_EltOspfIfPassiveList_Type=PortList
_EltOspfIfPassiveList_Object=MibTableColumn
eltOspfIfPassiveList=_EltOspfIfPassiveList_Object((1,3,6,1,4,1,35265,1,23,91,1,2,1,3),_EltOspfIfPassiveList_Type())
eltOspfIfPassiveList.setMaxAccess(_B)
if mibBuilder.loadTexts:eltOspfIfPassiveList.setStatus(_A)
_EltOspfIfStatus_Type=RowStatus
_EltOspfIfStatus_Object=MibTableColumn
eltOspfIfStatus=_EltOspfIfStatus_Object((1,3,6,1,4,1,35265,1,23,91,1,2,1,4),_EltOspfIfStatus_Type())
eltOspfIfStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:eltOspfIfStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'eltIpOspfIfTable':eltIpOspfIfTable,'eltIpOspfIfEntry':eltIpOspfIfEntry,_E:eltOspfIfAddress,'eltOspfIfPassiveDefault':eltOspfIfPassiveDefault,'eltOspfIfPassiveList':eltOspfIfPassiveList,'eltOspfIfStatus':eltOspfIfStatus})