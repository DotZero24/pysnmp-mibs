_V='ntcIpConfGrpV1Standard'
_U='ntcIpAlmGwUnreachable'
_T='ntcDataGateway'
_S='ntcDataInterfaceFysIpAddress'
_R='ntcDataInterfaceState'
_Q='ntcDataInterfaceIpAddress'
_P='ntcMgmtGateway'
_O='ntcIpMgmtInterfaceVirtualIpAddr'
_N='ntcIpMgmtInterfaceState'
_M='ntcIpMgmtInterfaceIpAddress'
_L='ntcDataInterfaceName'
_K='00000000'
_J='not-accessible'
_I='ntcIpMgmtInterfaceName'
_H='read-only'
_G='IpAddress'
_F='0.0.0.0/24'
_E='Integer32'
_D='NtcNetworkAddress'
_C='read-write'
_B='NEWTEC-IP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcNetworkAddress=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_G,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcIp=ModuleIdentity((1,3,6,1,4,1,5835,5,2,400))
if mibBuilder.loadTexts:ntcIp.setRevisions(('2017-07-10 12:00','2014-02-03 12:00','2013-01-08 12:00','2012-06-28 12:00'))
_NtcIpObjects_ObjectIdentity=ObjectIdentity
ntcIpObjects=_NtcIpObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,400,1))
if mibBuilder.loadTexts:ntcIpObjects.setStatus(_A)
_NtcIpMgmtInterfaceTable_Object=MibTable
ntcIpMgmtInterfaceTable=_NtcIpMgmtInterfaceTable_Object((1,3,6,1,4,1,5835,5,2,400,1,1))
if mibBuilder.loadTexts:ntcIpMgmtInterfaceTable.setStatus(_A)
_NtcIpMgmtInterfaceEntry_Object=MibTableRow
ntcIpMgmtInterfaceEntry=_NtcIpMgmtInterfaceEntry_Object((1,3,6,1,4,1,5835,5,2,400,1,1,1))
ntcIpMgmtInterfaceEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ntcIpMgmtInterfaceEntry.setStatus(_A)
class _NtcIpMgmtInterfaceName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('mgmt1',0),('mgmt2',1),('mgmtfp',2),('mgmt',3)))
_NtcIpMgmtInterfaceName_Type.__name__=_E
_NtcIpMgmtInterfaceName_Object=MibTableColumn
ntcIpMgmtInterfaceName=_NtcIpMgmtInterfaceName_Object((1,3,6,1,4,1,5835,5,2,400,1,1,1,1),_NtcIpMgmtInterfaceName_Type())
ntcIpMgmtInterfaceName.setMaxAccess(_J)
if mibBuilder.loadTexts:ntcIpMgmtInterfaceName.setStatus(_A)
class _NtcIpMgmtInterfaceIpAddress_Type(NtcNetworkAddress):defaultValue=OctetString(_F)
_NtcIpMgmtInterfaceIpAddress_Type.__name__=_D
_NtcIpMgmtInterfaceIpAddress_Object=MibTableColumn
ntcIpMgmtInterfaceIpAddress=_NtcIpMgmtInterfaceIpAddress_Object((1,3,6,1,4,1,5835,5,2,400,1,1,1,2),_NtcIpMgmtInterfaceIpAddress_Type())
ntcIpMgmtInterfaceIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIpMgmtInterfaceIpAddress.setStatus(_A)
class _NtcIpMgmtInterfaceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_NtcIpMgmtInterfaceState_Type.__name__=_E
_NtcIpMgmtInterfaceState_Object=MibTableColumn
ntcIpMgmtInterfaceState=_NtcIpMgmtInterfaceState_Object((1,3,6,1,4,1,5835,5,2,400,1,1,1,3),_NtcIpMgmtInterfaceState_Type())
ntcIpMgmtInterfaceState.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcIpMgmtInterfaceState.setStatus(_A)
class _NtcIpMgmtInterfaceVirtualIpAddr_Type(NtcNetworkAddress):defaultValue=OctetString(_F)
_NtcIpMgmtInterfaceVirtualIpAddr_Type.__name__=_D
_NtcIpMgmtInterfaceVirtualIpAddr_Object=MibTableColumn
ntcIpMgmtInterfaceVirtualIpAddr=_NtcIpMgmtInterfaceVirtualIpAddr_Object((1,3,6,1,4,1,5835,5,2,400,1,1,1,4),_NtcIpMgmtInterfaceVirtualIpAddr_Type())
ntcIpMgmtInterfaceVirtualIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIpMgmtInterfaceVirtualIpAddr.setStatus(_A)
class _NtcMgmtGateway_Type(IpAddress):defaultHexValue=_K
_NtcMgmtGateway_Type.__name__=_G
_NtcMgmtGateway_Object=MibScalar
ntcMgmtGateway=_NtcMgmtGateway_Object((1,3,6,1,4,1,5835,5,2,400,1,2),_NtcMgmtGateway_Type())
ntcMgmtGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMgmtGateway.setStatus(_A)
_NtcDataInterfaceTable_Object=MibTable
ntcDataInterfaceTable=_NtcDataInterfaceTable_Object((1,3,6,1,4,1,5835,5,2,400,1,3))
if mibBuilder.loadTexts:ntcDataInterfaceTable.setStatus(_A)
_NtcDataInterfaceEntry_Object=MibTableRow
ntcDataInterfaceEntry=_NtcDataInterfaceEntry_Object((1,3,6,1,4,1,5835,5,2,400,1,3,1))
ntcDataInterfaceEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:ntcDataInterfaceEntry.setStatus(_A)
class _NtcDataInterfaceName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('data1',0),('data2',1),('data',2),('sat1',3),('sat2',4),('sat',5)))
_NtcDataInterfaceName_Type.__name__=_E
_NtcDataInterfaceName_Object=MibTableColumn
ntcDataInterfaceName=_NtcDataInterfaceName_Object((1,3,6,1,4,1,5835,5,2,400,1,3,1,1),_NtcDataInterfaceName_Type())
ntcDataInterfaceName.setMaxAccess(_J)
if mibBuilder.loadTexts:ntcDataInterfaceName.setStatus(_A)
class _NtcDataInterfaceIpAddress_Type(NtcNetworkAddress):defaultValue=OctetString(_F)
_NtcDataInterfaceIpAddress_Type.__name__=_D
_NtcDataInterfaceIpAddress_Object=MibTableColumn
ntcDataInterfaceIpAddress=_NtcDataInterfaceIpAddress_Object((1,3,6,1,4,1,5835,5,2,400,1,3,1,2),_NtcDataInterfaceIpAddress_Type())
ntcDataInterfaceIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDataInterfaceIpAddress.setStatus(_A)
class _NtcDataInterfaceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_NtcDataInterfaceState_Type.__name__=_E
_NtcDataInterfaceState_Object=MibTableColumn
ntcDataInterfaceState=_NtcDataInterfaceState_Object((1,3,6,1,4,1,5835,5,2,400,1,3,1,3),_NtcDataInterfaceState_Type())
ntcDataInterfaceState.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcDataInterfaceState.setStatus(_A)
class _NtcDataInterfaceFysIpAddress_Type(NtcNetworkAddress):defaultValue=OctetString(_F)
_NtcDataInterfaceFysIpAddress_Type.__name__=_D
_NtcDataInterfaceFysIpAddress_Object=MibTableColumn
ntcDataInterfaceFysIpAddress=_NtcDataInterfaceFysIpAddress_Object((1,3,6,1,4,1,5835,5,2,400,1,3,1,4),_NtcDataInterfaceFysIpAddress_Type())
ntcDataInterfaceFysIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDataInterfaceFysIpAddress.setStatus(_A)
class _NtcDataGateway_Type(IpAddress):defaultHexValue=_K
_NtcDataGateway_Type.__name__=_G
_NtcDataGateway_Object=MibScalar
ntcDataGateway=_NtcDataGateway_Object((1,3,6,1,4,1,5835,5,2,400,1,4),_NtcDataGateway_Type())
ntcDataGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDataGateway.setStatus(_A)
_NtcIpAlarm_ObjectIdentity=ObjectIdentity
ntcIpAlarm=_NtcIpAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,400,1,5))
if mibBuilder.loadTexts:ntcIpAlarm.setStatus(_A)
_NtcIpAlmGwUnreachable_Type=NtcAlarmState
_NtcIpAlmGwUnreachable_Object=MibScalar
ntcIpAlmGwUnreachable=_NtcIpAlmGwUnreachable_Object((1,3,6,1,4,1,5835,5,2,400,1,5,1),_NtcIpAlmGwUnreachable_Type())
ntcIpAlmGwUnreachable.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcIpAlmGwUnreachable.setStatus(_A)
_NtcIpConformance_ObjectIdentity=ObjectIdentity
ntcIpConformance=_NtcIpConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,400,2))
if mibBuilder.loadTexts:ntcIpConformance.setStatus(_A)
_NtcIpConfCompliance_ObjectIdentity=ObjectIdentity
ntcIpConfCompliance=_NtcIpConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,400,2,1))
if mibBuilder.loadTexts:ntcIpConfCompliance.setStatus(_A)
_NtcIpConfGroup_ObjectIdentity=ObjectIdentity
ntcIpConfGroup=_NtcIpConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,400,2,2))
if mibBuilder.loadTexts:ntcIpConfGroup.setStatus(_A)
ntcIpConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,400,2,2,1))
ntcIpConfGrpV1Standard.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ntcIpConfGrpV1Standard.setStatus(_A)
ntcIpConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,400,2,1,1))
ntcIpConfCompV1Standard.setObjects((_B,_V))
if mibBuilder.loadTexts:ntcIpConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcIp':ntcIp,'ntcIpObjects':ntcIpObjects,'ntcIpMgmtInterfaceTable':ntcIpMgmtInterfaceTable,'ntcIpMgmtInterfaceEntry':ntcIpMgmtInterfaceEntry,_I:ntcIpMgmtInterfaceName,_M:ntcIpMgmtInterfaceIpAddress,_N:ntcIpMgmtInterfaceState,_O:ntcIpMgmtInterfaceVirtualIpAddr,_P:ntcMgmtGateway,'ntcDataInterfaceTable':ntcDataInterfaceTable,'ntcDataInterfaceEntry':ntcDataInterfaceEntry,_L:ntcDataInterfaceName,_Q:ntcDataInterfaceIpAddress,_R:ntcDataInterfaceState,_S:ntcDataInterfaceFysIpAddress,_T:ntcDataGateway,'ntcIpAlarm':ntcIpAlarm,_U:ntcIpAlmGwUnreachable,'ntcIpConformance':ntcIpConformance,'ntcIpConfCompliance':ntcIpConfCompliance,'ntcIpConfCompV1Standard':ntcIpConfCompV1Standard,'ntcIpConfGroup':ntcIpConfGroup,_V:ntcIpConfGrpV1Standard})