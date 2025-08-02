_G='topologyL2LinkLocalPort'
_F='topologyL2LinkLocalIp'
_E='TruthValue'
_D='SL-L2TOPOLOGY-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slMain,=mibBuilder.importSymbols('SL-MAIN-MIB','slMain')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_E)
slL2Topology=ModuleIdentity((1,3,6,1,4,1,4515,1,3,10))
_TopologyL2Links_ObjectIdentity=ObjectIdentity
topologyL2Links=_TopologyL2Links_ObjectIdentity((1,3,6,1,4,1,4515,1,3,10,1))
_TopologyL2LinkTable_Object=MibTable
topologyL2LinkTable=_TopologyL2LinkTable_Object((1,3,6,1,4,1,4515,1,3,10,1,1))
if mibBuilder.loadTexts:topologyL2LinkTable.setStatus(_A)
_TopologyL2LinkEntry_Object=MibTableRow
topologyL2LinkEntry=_TopologyL2LinkEntry_Object((1,3,6,1,4,1,4515,1,3,10,1,1,1))
topologyL2LinkEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:topologyL2LinkEntry.setStatus(_A)
_TopologyL2LinkLocalIp_Type=IpAddress
_TopologyL2LinkLocalIp_Object=MibTableColumn
topologyL2LinkLocalIp=_TopologyL2LinkLocalIp_Object((1,3,6,1,4,1,4515,1,3,10,1,1,1,1),_TopologyL2LinkLocalIp_Type())
topologyL2LinkLocalIp.setMaxAccess(_B)
if mibBuilder.loadTexts:topologyL2LinkLocalIp.setStatus(_A)
_TopologyL2LinkLocalPort_Type=Integer32
_TopologyL2LinkLocalPort_Object=MibTableColumn
topologyL2LinkLocalPort=_TopologyL2LinkLocalPort_Object((1,3,6,1,4,1,4515,1,3,10,1,1,1,2),_TopologyL2LinkLocalPort_Type())
topologyL2LinkLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:topologyL2LinkLocalPort.setStatus(_A)
_TopologyL2LinkLocalMac_Type=PhysAddress
_TopologyL2LinkLocalMac_Object=MibTableColumn
topologyL2LinkLocalMac=_TopologyL2LinkLocalMac_Object((1,3,6,1,4,1,4515,1,3,10,1,1,1,3),_TopologyL2LinkLocalMac_Type())
topologyL2LinkLocalMac.setMaxAccess(_B)
if mibBuilder.loadTexts:topologyL2LinkLocalMac.setStatus(_A)
class _TopologyL2LinkLocalTid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TopologyL2LinkLocalTid_Type.__name__=_C
_TopologyL2LinkLocalTid_Object=MibTableColumn
topologyL2LinkLocalTid=_TopologyL2LinkLocalTid_Object((1,3,6,1,4,1,4515,1,3,10,1,1,1,4),_TopologyL2LinkLocalTid_Type())
topologyL2LinkLocalTid.setMaxAccess(_B)
if mibBuilder.loadTexts:topologyL2LinkLocalTid.setStatus(_A)
_TopologyL2LinkRemoteIp_Type=IpAddress
_TopologyL2LinkRemoteIp_Object=MibTableColumn
topologyL2LinkRemoteIp=_TopologyL2LinkRemoteIp_Object((1,3,6,1,4,1,4515,1,3,10,1,1,1,5),_TopologyL2LinkRemoteIp_Type())
topologyL2LinkRemoteIp.setMaxAccess(_B)
if mibBuilder.loadTexts:topologyL2LinkRemoteIp.setStatus(_A)
_TopologyL2LinkRemotePort_Type=Integer32
_TopologyL2LinkRemotePort_Object=MibTableColumn
topologyL2LinkRemotePort=_TopologyL2LinkRemotePort_Object((1,3,6,1,4,1,4515,1,3,10,1,1,1,6),_TopologyL2LinkRemotePort_Type())
topologyL2LinkRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:topologyL2LinkRemotePort.setStatus(_A)
_TopologyL2LinkRemoteMac_Type=PhysAddress
_TopologyL2LinkRemoteMac_Object=MibTableColumn
topologyL2LinkRemoteMac=_TopologyL2LinkRemoteMac_Object((1,3,6,1,4,1,4515,1,3,10,1,1,1,7),_TopologyL2LinkRemoteMac_Type())
topologyL2LinkRemoteMac.setMaxAccess(_B)
if mibBuilder.loadTexts:topologyL2LinkRemoteMac.setStatus(_A)
class _TopologyL2LinkRemoteTid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TopologyL2LinkRemoteTid_Type.__name__=_C
_TopologyL2LinkRemoteTid_Object=MibTableColumn
topologyL2LinkRemoteTid=_TopologyL2LinkRemoteTid_Object((1,3,6,1,4,1,4515,1,3,10,1,1,1,8),_TopologyL2LinkRemoteTid_Type())
topologyL2LinkRemoteTid.setMaxAccess(_B)
if mibBuilder.loadTexts:topologyL2LinkRemoteTid.setStatus(_A)
_TopologyL2Traps_ObjectIdentity=ObjectIdentity
topologyL2Traps=_TopologyL2Traps_ObjectIdentity((1,3,6,1,4,1,4515,1,3,10,2))
_TopologyL2LastChange_Type=TimeStamp
_TopologyL2LastChange_Object=MibScalar
topologyL2LastChange=_TopologyL2LastChange_Object((1,3,6,1,4,1,4515,1,3,10,2,1),_TopologyL2LastChange_Type())
topologyL2LastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:topologyL2LastChange.setStatus(_A)
class _TopologyL2ChangeTrapEnable_Type(TruthValue):defaultValue=1
_TopologyL2ChangeTrapEnable_Type.__name__=_E
_TopologyL2ChangeTrapEnable_Object=MibScalar
topologyL2ChangeTrapEnable=_TopologyL2ChangeTrapEnable_Object((1,3,6,1,4,1,4515,1,3,10,2,2),_TopologyL2ChangeTrapEnable_Type())
topologyL2ChangeTrapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:topologyL2ChangeTrapEnable.setStatus(_A)
topologyL2LinkChange=NotificationType((1,3,6,1,4,1,4515,1,3,10,2,3))
if mibBuilder.loadTexts:topologyL2LinkChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'slL2Topology':slL2Topology,'topologyL2Links':topologyL2Links,'topologyL2LinkTable':topologyL2LinkTable,'topologyL2LinkEntry':topologyL2LinkEntry,_F:topologyL2LinkLocalIp,_G:topologyL2LinkLocalPort,'topologyL2LinkLocalMac':topologyL2LinkLocalMac,'topologyL2LinkLocalTid':topologyL2LinkLocalTid,'topologyL2LinkRemoteIp':topologyL2LinkRemoteIp,'topologyL2LinkRemotePort':topologyL2LinkRemotePort,'topologyL2LinkRemoteMac':topologyL2LinkRemoteMac,'topologyL2LinkRemoteTid':topologyL2LinkRemoteTid,'topologyL2Traps':topologyL2Traps,'topologyL2LastChange':topologyL2LastChange,'topologyL2ChangeTrapEnable':topologyL2ChangeTrapEnable,'topologyL2LinkChange':topologyL2LinkChange})