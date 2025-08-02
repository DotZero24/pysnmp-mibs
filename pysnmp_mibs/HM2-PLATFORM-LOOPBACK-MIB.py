_E='read-write'
_D='hm2AgentLoopbackID'
_C='HM2-PLATFORM-LOOPBACK-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2PlatformMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2PlatformMibs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddressIPv4,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hm2PlatformLoopback=ModuleIdentity((1,3,6,1,4,1,248,12,22))
if mibBuilder.loadTexts:hm2PlatformLoopback.setRevisions(('2011-09-08 00:00',))
_Hm2AgentLoopbackGroup_ObjectIdentity=ObjectIdentity
hm2AgentLoopbackGroup=_Hm2AgentLoopbackGroup_ObjectIdentity((1,3,6,1,4,1,248,12,22,1))
_Hm2AgentLoopbackTable_Object=MibTable
hm2AgentLoopbackTable=_Hm2AgentLoopbackTable_Object((1,3,6,1,4,1,248,12,22,1,1))
if mibBuilder.loadTexts:hm2AgentLoopbackTable.setStatus(_A)
_Hm2AgentLoopbackEntry_Object=MibTableRow
hm2AgentLoopbackEntry=_Hm2AgentLoopbackEntry_Object((1,3,6,1,4,1,248,12,22,1,1,1))
hm2AgentLoopbackEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hm2AgentLoopbackEntry.setStatus(_A)
class _Hm2AgentLoopbackID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2AgentLoopbackID_Type.__name__=_B
_Hm2AgentLoopbackID_Object=MibTableColumn
hm2AgentLoopbackID=_Hm2AgentLoopbackID_Object((1,3,6,1,4,1,248,12,22,1,1,1,1),_Hm2AgentLoopbackID_Type())
hm2AgentLoopbackID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hm2AgentLoopbackID.setStatus(_A)
_Hm2AgentLoopbackIfIndex_Type=InterfaceIndex
_Hm2AgentLoopbackIfIndex_Object=MibTableColumn
hm2AgentLoopbackIfIndex=_Hm2AgentLoopbackIfIndex_Object((1,3,6,1,4,1,248,12,22,1,1,1,2),_Hm2AgentLoopbackIfIndex_Type())
hm2AgentLoopbackIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:hm2AgentLoopbackIfIndex.setStatus(_A)
_Hm2AgentLoopbackIPAddress_Type=InetAddressIPv4
_Hm2AgentLoopbackIPAddress_Object=MibTableColumn
hm2AgentLoopbackIPAddress=_Hm2AgentLoopbackIPAddress_Object((1,3,6,1,4,1,248,12,22,1,1,1,3),_Hm2AgentLoopbackIPAddress_Type())
hm2AgentLoopbackIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2AgentLoopbackIPAddress.setStatus(_A)
_Hm2AgentLoopbackIPSubnet_Type=InetAddressIPv4
_Hm2AgentLoopbackIPSubnet_Object=MibTableColumn
hm2AgentLoopbackIPSubnet=_Hm2AgentLoopbackIPSubnet_Object((1,3,6,1,4,1,248,12,22,1,1,1,4),_Hm2AgentLoopbackIPSubnet_Type())
hm2AgentLoopbackIPSubnet.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2AgentLoopbackIPSubnet.setStatus(_A)
_Hm2AgentLoopbackStatus_Type=RowStatus
_Hm2AgentLoopbackStatus_Object=MibTableColumn
hm2AgentLoopbackStatus=_Hm2AgentLoopbackStatus_Object((1,3,6,1,4,1,248,12,22,1,1,1,5),_Hm2AgentLoopbackStatus_Type())
hm2AgentLoopbackStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hm2AgentLoopbackStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hm2PlatformLoopback':hm2PlatformLoopback,'hm2AgentLoopbackGroup':hm2AgentLoopbackGroup,'hm2AgentLoopbackTable':hm2AgentLoopbackTable,'hm2AgentLoopbackEntry':hm2AgentLoopbackEntry,_D:hm2AgentLoopbackID,'hm2AgentLoopbackIfIndex':hm2AgentLoopbackIfIndex,'hm2AgentLoopbackIPAddress':hm2AgentLoopbackIPAddress,'hm2AgentLoopbackIPSubnet':hm2AgentLoopbackIPSubnet,'hm2AgentLoopbackStatus':hm2AgentLoopbackStatus})