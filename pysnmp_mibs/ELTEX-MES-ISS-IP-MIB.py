_K='eltMesIssIpAuthMgrIpPrefixLength'
_J='eltMesIssIpAuthMgrIpAddr'
_I='eltMesIssIpAuthMgrIpAddrType'
_H='TruthValue'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='not-accessible'
_C='ELTEX-MES-ISS-IP-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
eltMesIssIpMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,24))
if mibBuilder.loadTexts:eltMesIssIpMIB.setRevisions(('2021-01-12 00:00','2021-01-19 00:00'))
_EltMesIssIpObjects_ObjectIdentity=ObjectIdentity
eltMesIssIpObjects=_EltMesIssIpObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,24,1))
_EltMesIssIpMgmt_ObjectIdentity=ObjectIdentity
eltMesIssIpMgmt=_EltMesIssIpMgmt_ObjectIdentity((1,3,6,1,4,1,35265,1,139,24,1,1))
_EltMesIssIpMgmtInterfaceTable_Object=MibTable
eltMesIssIpMgmtInterfaceTable=_EltMesIssIpMgmtInterfaceTable_Object((1,3,6,1,4,1,35265,1,139,24,1,1,1))
if mibBuilder.loadTexts:eltMesIssIpMgmtInterfaceTable.setStatus(_A)
_EltMesIssIpMgmtInterfaceEntry_Object=MibTableRow
eltMesIssIpMgmtInterfaceEntry=_EltMesIssIpMgmtInterfaceEntry_Object((1,3,6,1,4,1,35265,1,139,24,1,1,1,1))
eltMesIssIpMgmtInterfaceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:eltMesIssIpMgmtInterfaceEntry.setStatus(_A)
_EltMesIssIpMgmtInterfaceOuterVlanId_Type=VlanId
_EltMesIssIpMgmtInterfaceOuterVlanId_Object=MibTableColumn
eltMesIssIpMgmtInterfaceOuterVlanId=_EltMesIssIpMgmtInterfaceOuterVlanId_Object((1,3,6,1,4,1,35265,1,139,24,1,1,1,1,1),_EltMesIssIpMgmtInterfaceOuterVlanId_Type())
eltMesIssIpMgmtInterfaceOuterVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpMgmtInterfaceOuterVlanId.setStatus(_A)
_EltMesIssIpAuthMgr_ObjectIdentity=ObjectIdentity
eltMesIssIpAuthMgr=_EltMesIssIpAuthMgr_ObjectIdentity((1,3,6,1,4,1,35265,1,139,24,1,2))
_EltMesIssIpAuthMgrTable_Object=MibTable
eltMesIssIpAuthMgrTable=_EltMesIssIpAuthMgrTable_Object((1,3,6,1,4,1,35265,1,139,24,1,2,1))
if mibBuilder.loadTexts:eltMesIssIpAuthMgrTable.setStatus(_A)
_EltMesIssIpAuthMgrEntry_Object=MibTableRow
eltMesIssIpAuthMgrEntry=_EltMesIssIpAuthMgrEntry_Object((1,3,6,1,4,1,35265,1,139,24,1,2,1,1))
eltMesIssIpAuthMgrEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:eltMesIssIpAuthMgrEntry.setStatus(_A)
_EltMesIssIpAuthMgrIpAddrType_Type=InetAddressType
_EltMesIssIpAuthMgrIpAddrType_Object=MibTableColumn
eltMesIssIpAuthMgrIpAddrType=_EltMesIssIpAuthMgrIpAddrType_Object((1,3,6,1,4,1,35265,1,139,24,1,2,1,1,1),_EltMesIssIpAuthMgrIpAddrType_Type())
eltMesIssIpAuthMgrIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssIpAuthMgrIpAddrType.setStatus(_A)
_EltMesIssIpAuthMgrIpAddr_Type=InetAddress
_EltMesIssIpAuthMgrIpAddr_Object=MibTableColumn
eltMesIssIpAuthMgrIpAddr=_EltMesIssIpAuthMgrIpAddr_Object((1,3,6,1,4,1,35265,1,139,24,1,2,1,1,2),_EltMesIssIpAuthMgrIpAddr_Type())
eltMesIssIpAuthMgrIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssIpAuthMgrIpAddr.setStatus(_A)
_EltMesIssIpAuthMgrIpPrefixLength_Type=InetAddressPrefixLength
_EltMesIssIpAuthMgrIpPrefixLength_Object=MibTableColumn
eltMesIssIpAuthMgrIpPrefixLength=_EltMesIssIpAuthMgrIpPrefixLength_Object((1,3,6,1,4,1,35265,1,139,24,1,2,1,1,3),_EltMesIssIpAuthMgrIpPrefixLength_Type())
eltMesIssIpAuthMgrIpPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssIpAuthMgrIpPrefixLength.setStatus(_A)
_EltMesIssIpAuthMgrPortList_Type=PortList
_EltMesIssIpAuthMgrPortList_Object=MibTableColumn
eltMesIssIpAuthMgrPortList=_EltMesIssIpAuthMgrPortList_Object((1,3,6,1,4,1,35265,1,139,24,1,2,1,1,4),_EltMesIssIpAuthMgrPortList_Type())
eltMesIssIpAuthMgrPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpAuthMgrPortList.setStatus(_A)
_EltMesIssIpAuthMgrVlanList_Type=OctetString
_EltMesIssIpAuthMgrVlanList_Object=MibTableColumn
eltMesIssIpAuthMgrVlanList=_EltMesIssIpAuthMgrVlanList_Object((1,3,6,1,4,1,35265,1,139,24,1,2,1,1,5),_EltMesIssIpAuthMgrVlanList_Type())
eltMesIssIpAuthMgrVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpAuthMgrVlanList.setStatus(_A)
class _EltMesIssIpAuthMgrOOBPort_Type(TruthValue):defaultValue=2
_EltMesIssIpAuthMgrOOBPort_Type.__name__=_H
_EltMesIssIpAuthMgrOOBPort_Object=MibTableColumn
eltMesIssIpAuthMgrOOBPort=_EltMesIssIpAuthMgrOOBPort_Object((1,3,6,1,4,1,35265,1,139,24,1,2,1,1,6),_EltMesIssIpAuthMgrOOBPort_Type())
eltMesIssIpAuthMgrOOBPort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpAuthMgrOOBPort.setStatus(_A)
class _EltMesIssIpAuthMgrAllowedServices_Type(Integer32):defaultValue=31
_EltMesIssIpAuthMgrAllowedServices_Type.__name__=_G
_EltMesIssIpAuthMgrAllowedServices_Object=MibTableColumn
eltMesIssIpAuthMgrAllowedServices=_EltMesIssIpAuthMgrAllowedServices_Object((1,3,6,1,4,1,35265,1,139,24,1,2,1,1,7),_EltMesIssIpAuthMgrAllowedServices_Type())
eltMesIssIpAuthMgrAllowedServices.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssIpAuthMgrAllowedServices.setStatus(_A)
_EltMesIssIpAuthMgrRowStatus_Type=RowStatus
_EltMesIssIpAuthMgrRowStatus_Object=MibTableColumn
eltMesIssIpAuthMgrRowStatus=_EltMesIssIpAuthMgrRowStatus_Object((1,3,6,1,4,1,35265,1,139,24,1,2,1,1,8),_EltMesIssIpAuthMgrRowStatus_Type())
eltMesIssIpAuthMgrRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:eltMesIssIpAuthMgrRowStatus.setStatus(_A)
_EltMesIssIpNotifications_ObjectIdentity=ObjectIdentity
eltMesIssIpNotifications=_EltMesIssIpNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,139,24,2))
mibBuilder.exportSymbols(_C,**{'eltMesIssIpMIB':eltMesIssIpMIB,'eltMesIssIpObjects':eltMesIssIpObjects,'eltMesIssIpMgmt':eltMesIssIpMgmt,'eltMesIssIpMgmtInterfaceTable':eltMesIssIpMgmtInterfaceTable,'eltMesIssIpMgmtInterfaceEntry':eltMesIssIpMgmtInterfaceEntry,'eltMesIssIpMgmtInterfaceOuterVlanId':eltMesIssIpMgmtInterfaceOuterVlanId,'eltMesIssIpAuthMgr':eltMesIssIpAuthMgr,'eltMesIssIpAuthMgrTable':eltMesIssIpAuthMgrTable,'eltMesIssIpAuthMgrEntry':eltMesIssIpAuthMgrEntry,_I:eltMesIssIpAuthMgrIpAddrType,_J:eltMesIssIpAuthMgrIpAddr,_K:eltMesIssIpAuthMgrIpPrefixLength,'eltMesIssIpAuthMgrPortList':eltMesIssIpAuthMgrPortList,'eltMesIssIpAuthMgrVlanList':eltMesIssIpAuthMgrVlanList,'eltMesIssIpAuthMgrOOBPort':eltMesIssIpAuthMgrOOBPort,'eltMesIssIpAuthMgrAllowedServices':eltMesIssIpAuthMgrAllowedServices,'eltMesIssIpAuthMgrRowStatus':eltMesIssIpAuthMgrRowStatus,'eltMesIssIpNotifications':eltMesIssIpNotifications})