_E='deprecated'
_D='ipAddr'
_C='ELTEX-MES-IP-OSPF-MTU-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
eltMesIpOspfMtu=ModuleIdentity((1,3,6,1,4,1,35265,1,23,4))
if mibBuilder.loadTexts:eltMesIpOspfMtu.setRevisions(('2013-08-30 00:00',))
_EltIpOspfMtuTable_Object=MibTable
eltIpOspfMtuTable=_EltIpOspfMtuTable_Object((1,3,6,1,4,1,35265,1,23,4,1))
if mibBuilder.loadTexts:eltIpOspfMtuTable.setStatus(_A)
_EltIpOspfMtuEntry_Object=MibTableRow
eltIpOspfMtuEntry=_EltIpOspfMtuEntry_Object((1,3,6,1,4,1,35265,1,23,4,1,1))
eltIpOspfMtuEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:eltIpOspfMtuEntry.setStatus(_A)
_IpAddr_Type=IpAddress
_IpAddr_Object=MibTableColumn
ipAddr=_IpAddr_Object((1,3,6,1,4,1,35265,1,23,4,1,1,1),_IpAddr_Type())
ipAddr.setMaxAccess('read-only')
if mibBuilder.loadTexts:ipAddr.setStatus(_E)
class _IpOspfMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,10218))
_IpOspfMtu_Type.__name__=_B
_IpOspfMtu_Object=MibTableColumn
ipOspfMtu=_IpOspfMtu_Object((1,3,6,1,4,1,35265,1,23,4,1,1,2),_IpOspfMtu_Type())
ipOspfMtu.setMaxAccess('read-write')
if mibBuilder.loadTexts:ipOspfMtu.setStatus(_E)
_IpOspfMtuRowStatus_Type=RowStatus
_IpOspfMtuRowStatus_Object=MibTableColumn
ipOspfMtuRowStatus=_IpOspfMtuRowStatus_Object((1,3,6,1,4,1,35265,1,23,4,1,1,3),_IpOspfMtuRowStatus_Type())
ipOspfMtuRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:ipOspfMtuRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'eltMesIpOspfMtu':eltMesIpOspfMtu,'eltIpOspfMtuTable':eltIpOspfMtuTable,'eltIpOspfMtuEntry':eltIpOspfMtuEntry,_D:ipAddr,'ipOspfMtu':ipOspfMtu,'ipOspfMtuRowStatus':ipOspfMtuRowStatus})