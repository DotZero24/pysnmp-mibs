_N='nbsConnectivityStatus'
_M='nbsConnectivityDestAddr'
_L='nbsConnectivityDestAddrType'
_K='not-accessible'
_J='nbsConnectivityOrdinalIndex'
_I='nbsConnectivitySourceIfIndex'
_H='nbsCmmcSlotIndex'
_G='nbsCmmcPortIndex'
_F='nbsCmmcChassisIndex'
_E='Integer32'
_D='NBS-CMMC-MIB'
_C='NBS-CONNECTIVITY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
nbsCmmcChassisIndex,nbsCmmcPortIndex,nbsCmmcSlotIndex=mibBuilder.importSymbols(_D,_F,_G,_H)
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsConnectivityMib=ModuleIdentity((1,3,6,1,4,1,629,238))
_NbsConnectivityGrp_ObjectIdentity=ObjectIdentity
nbsConnectivityGrp=_NbsConnectivityGrp_ObjectIdentity((1,3,6,1,4,1,629,238,1))
if mibBuilder.loadTexts:nbsConnectivityGrp.setStatus(_A)
_NbsConnectivityTable_Object=MibTable
nbsConnectivityTable=_NbsConnectivityTable_Object((1,3,6,1,4,1,629,238,1,1))
if mibBuilder.loadTexts:nbsConnectivityTable.setStatus(_A)
_NbsConnectivityEntry_Object=MibTableRow
nbsConnectivityEntry=_NbsConnectivityEntry_Object((1,3,6,1,4,1,629,238,1,1,1))
nbsConnectivityEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:nbsConnectivityEntry.setStatus(_A)
_NbsConnectivitySourceIfIndex_Type=InterfaceIndex
_NbsConnectivitySourceIfIndex_Object=MibTableColumn
nbsConnectivitySourceIfIndex=_NbsConnectivitySourceIfIndex_Object((1,3,6,1,4,1,629,238,1,1,1,10),_NbsConnectivitySourceIfIndex_Type())
nbsConnectivitySourceIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:nbsConnectivitySourceIfIndex.setStatus(_A)
class _NbsConnectivityOrdinalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_NbsConnectivityOrdinalIndex_Type.__name__=_E
_NbsConnectivityOrdinalIndex_Object=MibTableColumn
nbsConnectivityOrdinalIndex=_NbsConnectivityOrdinalIndex_Object((1,3,6,1,4,1,629,238,1,1,1,11),_NbsConnectivityOrdinalIndex_Type())
nbsConnectivityOrdinalIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:nbsConnectivityOrdinalIndex.setStatus(_A)
_NbsConnectivityDestIfIndex_Type=InterfaceIndex
_NbsConnectivityDestIfIndex_Object=MibTableColumn
nbsConnectivityDestIfIndex=_NbsConnectivityDestIfIndex_Object((1,3,6,1,4,1,629,238,1,1,1,20),_NbsConnectivityDestIfIndex_Type())
nbsConnectivityDestIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsConnectivityDestIfIndex.setStatus(_A)
_NbsConnectivityDestIPAddress_Type=IpAddress
_NbsConnectivityDestIPAddress_Object=MibTableColumn
nbsConnectivityDestIPAddress=_NbsConnectivityDestIPAddress_Object((1,3,6,1,4,1,629,238,1,1,1,30),_NbsConnectivityDestIPAddress_Type())
nbsConnectivityDestIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsConnectivityDestIPAddress.setStatus('deprecated')
_NbsConnectivityDestAddrType_Type=InetAddressType
_NbsConnectivityDestAddrType_Object=MibTableColumn
nbsConnectivityDestAddrType=_NbsConnectivityDestAddrType_Object((1,3,6,1,4,1,629,238,1,1,1,40),_NbsConnectivityDestAddrType_Type())
nbsConnectivityDestAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsConnectivityDestAddrType.setStatus(_A)
_NbsConnectivityDestAddr_Type=InetAddress
_NbsConnectivityDestAddr_Object=MibTableColumn
nbsConnectivityDestAddr=_NbsConnectivityDestAddr_Object((1,3,6,1,4,1,629,238,1,1,1,50),_NbsConnectivityDestAddr_Type())
nbsConnectivityDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsConnectivityDestAddr.setStatus(_A)
class _NbsConnectivityStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('up',1),('down',2),('unknown',3),('notSupported',4),('sourceBlocked',5),('destBlocked',6)))
_NbsConnectivityStatus_Type.__name__=_E
_NbsConnectivityStatus_Object=MibTableColumn
nbsConnectivityStatus=_NbsConnectivityStatus_Object((1,3,6,1,4,1,629,238,1,1,1,60),_NbsConnectivityStatus_Type())
nbsConnectivityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsConnectivityStatus.setStatus(_A)
_NbsConnectivityDestV6AddrType_Type=InetAddressType
_NbsConnectivityDestV6AddrType_Object=MibTableColumn
nbsConnectivityDestV6AddrType=_NbsConnectivityDestV6AddrType_Object((1,3,6,1,4,1,629,238,1,1,1,70),_NbsConnectivityDestV6AddrType_Type())
nbsConnectivityDestV6AddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsConnectivityDestV6AddrType.setStatus(_A)
_NbsConnectivityDestV6Addr_Type=InetAddress
_NbsConnectivityDestV6Addr_Object=MibTableColumn
nbsConnectivityDestV6Addr=_NbsConnectivityDestV6Addr_Object((1,3,6,1,4,1,629,238,1,1,1,80),_NbsConnectivityDestV6Addr_Type())
nbsConnectivityDestV6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsConnectivityDestV6Addr.setStatus(_A)
_NbsConnectivityTraps_ObjectIdentity=ObjectIdentity
nbsConnectivityTraps=_NbsConnectivityTraps_ObjectIdentity((1,3,6,1,4,1,629,238,100))
if mibBuilder.loadTexts:nbsConnectivityTraps.setStatus(_A)
_NbsConnectivityEvent_ObjectIdentity=ObjectIdentity
nbsConnectivityEvent=_NbsConnectivityEvent_ObjectIdentity((1,3,6,1,4,1,629,238,100,0))
if mibBuilder.loadTexts:nbsConnectivityEvent.setStatus(_A)
nbsConnectivityChanged=NotificationType((1,3,6,1,4,1,629,238,100,0,10))
nbsConnectivityChanged.setObjects(*((_D,_F),(_D,_H),(_D,_G),(_C,_L),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:nbsConnectivityChanged.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nbsConnectivityMib':nbsConnectivityMib,'nbsConnectivityGrp':nbsConnectivityGrp,'nbsConnectivityTable':nbsConnectivityTable,'nbsConnectivityEntry':nbsConnectivityEntry,_I:nbsConnectivitySourceIfIndex,_J:nbsConnectivityOrdinalIndex,'nbsConnectivityDestIfIndex':nbsConnectivityDestIfIndex,'nbsConnectivityDestIPAddress':nbsConnectivityDestIPAddress,_L:nbsConnectivityDestAddrType,_M:nbsConnectivityDestAddr,_N:nbsConnectivityStatus,'nbsConnectivityDestV6AddrType':nbsConnectivityDestV6AddrType,'nbsConnectivityDestV6Addr':nbsConnectivityDestV6Addr,'nbsConnectivityTraps':nbsConnectivityTraps,'nbsConnectivityEvent':nbsConnectivityEvent,'nbsConnectivityChanged':nbsConnectivityChanged})