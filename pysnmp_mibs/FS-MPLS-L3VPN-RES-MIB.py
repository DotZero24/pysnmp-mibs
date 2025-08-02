_E='fsmplsL3VpnResVrfName'
_D='fsmplsL3VpnResPeAddr'
_C='FS-MPLS-L3VPN-RES-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bgp4PathAttrIpAddrPrefix,bgp4PathAttrIpAddrPrefixLen,bgp4PathAttrPeer=mibBuilder.importSymbols('BGP4-MIB','bgp4PathAttrIpAddrPrefix','bgp4PathAttrIpAddrPrefixLen','bgp4PathAttrPeer')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
mplsL3VpnVrfName,=mibBuilder.importSymbols('MPLS-L3VPN-STD-MIB','mplsL3VpnVrfName')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
fsmplsL3VpnResMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,123))
if mibBuilder.loadTexts:fsmplsL3VpnResMIB.setRevisions(('2013-02-21 00:00',))
_FsmplsL3VpnResMIBObjects_ObjectIdentity=ObjectIdentity
fsmplsL3VpnResMIBObjects=_FsmplsL3VpnResMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,123,1))
_FsmplsL3VpnResTable_Object=MibTable
fsmplsL3VpnResTable=_FsmplsL3VpnResTable_Object((1,3,6,1,4,1,52642,1,1,10,2,123,1,1))
if mibBuilder.loadTexts:fsmplsL3VpnResTable.setStatus(_A)
_FsmplsL3VpnResEntry_Object=MibTableRow
fsmplsL3VpnResEntry=_FsmplsL3VpnResEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,123,1,1,1))
fsmplsL3VpnResEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:fsmplsL3VpnResEntry.setStatus(_A)
_FsmplsL3VpnResPeAddr_Type=InetAddress
_FsmplsL3VpnResPeAddr_Object=MibTableColumn
fsmplsL3VpnResPeAddr=_FsmplsL3VpnResPeAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,123,1,1,1,1),_FsmplsL3VpnResPeAddr_Type())
fsmplsL3VpnResPeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsmplsL3VpnResPeAddr.setStatus(_A)
_FsmplsL3VpnResVrfName_Type=DisplayString
_FsmplsL3VpnResVrfName_Object=MibTableColumn
fsmplsL3VpnResVrfName=_FsmplsL3VpnResVrfName_Object((1,3,6,1,4,1,52642,1,1,10,2,123,1,1,1,2),_FsmplsL3VpnResVrfName_Type())
fsmplsL3VpnResVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsmplsL3VpnResVrfName.setStatus(_A)
_FsmplsL3VpnResRtCollect_Type=DisplayString
_FsmplsL3VpnResRtCollect_Object=MibTableColumn
fsmplsL3VpnResRtCollect=_FsmplsL3VpnResRtCollect_Object((1,3,6,1,4,1,52642,1,1,10,2,123,1,1,1,3),_FsmplsL3VpnResRtCollect_Type())
fsmplsL3VpnResRtCollect.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsmplsL3VpnResRtCollect.setStatus(_A)
_FsmplsL3VpnResRdCollect_Type=DisplayString
_FsmplsL3VpnResRdCollect_Object=MibTableColumn
fsmplsL3VpnResRdCollect=_FsmplsL3VpnResRdCollect_Object((1,3,6,1,4,1,52642,1,1,10,2,123,1,1,1,4),_FsmplsL3VpnResRdCollect_Type())
fsmplsL3VpnResRdCollect.setMaxAccess(_B)
if mibBuilder.loadTexts:fsmplsL3VpnResRdCollect.setStatus(_A)
_FsmplsL3VpnResIntfAddr_Type=InetAddress
_FsmplsL3VpnResIntfAddr_Object=MibTableColumn
fsmplsL3VpnResIntfAddr=_FsmplsL3VpnResIntfAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,123,1,1,1,5),_FsmplsL3VpnResIntfAddr_Type())
fsmplsL3VpnResIntfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsmplsL3VpnResIntfAddr.setStatus(_A)
_FsmplsL3VpnResImptRt_Type=DisplayString
_FsmplsL3VpnResImptRt_Object=MibTableColumn
fsmplsL3VpnResImptRt=_FsmplsL3VpnResImptRt_Object((1,3,6,1,4,1,52642,1,1,10,2,123,1,1,1,6),_FsmplsL3VpnResImptRt_Type())
fsmplsL3VpnResImptRt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsmplsL3VpnResImptRt.setStatus(_A)
_FsmplsL3VpnResExptRt_Type=DisplayString
_FsmplsL3VpnResExptRt_Object=MibTableColumn
fsmplsL3VpnResExptRt=_FsmplsL3VpnResExptRt_Object((1,3,6,1,4,1,52642,1,1,10,2,123,1,1,1,7),_FsmplsL3VpnResExptRt_Type())
fsmplsL3VpnResExptRt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsmplsL3VpnResExptRt.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsmplsL3VpnResMIB':fsmplsL3VpnResMIB,'fsmplsL3VpnResMIBObjects':fsmplsL3VpnResMIBObjects,'fsmplsL3VpnResTable':fsmplsL3VpnResTable,'fsmplsL3VpnResEntry':fsmplsL3VpnResEntry,_D:fsmplsL3VpnResPeAddr,_E:fsmplsL3VpnResVrfName,'fsmplsL3VpnResRtCollect':fsmplsL3VpnResRtCollect,'fsmplsL3VpnResRdCollect':fsmplsL3VpnResRdCollect,'fsmplsL3VpnResIntfAddr':fsmplsL3VpnResIntfAddr,'fsmplsL3VpnResImptRt':fsmplsL3VpnResImptRt,'fsmplsL3VpnResExptRt':fsmplsL3VpnResExptRt})