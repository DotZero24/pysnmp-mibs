_H='enable'
_G='disable'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ndpManage,=mibBuilder.importSymbols('TPLINK-CLUSTER-MIB','ndpManage')
_NdpGlobalConfig_ObjectIdentity=ObjectIdentity
ndpGlobalConfig=_NdpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,33,1,1,1,1))
class _NdpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NdpStatus_Type.__name__=_B
_NdpStatus_Object=MibScalar
ndpStatus=_NdpStatus_Object((1,3,6,1,4,1,11863,6,33,1,1,1,1,1),_NdpStatus_Type())
ndpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ndpStatus.setStatus(_A)
class _NdpAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,255))
_NdpAgingTime_Type.__name__=_B
_NdpAgingTime_Object=MibScalar
ndpAgingTime=_NdpAgingTime_Object((1,3,6,1,4,1,11863,6,33,1,1,1,1,2),_NdpAgingTime_Type())
ndpAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ndpAgingTime.setStatus(_A)
class _NdpHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,254))
_NdpHelloTime_Type.__name__=_B
_NdpHelloTime_Object=MibScalar
ndpHelloTime=_NdpHelloTime_Object((1,3,6,1,4,1,11863,6,33,1,1,1,1,3),_NdpHelloTime_Type())
ndpHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ndpHelloTime.setStatus(_A)
_NdpPortTable_Object=MibTable
ndpPortTable=_NdpPortTable_Object((1,3,6,1,4,1,11863,6,33,1,1,1,2))
if mibBuilder.loadTexts:ndpPortTable.setStatus(_A)
_NdpPortEntry_Object=MibTableRow
ndpPortEntry=_NdpPortEntry_Object((1,3,6,1,4,1,11863,6,33,1,1,1,2,1))
ndpPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ndpPortEntry.setStatus(_A)
class _NdpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NdpPortStatus_Type.__name__=_B
_NdpPortStatus_Object=MibTableColumn
ndpPortStatus=_NdpPortStatus_Object((1,3,6,1,4,1,11863,6,33,1,1,1,2,1,2),_NdpPortStatus_Type())
ndpPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ndpPortStatus.setStatus(_A)
_NdpPortRecvPkt_Type=Integer32
_NdpPortRecvPkt_Object=MibTableColumn
ndpPortRecvPkt=_NdpPortRecvPkt_Object((1,3,6,1,4,1,11863,6,33,1,1,1,2,1,3),_NdpPortRecvPkt_Type())
ndpPortRecvPkt.setMaxAccess(_D)
if mibBuilder.loadTexts:ndpPortRecvPkt.setStatus(_A)
_NdpPortSendPkt_Type=Integer32
_NdpPortSendPkt_Object=MibTableColumn
ndpPortSendPkt=_NdpPortSendPkt_Object((1,3,6,1,4,1,11863,6,33,1,1,1,2,1,4),_NdpPortSendPkt_Type())
ndpPortSendPkt.setMaxAccess(_D)
if mibBuilder.loadTexts:ndpPortSendPkt.setStatus(_A)
_NdpPortErrPkt_Type=Integer32
_NdpPortErrPkt_Object=MibTableColumn
ndpPortErrPkt=_NdpPortErrPkt_Object((1,3,6,1,4,1,11863,6,33,1,1,1,2,1,5),_NdpPortErrPkt_Type())
ndpPortErrPkt.setMaxAccess(_D)
if mibBuilder.loadTexts:ndpPortErrPkt.setStatus(_A)
_NdpPortNeighborNum_Type=Integer32
_NdpPortNeighborNum_Object=MibTableColumn
ndpPortNeighborNum=_NdpPortNeighborNum_Object((1,3,6,1,4,1,11863,6,33,1,1,1,2,1,6),_NdpPortNeighborNum_Type())
ndpPortNeighborNum.setMaxAccess(_D)
if mibBuilder.loadTexts:ndpPortNeighborNum.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-NDP-MIB',**{'ndpGlobalConfig':ndpGlobalConfig,'ndpStatus':ndpStatus,'ndpAgingTime':ndpAgingTime,'ndpHelloTime':ndpHelloTime,'ndpPortTable':ndpPortTable,'ndpPortEntry':ndpPortEntry,'ndpPortStatus':ndpPortStatus,'ndpPortRecvPkt':ndpPortRecvPkt,'ndpPortSendPkt':ndpPortSendPkt,'ndpPortErrPkt':ndpPortErrPkt,'ndpPortNeighborNum':ndpPortNeighborNum})