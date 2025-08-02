_T='wwpLeosIpInterfaceOperationalGateway'
_S='wwpLeosIpInterfaceSubnet'
_R='wwpLeosIpInterfaceIpAddr'
_Q='wwpLeosIpInterfaceName'
_P='wwpLeosIpExtInterfaceEntry'
_O='wwpLeosIpAclEntryIpMask'
_N='wwpLeosIpAclEntryIpAddr'
_M='enabled'
_L='disabled'
_K='wwpLeosIpDataInterfaceIndex'
_J='wwpLeosIpInterfaceIndex'
_I='TruthValue'
_H='DisplayString'
_G='OctetString'
_F='read-write'
_E='Integer32'
_D='WWP-LEOS-IP-INTERFACE-MIB'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosIpInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,24))
if mibBuilder.loadTexts:wwpLeosIpInterfaceMIB.setRevisions(('2008-05-14 00:00','2003-05-02 00:00','2001-04-03 17:00'))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpLeosIpInterfaceMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosIpInterfaceMIBObjects=_WwpLeosIpInterfaceMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,24,1))
_WwpLeosIpInterface_ObjectIdentity=ObjectIdentity
wwpLeosIpInterface=_WwpLeosIpInterface_ObjectIdentity((1,3,6,1,4,1,6141,2,60,24,1,1))
_WwpLeosIpInterfaceTable_Object=MibTable
wwpLeosIpInterfaceTable=_WwpLeosIpInterfaceTable_Object((1,3,6,1,4,1,6141,2,60,24,1,1,1))
if mibBuilder.loadTexts:wwpLeosIpInterfaceTable.setStatus(_A)
_WwpLeosIpInterfaceEntry_Object=MibTableRow
wwpLeosIpInterfaceEntry=_WwpLeosIpInterfaceEntry_Object((1,3,6,1,4,1,6141,2,60,24,1,1,1,1))
wwpLeosIpInterfaceEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:wwpLeosIpInterfaceEntry.setStatus(_A)
class _WwpLeosIpInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WwpLeosIpInterfaceIndex_Type.__name__=_E
_WwpLeosIpInterfaceIndex_Object=MibTableColumn
wwpLeosIpInterfaceIndex=_WwpLeosIpInterfaceIndex_Object((1,3,6,1,4,1,6141,2,60,24,1,1,1,1,1),_WwpLeosIpInterfaceIndex_Type())
wwpLeosIpInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpInterfaceIndex.setStatus(_A)
class _WwpLeosIpInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpLeosIpInterfaceName_Type.__name__=_H
_WwpLeosIpInterfaceName_Object=MibTableColumn
wwpLeosIpInterfaceName=_WwpLeosIpInterfaceName_Object((1,3,6,1,4,1,6141,2,60,24,1,1,1,1,2),_WwpLeosIpInterfaceName_Type())
wwpLeosIpInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpInterfaceName.setStatus(_A)
_WwpLeosIpInterfaceIpAddr_Type=IpAddress
_WwpLeosIpInterfaceIpAddr_Object=MibTableColumn
wwpLeosIpInterfaceIpAddr=_WwpLeosIpInterfaceIpAddr_Object((1,3,6,1,4,1,6141,2,60,24,1,1,1,1,3),_WwpLeosIpInterfaceIpAddr_Type())
wwpLeosIpInterfaceIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosIpInterfaceIpAddr.setStatus(_A)
_WwpLeosIpInterfaceSubnet_Type=IpAddress
_WwpLeosIpInterfaceSubnet_Object=MibTableColumn
wwpLeosIpInterfaceSubnet=_WwpLeosIpInterfaceSubnet_Object((1,3,6,1,4,1,6141,2,60,24,1,1,1,1,4),_WwpLeosIpInterfaceSubnet_Type())
wwpLeosIpInterfaceSubnet.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosIpInterfaceSubnet.setStatus(_A)
class _WwpLeosIpInterfaceIfIndexXref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WwpLeosIpInterfaceIfIndexXref_Type.__name__=_E
_WwpLeosIpInterfaceIfIndexXref_Object=MibTableColumn
wwpLeosIpInterfaceIfIndexXref=_WwpLeosIpInterfaceIfIndexXref_Object((1,3,6,1,4,1,6141,2,60,24,1,1,1,1,5),_WwpLeosIpInterfaceIfIndexXref_Type())
wwpLeosIpInterfaceIfIndexXref.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpInterfaceIfIndexXref.setStatus(_A)
_WwpLeosIpExtInterfaceTable_Object=MibTable
wwpLeosIpExtInterfaceTable=_WwpLeosIpExtInterfaceTable_Object((1,3,6,1,4,1,6141,2,60,24,1,1,2))
if mibBuilder.loadTexts:wwpLeosIpExtInterfaceTable.setStatus(_A)
_WwpLeosIpExtInterfaceEntry_Object=MibTableRow
wwpLeosIpExtInterfaceEntry=_WwpLeosIpExtInterfaceEntry_Object((1,3,6,1,4,1,6141,2,60,24,1,1,2,1))
if mibBuilder.loadTexts:wwpLeosIpExtInterfaceEntry.setStatus(_A)
_WwpLeosIpInterfaceEnable_Type=TruthValue
_WwpLeosIpInterfaceEnable_Object=MibTableColumn
wwpLeosIpInterfaceEnable=_WwpLeosIpInterfaceEnable_Object((1,3,6,1,4,1,6141,2,60,24,1,1,2,1,1),_WwpLeosIpInterfaceEnable_Type())
wwpLeosIpInterfaceEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosIpInterfaceEnable.setStatus(_A)
_WwpLeosIpInterfaceVlanId_Type=VlanId
_WwpLeosIpInterfaceVlanId_Object=MibTableColumn
wwpLeosIpInterfaceVlanId=_WwpLeosIpInterfaceVlanId_Object((1,3,6,1,4,1,6141,2,60,24,1,1,2,1,2),_WwpLeosIpInterfaceVlanId_Type())
wwpLeosIpInterfaceVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosIpInterfaceVlanId.setStatus(_A)
class _WwpLeosIpInterfaceMgmtPktPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosIpInterfaceMgmtPktPriority_Type.__name__=_E
_WwpLeosIpInterfaceMgmtPktPriority_Object=MibTableColumn
wwpLeosIpInterfaceMgmtPktPriority=_WwpLeosIpInterfaceMgmtPktPriority_Object((1,3,6,1,4,1,6141,2,60,24,1,1,2,1,3),_WwpLeosIpInterfaceMgmtPktPriority_Type())
wwpLeosIpInterfaceMgmtPktPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosIpInterfaceMgmtPktPriority.setStatus(_A)
class _WwpLeosIpInterfaceAddrNotifEnabled_Type(TruthValue):defaultValue=1
_WwpLeosIpInterfaceAddrNotifEnabled_Type.__name__=_I
_WwpLeosIpInterfaceAddrNotifEnabled_Object=MibScalar
wwpLeosIpInterfaceAddrNotifEnabled=_WwpLeosIpInterfaceAddrNotifEnabled_Object((1,3,6,1,4,1,6141,2,60,24,1,1,3),_WwpLeosIpInterfaceAddrNotifEnabled_Type())
wwpLeosIpInterfaceAddrNotifEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosIpInterfaceAddrNotifEnabled.setStatus(_A)
_WwpLeosIpDataInterfaceTable_Object=MibTable
wwpLeosIpDataInterfaceTable=_WwpLeosIpDataInterfaceTable_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4))
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceTable.setStatus(_A)
_WwpLeosIpDataInterfaceEntry_Object=MibTableRow
wwpLeosIpDataInterfaceEntry=_WwpLeosIpDataInterfaceEntry_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4,1))
wwpLeosIpDataInterfaceEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceEntry.setStatus(_A)
class _WwpLeosIpDataInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WwpLeosIpDataInterfaceIndex_Type.__name__=_E
_WwpLeosIpDataInterfaceIndex_Object=MibTableColumn
wwpLeosIpDataInterfaceIndex=_WwpLeosIpDataInterfaceIndex_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4,1,1),_WwpLeosIpDataInterfaceIndex_Type())
wwpLeosIpDataInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceIndex.setStatus(_A)
class _WwpLeosIpDataInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_WwpLeosIpDataInterfaceName_Type.__name__=_H
_WwpLeosIpDataInterfaceName_Object=MibTableColumn
wwpLeosIpDataInterfaceName=_WwpLeosIpDataInterfaceName_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4,1,2),_WwpLeosIpDataInterfaceName_Type())
wwpLeosIpDataInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceName.setStatus(_A)
_WwpLeosIpDataInterfaceIpAddr_Type=IpAddress
_WwpLeosIpDataInterfaceIpAddr_Object=MibTableColumn
wwpLeosIpDataInterfaceIpAddr=_WwpLeosIpDataInterfaceIpAddr_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4,1,3),_WwpLeosIpDataInterfaceIpAddr_Type())
wwpLeosIpDataInterfaceIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceIpAddr.setStatus(_A)
_WwpLeosIpDataInterfaceMask_Type=IpAddress
_WwpLeosIpDataInterfaceMask_Object=MibTableColumn
wwpLeosIpDataInterfaceMask=_WwpLeosIpDataInterfaceMask_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4,1,4),_WwpLeosIpDataInterfaceMask_Type())
wwpLeosIpDataInterfaceMask.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceMask.setStatus(_A)
_WwpLeosIpDataInterfaceVlanId_Type=VlanId
_WwpLeosIpDataInterfaceVlanId_Object=MibTableColumn
wwpLeosIpDataInterfaceVlanId=_WwpLeosIpDataInterfaceVlanId_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4,1,5),_WwpLeosIpDataInterfaceVlanId_Type())
wwpLeosIpDataInterfaceVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceVlanId.setStatus(_A)
class _WwpLeosIpDataInterfaceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('broadcast',1),('pointToPoint',2),('loopBack',3)))
_WwpLeosIpDataInterfaceType_Type.__name__=_E
_WwpLeosIpDataInterfaceType_Object=MibTableColumn
wwpLeosIpDataInterfaceType=_WwpLeosIpDataInterfaceType_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4,1,6),_WwpLeosIpDataInterfaceType_Type())
wwpLeosIpDataInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceType.setStatus(_A)
_WwpLeosIpDataInterfaceIfIndex_Type=Integer32
_WwpLeosIpDataInterfaceIfIndex_Object=MibTableColumn
wwpLeosIpDataInterfaceIfIndex=_WwpLeosIpDataInterfaceIfIndex_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4,1,7),_WwpLeosIpDataInterfaceIfIndex_Type())
wwpLeosIpDataInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceIfIndex.setStatus(_A)
_WwpLeosIpDataInterfaceMac_Type=MacAddress
_WwpLeosIpDataInterfaceMac_Object=MibTableColumn
wwpLeosIpDataInterfaceMac=_WwpLeosIpDataInterfaceMac_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4,1,8),_WwpLeosIpDataInterfaceMac_Type())
wwpLeosIpDataInterfaceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceMac.setStatus(_A)
class _WwpLeosIpDataInterfaceIfMtu_Type(Integer32):defaultValue=1500
_WwpLeosIpDataInterfaceIfMtu_Type.__name__=_E
_WwpLeosIpDataInterfaceIfMtu_Object=MibTableColumn
wwpLeosIpDataInterfaceIfMtu=_WwpLeosIpDataInterfaceIfMtu_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4,1,9),_WwpLeosIpDataInterfaceIfMtu_Type())
wwpLeosIpDataInterfaceIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceIfMtu.setStatus(_A)
_WwpLeosIpDataInterfaceRowStatus_Type=RowStatus
_WwpLeosIpDataInterfaceRowStatus_Object=MibTableColumn
wwpLeosIpDataInterfaceRowStatus=_WwpLeosIpDataInterfaceRowStatus_Object((1,3,6,1,4,1,6141,2,60,24,1,1,4,1,10),_WwpLeosIpDataInterfaceRowStatus_Type())
wwpLeosIpDataInterfaceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpDataInterfaceRowStatus.setStatus(_A)
_WwpLeosIpInterfaceOperationalGateway_Type=IpAddress
_WwpLeosIpInterfaceOperationalGateway_Object=MibScalar
wwpLeosIpInterfaceOperationalGateway=_WwpLeosIpInterfaceOperationalGateway_Object((1,3,6,1,4,1,6141,2,60,24,1,1,5),_WwpLeosIpInterfaceOperationalGateway_Type())
wwpLeosIpInterfaceOperationalGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpInterfaceOperationalGateway.setStatus(_A)
_WwpLeosIpAclGlobal_ObjectIdentity=ObjectIdentity
wwpLeosIpAclGlobal=_WwpLeosIpAclGlobal_ObjectIdentity((1,3,6,1,4,1,6141,2,60,24,1,2))
class _WwpLeosIpAclState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WwpLeosIpAclState_Type.__name__=_E
_WwpLeosIpAclState_Object=MibScalar
wwpLeosIpAclState=_WwpLeosIpAclState_Object((1,3,6,1,4,1,6141,2,60,24,1,2,1),_WwpLeosIpAclState_Type())
wwpLeosIpAclState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosIpAclState.setStatus(_A)
_WwpLeosIpAclCacheHit_Type=Counter32
_WwpLeosIpAclCacheHit_Object=MibScalar
wwpLeosIpAclCacheHit=_WwpLeosIpAclCacheHit_Object((1,3,6,1,4,1,6141,2,60,24,1,2,2),_WwpLeosIpAclCacheHit_Type())
wwpLeosIpAclCacheHit.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpAclCacheHit.setStatus(_A)
_WwpLeosIpAclNoHit_Type=Counter32
_WwpLeosIpAclNoHit_Object=MibScalar
wwpLeosIpAclNoHit=_WwpLeosIpAclNoHit_Object((1,3,6,1,4,1,6141,2,60,24,1,2,3),_WwpLeosIpAclNoHit_Type())
wwpLeosIpAclNoHit.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpAclNoHit.setStatus(_A)
_WwpLeosIpAclBadPort_Type=Counter32
_WwpLeosIpAclBadPort_Object=MibScalar
wwpLeosIpAclBadPort=_WwpLeosIpAclBadPort_Object((1,3,6,1,4,1,6141,2,60,24,1,2,4),_WwpLeosIpAclBadPort_Type())
wwpLeosIpAclBadPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpAclBadPort.setStatus(_A)
_WwpLeosIpAclClearStats_Type=RowStatus
_WwpLeosIpAclClearStats_Object=MibScalar
wwpLeosIpAclClearStats=_WwpLeosIpAclClearStats_Object((1,3,6,1,4,1,6141,2,60,24,1,2,5),_WwpLeosIpAclClearStats_Type())
wwpLeosIpAclClearStats.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosIpAclClearStats.setStatus(_A)
_WwpLeosIpAclBadDscp_Type=Counter32
_WwpLeosIpAclBadDscp_Object=MibScalar
wwpLeosIpAclBadDscp=_WwpLeosIpAclBadDscp_Object((1,3,6,1,4,1,6141,2,60,24,1,2,6),_WwpLeosIpAclBadDscp_Type())
wwpLeosIpAclBadDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpAclBadDscp.setStatus(_A)
class _WwpLeosIpAclOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WwpLeosIpAclOperState_Type.__name__=_E
_WwpLeosIpAclOperState_Object=MibScalar
wwpLeosIpAclOperState=_WwpLeosIpAclOperState_Object((1,3,6,1,4,1,6141,2,60,24,1,2,7),_WwpLeosIpAclOperState_Type())
wwpLeosIpAclOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpAclOperState.setStatus(_A)
_WwpLeosIpAclInUseEntries_Type=Counter32
_WwpLeosIpAclInUseEntries_Object=MibScalar
wwpLeosIpAclInUseEntries=_WwpLeosIpAclInUseEntries_Object((1,3,6,1,4,1,6141,2,60,24,1,2,8),_WwpLeosIpAclInUseEntries_Type())
wwpLeosIpAclInUseEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpAclInUseEntries.setStatus(_A)
_WwpLeosIpAclMaxEntries_Type=Counter32
_WwpLeosIpAclMaxEntries_Object=MibScalar
wwpLeosIpAclMaxEntries=_WwpLeosIpAclMaxEntries_Object((1,3,6,1,4,1,6141,2,60,24,1,2,9),_WwpLeosIpAclMaxEntries_Type())
wwpLeosIpAclMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpAclMaxEntries.setStatus(_A)
_WwpLeosIpAclRules_ObjectIdentity=ObjectIdentity
wwpLeosIpAclRules=_WwpLeosIpAclRules_ObjectIdentity((1,3,6,1,4,1,6141,2,60,24,1,3))
_WwpLeosIpAclTable_Object=MibTable
wwpLeosIpAclTable=_WwpLeosIpAclTable_Object((1,3,6,1,4,1,6141,2,60,24,1,3,1))
if mibBuilder.loadTexts:wwpLeosIpAclTable.setStatus(_A)
_WwpLeosIpAclEntry_Object=MibTableRow
wwpLeosIpAclEntry=_WwpLeosIpAclEntry_Object((1,3,6,1,4,1,6141,2,60,24,1,3,1,1))
wwpLeosIpAclEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:wwpLeosIpAclEntry.setStatus(_A)
_WwpLeosIpAclEntryIpAddr_Type=IpAddress
_WwpLeosIpAclEntryIpAddr_Object=MibTableColumn
wwpLeosIpAclEntryIpAddr=_WwpLeosIpAclEntryIpAddr_Object((1,3,6,1,4,1,6141,2,60,24,1,3,1,1,1),_WwpLeosIpAclEntryIpAddr_Type())
wwpLeosIpAclEntryIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpAclEntryIpAddr.setStatus(_A)
_WwpLeosIpAclEntryIpMask_Type=IpAddress
_WwpLeosIpAclEntryIpMask_Object=MibTableColumn
wwpLeosIpAclEntryIpMask=_WwpLeosIpAclEntryIpMask_Object((1,3,6,1,4,1,6141,2,60,24,1,3,1,1,2),_WwpLeosIpAclEntryIpMask_Type())
wwpLeosIpAclEntryIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpAclEntryIpMask.setStatus(_A)
_WwpLeosIpAclEntryPortMask_Type=Unsigned32
_WwpLeosIpAclEntryPortMask_Object=MibTableColumn
wwpLeosIpAclEntryPortMask=_WwpLeosIpAclEntryPortMask_Object((1,3,6,1,4,1,6141,2,60,24,1,3,1,1,3),_WwpLeosIpAclEntryPortMask_Type())
wwpLeosIpAclEntryPortMask.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpAclEntryPortMask.setStatus('deprecated')
_WwpLeosIpAclEntryHits_Type=Counter32
_WwpLeosIpAclEntryHits_Object=MibTableColumn
wwpLeosIpAclEntryHits=_WwpLeosIpAclEntryHits_Object((1,3,6,1,4,1,6141,2,60,24,1,3,1,1,4),_WwpLeosIpAclEntryHits_Type())
wwpLeosIpAclEntryHits.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpAclEntryHits.setStatus(_A)
_WwpLeosIpAclEntryBadPort_Type=Counter32
_WwpLeosIpAclEntryBadPort_Object=MibTableColumn
wwpLeosIpAclEntryBadPort=_WwpLeosIpAclEntryBadPort_Object((1,3,6,1,4,1,6141,2,60,24,1,3,1,1,5),_WwpLeosIpAclEntryBadPort_Type())
wwpLeosIpAclEntryBadPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpAclEntryBadPort.setStatus(_A)
_WwpLeosIpAclEntryStatus_Type=RowStatus
_WwpLeosIpAclEntryStatus_Object=MibTableColumn
wwpLeosIpAclEntryStatus=_WwpLeosIpAclEntryStatus_Object((1,3,6,1,4,1,6141,2,60,24,1,3,1,1,6),_WwpLeosIpAclEntryStatus_Type())
wwpLeosIpAclEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpAclEntryStatus.setStatus(_A)
class _WwpLeosIpAclEntryDscpMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_WwpLeosIpAclEntryDscpMask_Type.__name__=_G
_WwpLeosIpAclEntryDscpMask_Object=MibTableColumn
wwpLeosIpAclEntryDscpMask=_WwpLeosIpAclEntryDscpMask_Object((1,3,6,1,4,1,6141,2,60,24,1,3,1,1,7),_WwpLeosIpAclEntryDscpMask_Type())
wwpLeosIpAclEntryDscpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpAclEntryDscpMask.setStatus(_A)
_WwpLeosIpAclEntryBadDscp_Type=Counter32
_WwpLeosIpAclEntryBadDscp_Object=MibTableColumn
wwpLeosIpAclEntryBadDscp=_WwpLeosIpAclEntryBadDscp_Object((1,3,6,1,4,1,6141,2,60,24,1,3,1,1,8),_WwpLeosIpAclEntryBadDscp_Type())
wwpLeosIpAclEntryBadDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosIpAclEntryBadDscp.setStatus(_A)
class _WwpLeosIpAclEntryPortBitMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_WwpLeosIpAclEntryPortBitMask_Type.__name__=_G
_WwpLeosIpAclEntryPortBitMask_Object=MibTableColumn
wwpLeosIpAclEntryPortBitMask=_WwpLeosIpAclEntryPortBitMask_Object((1,3,6,1,4,1,6141,2,60,24,1,3,1,1,9),_WwpLeosIpAclEntryPortBitMask_Type())
wwpLeosIpAclEntryPortBitMask.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosIpAclEntryPortBitMask.setStatus(_A)
_WwpLeosIpInterfaceMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosIpInterfaceMIBNotificationPrefix=_WwpLeosIpInterfaceMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,24,2))
_WwpLeosIpInterfaceMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosIpInterfaceMIBNotifications=_WwpLeosIpInterfaceMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,24,2,0))
_WwpLeosIpInterfaceMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosIpInterfaceMIBConformance=_WwpLeosIpInterfaceMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,24,3))
_WwpLeosIpInterfaceMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosIpInterfaceMIBCompliances=_WwpLeosIpInterfaceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,24,3,1))
_WwpLeosIpInterfaceMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosIpInterfaceMIBGroups=_WwpLeosIpInterfaceMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,24,3,2))
wwpLeosIpInterfaceEntry.registerAugmentions((_D,_P))
wwpLeosIpExtInterfaceEntry.setIndexNames(*wwpLeosIpInterfaceEntry.getIndexNames())
wwpLeosIpInterfaceAddrChgNotification=NotificationType((1,3,6,1,4,1,6141,2,60,24,2,0,1))
wwpLeosIpInterfaceAddrChgNotification.setObjects(*((_D,_Q),(_D,_R),(_D,_S)))
if mibBuilder.loadTexts:wwpLeosIpInterfaceAddrChgNotification.setStatus(_A)
wwpLeosIpInterfaceOperationalGatewayChgNotification=NotificationType((1,3,6,1,4,1,6141,2,60,24,2,0,2))
wwpLeosIpInterfaceOperationalGatewayChgNotification.setObjects((_D,_T))
if mibBuilder.loadTexts:wwpLeosIpInterfaceOperationalGatewayChgNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'VlanId':VlanId,'wwpLeosIpInterfaceMIB':wwpLeosIpInterfaceMIB,'wwpLeosIpInterfaceMIBObjects':wwpLeosIpInterfaceMIBObjects,'wwpLeosIpInterface':wwpLeosIpInterface,'wwpLeosIpInterfaceTable':wwpLeosIpInterfaceTable,'wwpLeosIpInterfaceEntry':wwpLeosIpInterfaceEntry,_J:wwpLeosIpInterfaceIndex,_Q:wwpLeosIpInterfaceName,_R:wwpLeosIpInterfaceIpAddr,_S:wwpLeosIpInterfaceSubnet,'wwpLeosIpInterfaceIfIndexXref':wwpLeosIpInterfaceIfIndexXref,'wwpLeosIpExtInterfaceTable':wwpLeosIpExtInterfaceTable,_P:wwpLeosIpExtInterfaceEntry,'wwpLeosIpInterfaceEnable':wwpLeosIpInterfaceEnable,'wwpLeosIpInterfaceVlanId':wwpLeosIpInterfaceVlanId,'wwpLeosIpInterfaceMgmtPktPriority':wwpLeosIpInterfaceMgmtPktPriority,'wwpLeosIpInterfaceAddrNotifEnabled':wwpLeosIpInterfaceAddrNotifEnabled,'wwpLeosIpDataInterfaceTable':wwpLeosIpDataInterfaceTable,'wwpLeosIpDataInterfaceEntry':wwpLeosIpDataInterfaceEntry,_K:wwpLeosIpDataInterfaceIndex,'wwpLeosIpDataInterfaceName':wwpLeosIpDataInterfaceName,'wwpLeosIpDataInterfaceIpAddr':wwpLeosIpDataInterfaceIpAddr,'wwpLeosIpDataInterfaceMask':wwpLeosIpDataInterfaceMask,'wwpLeosIpDataInterfaceVlanId':wwpLeosIpDataInterfaceVlanId,'wwpLeosIpDataInterfaceType':wwpLeosIpDataInterfaceType,'wwpLeosIpDataInterfaceIfIndex':wwpLeosIpDataInterfaceIfIndex,'wwpLeosIpDataInterfaceMac':wwpLeosIpDataInterfaceMac,'wwpLeosIpDataInterfaceIfMtu':wwpLeosIpDataInterfaceIfMtu,'wwpLeosIpDataInterfaceRowStatus':wwpLeosIpDataInterfaceRowStatus,_T:wwpLeosIpInterfaceOperationalGateway,'wwpLeosIpAclGlobal':wwpLeosIpAclGlobal,'wwpLeosIpAclState':wwpLeosIpAclState,'wwpLeosIpAclCacheHit':wwpLeosIpAclCacheHit,'wwpLeosIpAclNoHit':wwpLeosIpAclNoHit,'wwpLeosIpAclBadPort':wwpLeosIpAclBadPort,'wwpLeosIpAclClearStats':wwpLeosIpAclClearStats,'wwpLeosIpAclBadDscp':wwpLeosIpAclBadDscp,'wwpLeosIpAclOperState':wwpLeosIpAclOperState,'wwpLeosIpAclInUseEntries':wwpLeosIpAclInUseEntries,'wwpLeosIpAclMaxEntries':wwpLeosIpAclMaxEntries,'wwpLeosIpAclRules':wwpLeosIpAclRules,'wwpLeosIpAclTable':wwpLeosIpAclTable,'wwpLeosIpAclEntry':wwpLeosIpAclEntry,_N:wwpLeosIpAclEntryIpAddr,_O:wwpLeosIpAclEntryIpMask,'wwpLeosIpAclEntryPortMask':wwpLeosIpAclEntryPortMask,'wwpLeosIpAclEntryHits':wwpLeosIpAclEntryHits,'wwpLeosIpAclEntryBadPort':wwpLeosIpAclEntryBadPort,'wwpLeosIpAclEntryStatus':wwpLeosIpAclEntryStatus,'wwpLeosIpAclEntryDscpMask':wwpLeosIpAclEntryDscpMask,'wwpLeosIpAclEntryBadDscp':wwpLeosIpAclEntryBadDscp,'wwpLeosIpAclEntryPortBitMask':wwpLeosIpAclEntryPortBitMask,'wwpLeosIpInterfaceMIBNotificationPrefix':wwpLeosIpInterfaceMIBNotificationPrefix,'wwpLeosIpInterfaceMIBNotifications':wwpLeosIpInterfaceMIBNotifications,'wwpLeosIpInterfaceAddrChgNotification':wwpLeosIpInterfaceAddrChgNotification,'wwpLeosIpInterfaceOperationalGatewayChgNotification':wwpLeosIpInterfaceOperationalGatewayChgNotification,'wwpLeosIpInterfaceMIBConformance':wwpLeosIpInterfaceMIBConformance,'wwpLeosIpInterfaceMIBCompliances':wwpLeosIpInterfaceMIBCompliances,'wwpLeosIpInterfaceMIBGroups':wwpLeosIpInterfaceMIBGroups})