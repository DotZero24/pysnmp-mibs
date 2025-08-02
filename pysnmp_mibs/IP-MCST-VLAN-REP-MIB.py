_R='swIpMcstVlanRepDstVID'
_Q='swIpMcstVlanRepSrcAddr'
_P='swIpMcstVlanRepSrcAddrType'
_O='swIpMcstVlanRepGrpAddrEnd'
_N='swIpMcstVlanRepGrpAddrStart'
_M='swIpMcstVlanRepGrpAddrType'
_L='swIpMcstVlanRepSourceAddr'
_K='swIpMcstVlanRepSourceAddrType'
_J='swIpMcstVlanRepGroupAddr'
_I='swIpMcstVlanRepGroupAddrType'
_H='read-create'
_G='not-accessible'
_F='swIpMcstVlanRepName'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='IP-MCST-VLAN-REP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
swIpMcstVlanRepMIB=ModuleIdentity((1,3,6,1,4,1,171,12,71))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwIpMcstVlanRepCtrl_ObjectIdentity=ObjectIdentity
swIpMcstVlanRepCtrl=_SwIpMcstVlanRepCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,71,1))
class _SwIpMcstVlanRepState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SwIpMcstVlanRepState_Type.__name__=_D
_SwIpMcstVlanRepState_Object=MibScalar
swIpMcstVlanRepState=_SwIpMcstVlanRepState_Object((1,3,6,1,4,1,171,12,71,1,1),_SwIpMcstVlanRepState_Type())
swIpMcstVlanRepState.setMaxAccess(_E)
if mibBuilder.loadTexts:swIpMcstVlanRepState.setStatus(_A)
_SwIpMcstVlanRepInfo_ObjectIdentity=ObjectIdentity
swIpMcstVlanRepInfo=_SwIpMcstVlanRepInfo_ObjectIdentity((1,3,6,1,4,1,171,12,71,2))
_SwIpMcastVlanRepInfoTable_Object=MibTable
swIpMcastVlanRepInfoTable=_SwIpMcastVlanRepInfoTable_Object((1,3,6,1,4,1,171,12,71,2,1))
if mibBuilder.loadTexts:swIpMcastVlanRepInfoTable.setStatus(_A)
_SwIpMcastVlanRepInfoEntry_Object=MibTableRow
swIpMcastVlanRepInfoEntry=_SwIpMcastVlanRepInfoEntry_Object((1,3,6,1,4,1,171,12,71,2,1,1))
swIpMcastVlanRepInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:swIpMcastVlanRepInfoEntry.setStatus(_A)
_SwIpMcstVlanRepGroupAddrType_Type=InetAddressType
_SwIpMcstVlanRepGroupAddrType_Object=MibTableColumn
swIpMcstVlanRepGroupAddrType=_SwIpMcstVlanRepGroupAddrType_Object((1,3,6,1,4,1,171,12,71,2,1,1,1),_SwIpMcstVlanRepGroupAddrType_Type())
swIpMcstVlanRepGroupAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:swIpMcstVlanRepGroupAddrType.setStatus(_A)
_SwIpMcstVlanRepGroupAddr_Type=InetAddress
_SwIpMcstVlanRepGroupAddr_Object=MibTableColumn
swIpMcstVlanRepGroupAddr=_SwIpMcstVlanRepGroupAddr_Object((1,3,6,1,4,1,171,12,71,2,1,1,2),_SwIpMcstVlanRepGroupAddr_Type())
swIpMcstVlanRepGroupAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:swIpMcstVlanRepGroupAddr.setStatus(_A)
_SwIpMcstVlanRepSourceAddrType_Type=InetAddressType
_SwIpMcstVlanRepSourceAddrType_Object=MibTableColumn
swIpMcstVlanRepSourceAddrType=_SwIpMcstVlanRepSourceAddrType_Object((1,3,6,1,4,1,171,12,71,2,1,1,3),_SwIpMcstVlanRepSourceAddrType_Type())
swIpMcstVlanRepSourceAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:swIpMcstVlanRepSourceAddrType.setStatus(_A)
_SwIpMcstVlanRepSourceAddr_Type=InetAddress
_SwIpMcstVlanRepSourceAddr_Object=MibTableColumn
swIpMcstVlanRepSourceAddr=_SwIpMcstVlanRepSourceAddr_Object((1,3,6,1,4,1,171,12,71,2,1,1,4),_SwIpMcstVlanRepSourceAddr_Type())
swIpMcstVlanRepSourceAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:swIpMcstVlanRepSourceAddr.setStatus(_A)
class _SwIpMcstVlanRepStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_SwIpMcstVlanRepStatus_Type.__name__=_D
_SwIpMcstVlanRepStatus_Object=MibTableColumn
swIpMcstVlanRepStatus=_SwIpMcstVlanRepStatus_Object((1,3,6,1,4,1,171,12,71,2,1,1,5),_SwIpMcstVlanRepStatus_Type())
swIpMcstVlanRepStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swIpMcstVlanRepStatus.setStatus(_A)
_SwIpMcstVlanRepMgmt_ObjectIdentity=ObjectIdentity
swIpMcstVlanRepMgmt=_SwIpMcstVlanRepMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,71,3))
class _SwIpMcstVlanRepTTLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('decrease',1),('nodecrease',2)))
_SwIpMcstVlanRepTTLStatus_Type.__name__=_D
_SwIpMcstVlanRepTTLStatus_Object=MibScalar
swIpMcstVlanRepTTLStatus=_SwIpMcstVlanRepTTLStatus_Object((1,3,6,1,4,1,171,12,71,3,1),_SwIpMcstVlanRepTTLStatus_Type())
swIpMcstVlanRepTTLStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swIpMcstVlanRepTTLStatus.setStatus(_A)
class _SwIpMcstVlanRepSrcMacStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('replace',1),('noreplace',2)))
_SwIpMcstVlanRepSrcMacStatus_Type.__name__=_D
_SwIpMcstVlanRepSrcMacStatus_Object=MibScalar
swIpMcstVlanRepSrcMacStatus=_SwIpMcstVlanRepSrcMacStatus_Object((1,3,6,1,4,1,171,12,71,3,2),_SwIpMcstVlanRepSrcMacStatus_Type())
swIpMcstVlanRepSrcMacStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swIpMcstVlanRepSrcMacStatus.setStatus(_A)
_SwIpMcstVlanRepTable_Object=MibTable
swIpMcstVlanRepTable=_SwIpMcstVlanRepTable_Object((1,3,6,1,4,1,171,12,71,3,3))
if mibBuilder.loadTexts:swIpMcstVlanRepTable.setStatus(_A)
_SwIpMcstVlanRepEntry_Object=MibTableRow
swIpMcstVlanRepEntry=_SwIpMcstVlanRepEntry_Object((1,3,6,1,4,1,171,12,71,3,3,1))
swIpMcstVlanRepEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:swIpMcstVlanRepEntry.setStatus(_A)
_SwIpMcstVlanRepName_Type=DisplayString
_SwIpMcstVlanRepName_Object=MibTableColumn
swIpMcstVlanRepName=_SwIpMcstVlanRepName_Object((1,3,6,1,4,1,171,12,71,3,3,1,1),_SwIpMcstVlanRepName_Type())
swIpMcstVlanRepName.setMaxAccess(_C)
if mibBuilder.loadTexts:swIpMcstVlanRepName.setStatus(_A)
_SwIpMcstVlanRepSrcVID_Type=VlanId
_SwIpMcstVlanRepSrcVID_Object=MibTableColumn
swIpMcstVlanRepSrcVID=_SwIpMcstVlanRepSrcVID_Object((1,3,6,1,4,1,171,12,71,3,3,1,2),_SwIpMcstVlanRepSrcVID_Type())
swIpMcstVlanRepSrcVID.setMaxAccess(_E)
if mibBuilder.loadTexts:swIpMcstVlanRepSrcVID.setStatus(_A)
_SwIpMcstVlanRepRowStatus_Type=RowStatus
_SwIpMcstVlanRepRowStatus_Object=MibTableColumn
swIpMcstVlanRepRowStatus=_SwIpMcstVlanRepRowStatus_Object((1,3,6,1,4,1,171,12,71,3,3,1,3),_SwIpMcstVlanRepRowStatus_Type())
swIpMcstVlanRepRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swIpMcstVlanRepRowStatus.setStatus(_A)
_SwIpMcstVlanRepSrcTable_Object=MibTable
swIpMcstVlanRepSrcTable=_SwIpMcstVlanRepSrcTable_Object((1,3,6,1,4,1,171,12,71,3,4))
if mibBuilder.loadTexts:swIpMcstVlanRepSrcTable.setStatus(_A)
_SwIpMcstVlanRepSrcEntry_Object=MibTableRow
swIpMcstVlanRepSrcEntry=_SwIpMcstVlanRepSrcEntry_Object((1,3,6,1,4,1,171,12,71,3,4,1))
swIpMcstVlanRepSrcEntry.setIndexNames((0,_B,_F),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:swIpMcstVlanRepSrcEntry.setStatus(_A)
_SwIpMcstVlanRepGrpAddrType_Type=InetAddressType
_SwIpMcstVlanRepGrpAddrType_Object=MibTableColumn
swIpMcstVlanRepGrpAddrType=_SwIpMcstVlanRepGrpAddrType_Object((1,3,6,1,4,1,171,12,71,3,4,1,1),_SwIpMcstVlanRepGrpAddrType_Type())
swIpMcstVlanRepGrpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:swIpMcstVlanRepGrpAddrType.setStatus(_A)
_SwIpMcstVlanRepGrpAddrStart_Type=InetAddress
_SwIpMcstVlanRepGrpAddrStart_Object=MibTableColumn
swIpMcstVlanRepGrpAddrStart=_SwIpMcstVlanRepGrpAddrStart_Object((1,3,6,1,4,1,171,12,71,3,4,1,2),_SwIpMcstVlanRepGrpAddrStart_Type())
swIpMcstVlanRepGrpAddrStart.setMaxAccess(_C)
if mibBuilder.loadTexts:swIpMcstVlanRepGrpAddrStart.setStatus(_A)
_SwIpMcstVlanRepGrpAddrEnd_Type=InetAddress
_SwIpMcstVlanRepGrpAddrEnd_Object=MibTableColumn
swIpMcstVlanRepGrpAddrEnd=_SwIpMcstVlanRepGrpAddrEnd_Object((1,3,6,1,4,1,171,12,71,3,4,1,3),_SwIpMcstVlanRepGrpAddrEnd_Type())
swIpMcstVlanRepGrpAddrEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:swIpMcstVlanRepGrpAddrEnd.setStatus(_A)
_SwIpMcstVlanRepSrcAddrType_Type=InetAddressType
_SwIpMcstVlanRepSrcAddrType_Object=MibTableColumn
swIpMcstVlanRepSrcAddrType=_SwIpMcstVlanRepSrcAddrType_Object((1,3,6,1,4,1,171,12,71,3,4,1,4),_SwIpMcstVlanRepSrcAddrType_Type())
swIpMcstVlanRepSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:swIpMcstVlanRepSrcAddrType.setStatus(_A)
_SwIpMcstVlanRepSrcAddr_Type=InetAddress
_SwIpMcstVlanRepSrcAddr_Object=MibTableColumn
swIpMcstVlanRepSrcAddr=_SwIpMcstVlanRepSrcAddr_Object((1,3,6,1,4,1,171,12,71,3,4,1,5),_SwIpMcstVlanRepSrcAddr_Type())
swIpMcstVlanRepSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swIpMcstVlanRepSrcAddr.setStatus(_A)
_SwIpMcstVlanRepSrcRowStatus_Type=RowStatus
_SwIpMcstVlanRepSrcRowStatus_Object=MibTableColumn
swIpMcstVlanRepSrcRowStatus=_SwIpMcstVlanRepSrcRowStatus_Object((1,3,6,1,4,1,171,12,71,3,4,1,6),_SwIpMcstVlanRepSrcRowStatus_Type())
swIpMcstVlanRepSrcRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swIpMcstVlanRepSrcRowStatus.setStatus(_A)
_SwIpMcstVlanRepDstTable_Object=MibTable
swIpMcstVlanRepDstTable=_SwIpMcstVlanRepDstTable_Object((1,3,6,1,4,1,171,12,71,3,5))
if mibBuilder.loadTexts:swIpMcstVlanRepDstTable.setStatus(_A)
_SwIpMcstVlanRepDstEntry_Object=MibTableRow
swIpMcstVlanRepDstEntry=_SwIpMcstVlanRepDstEntry_Object((1,3,6,1,4,1,171,12,71,3,5,1))
swIpMcstVlanRepDstEntry.setIndexNames((0,_B,_F),(0,_B,_R))
if mibBuilder.loadTexts:swIpMcstVlanRepDstEntry.setStatus(_A)
_SwIpMcstVlanRepDstVID_Type=VlanId
_SwIpMcstVlanRepDstVID_Object=MibTableColumn
swIpMcstVlanRepDstVID=_SwIpMcstVlanRepDstVID_Object((1,3,6,1,4,1,171,12,71,3,5,1,1),_SwIpMcstVlanRepDstVID_Type())
swIpMcstVlanRepDstVID.setMaxAccess(_C)
if mibBuilder.loadTexts:swIpMcstVlanRepDstVID.setStatus(_A)
_SwIpMcstVlanRepDstPort_Type=PortList
_SwIpMcstVlanRepDstPort_Object=MibTableColumn
swIpMcstVlanRepDstPort=_SwIpMcstVlanRepDstPort_Object((1,3,6,1,4,1,171,12,71,3,5,1,2),_SwIpMcstVlanRepDstPort_Type())
swIpMcstVlanRepDstPort.setMaxAccess(_E)
if mibBuilder.loadTexts:swIpMcstVlanRepDstPort.setStatus(_A)
_SwIpMcstVlanRepDstRowStatus_Type=RowStatus
_SwIpMcstVlanRepDstRowStatus_Object=MibTableColumn
swIpMcstVlanRepDstRowStatus=_SwIpMcstVlanRepDstRowStatus_Object((1,3,6,1,4,1,171,12,71,3,5,1,3),_SwIpMcstVlanRepDstRowStatus_Type())
swIpMcstVlanRepDstRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swIpMcstVlanRepDstRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PortList':PortList,'VlanId':VlanId,'swIpMcstVlanRepMIB':swIpMcstVlanRepMIB,'swIpMcstVlanRepCtrl':swIpMcstVlanRepCtrl,'swIpMcstVlanRepState':swIpMcstVlanRepState,'swIpMcstVlanRepInfo':swIpMcstVlanRepInfo,'swIpMcastVlanRepInfoTable':swIpMcastVlanRepInfoTable,'swIpMcastVlanRepInfoEntry':swIpMcastVlanRepInfoEntry,_I:swIpMcstVlanRepGroupAddrType,_J:swIpMcstVlanRepGroupAddr,_K:swIpMcstVlanRepSourceAddrType,_L:swIpMcstVlanRepSourceAddr,'swIpMcstVlanRepStatus':swIpMcstVlanRepStatus,'swIpMcstVlanRepMgmt':swIpMcstVlanRepMgmt,'swIpMcstVlanRepTTLStatus':swIpMcstVlanRepTTLStatus,'swIpMcstVlanRepSrcMacStatus':swIpMcstVlanRepSrcMacStatus,'swIpMcstVlanRepTable':swIpMcstVlanRepTable,'swIpMcstVlanRepEntry':swIpMcstVlanRepEntry,_F:swIpMcstVlanRepName,'swIpMcstVlanRepSrcVID':swIpMcstVlanRepSrcVID,'swIpMcstVlanRepRowStatus':swIpMcstVlanRepRowStatus,'swIpMcstVlanRepSrcTable':swIpMcstVlanRepSrcTable,'swIpMcstVlanRepSrcEntry':swIpMcstVlanRepSrcEntry,_M:swIpMcstVlanRepGrpAddrType,_N:swIpMcstVlanRepGrpAddrStart,_O:swIpMcstVlanRepGrpAddrEnd,_P:swIpMcstVlanRepSrcAddrType,_Q:swIpMcstVlanRepSrcAddr,'swIpMcstVlanRepSrcRowStatus':swIpMcstVlanRepSrcRowStatus,'swIpMcstVlanRepDstTable':swIpMcstVlanRepDstTable,'swIpMcstVlanRepDstEntry':swIpMcstVlanRepDstEntry,_R:swIpMcstVlanRepDstVID,'swIpMcstVlanRepDstPort':swIpMcstVlanRepDstPort,'swIpMcstVlanRepDstRowStatus':swIpMcstVlanRepDstRowStatus})