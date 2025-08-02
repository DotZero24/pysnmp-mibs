_c='cIpNetworkDiscoveryCfgGroup'
_b='cIpNetworkDiscoveryInfoGroup'
_a='cIpNetworkDiscoveryCmdStatus'
_Z='cIpNetworkDiscoveryCommand'
_Y='cIpNetworkGigEInetAddrToDiscover'
_X='cIpNetworkInetAddrTypeToDiscover'
_W='cIpNetworkGigEIfIndexToDiscover'
_V='cIpNetworkDiscoverySpinLock'
_U='cIpNetworkDiscoveryPort'
_T='cIpNetworkDiscoveryType'
_S='cIpNetworkDiscoveryTypeSpinLock'
_R='cIpNetworkDiscoveryDelay'
_Q='cIpNetworkAutomaticDiscovery'
_P='cIpNetworkSwitchWWN'
_O='cIpNetworkGigEPortInetAddrType'
_N='cIpNetworkGigEPortIfIndex'
_M='cIpNetworkGigEPortSwitchWWN'
_L='TruthValue'
_K='InetAddressType'
_J='InetAddress'
_I='FcNameId'
_H='cIpNetworkGigEPortInetAddr'
_G='cIpNetworkIndex'
_F='not-accessible'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='CISCO-IP-NW-DISCOVERY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcNameId,=mibBuilder.importSymbols('CISCO-ST-TC',_I)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,_K,'InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TestAndIncr,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TestAndIncr',_L)
ciscoIpNetworkDiscoveryMIB=ModuleIdentity((1,3,6,1,4,1,9,9,434))
if mibBuilder.loadTexts:ciscoIpNetworkDiscoveryMIB.setRevisions(('2006-10-03 00:00','2005-08-09 00:00'))
_CIpNetworkDiscoveryMIBNotifs_ObjectIdentity=ObjectIdentity
cIpNetworkDiscoveryMIBNotifs=_CIpNetworkDiscoveryMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,434,0))
_CIpNetworkDiscoveryMIBObjs_ObjectIdentity=ObjectIdentity
cIpNetworkDiscoveryMIBObjs=_CIpNetworkDiscoveryMIBObjs_ObjectIdentity((1,3,6,1,4,1,9,9,434,1))
_CIpNetworkDiscoveryConfig_ObjectIdentity=ObjectIdentity
cIpNetworkDiscoveryConfig=_CIpNetworkDiscoveryConfig_ObjectIdentity((1,3,6,1,4,1,9,9,434,1,1))
class _CIpNetworkAutomaticDiscovery_Type(TruthValue):defaultValue=2
_CIpNetworkAutomaticDiscovery_Type.__name__=_L
_CIpNetworkAutomaticDiscovery_Object=MibScalar
cIpNetworkAutomaticDiscovery=_CIpNetworkAutomaticDiscovery_Object((1,3,6,1,4,1,9,9,434,1,1,1),_CIpNetworkAutomaticDiscovery_Type())
cIpNetworkAutomaticDiscovery.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpNetworkAutomaticDiscovery.setStatus(_A)
class _CIpNetworkDiscoveryDelay_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5184000))
_CIpNetworkDiscoveryDelay_Type.__name__=_D
_CIpNetworkDiscoveryDelay_Object=MibScalar
cIpNetworkDiscoveryDelay=_CIpNetworkDiscoveryDelay_Object((1,3,6,1,4,1,9,9,434,1,1,2),_CIpNetworkDiscoveryDelay_Type())
cIpNetworkDiscoveryDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:cIpNetworkDiscoveryDelay.setStatus(_A)
if mibBuilder.loadTexts:cIpNetworkDiscoveryDelay.setUnits('seconds')
_CIpNetworkDiscoveryTypeSpinLock_Type=TestAndIncr
_CIpNetworkDiscoveryTypeSpinLock_Object=MibScalar
cIpNetworkDiscoveryTypeSpinLock=_CIpNetworkDiscoveryTypeSpinLock_Object((1,3,6,1,4,1,9,9,434,1,1,3),_CIpNetworkDiscoveryTypeSpinLock_Type())
cIpNetworkDiscoveryTypeSpinLock.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpNetworkDiscoveryTypeSpinLock.setStatus(_A)
class _CIpNetworkDiscoveryType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('icmp',1),('tcp',2),('udp',3)))
_CIpNetworkDiscoveryType_Type.__name__=_D
_CIpNetworkDiscoveryType_Object=MibScalar
cIpNetworkDiscoveryType=_CIpNetworkDiscoveryType_Object((1,3,6,1,4,1,9,9,434,1,1,4),_CIpNetworkDiscoveryType_Type())
cIpNetworkDiscoveryType.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpNetworkDiscoveryType.setStatus(_A)
_CIpNetworkDiscoveryPort_Type=InetPortNumber
_CIpNetworkDiscoveryPort_Object=MibScalar
cIpNetworkDiscoveryPort=_CIpNetworkDiscoveryPort_Object((1,3,6,1,4,1,9,9,434,1,1,5),_CIpNetworkDiscoveryPort_Type())
cIpNetworkDiscoveryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpNetworkDiscoveryPort.setStatus(_A)
_CIpNetworkDiscoverySpinLock_Type=TestAndIncr
_CIpNetworkDiscoverySpinLock_Object=MibScalar
cIpNetworkDiscoverySpinLock=_CIpNetworkDiscoverySpinLock_Object((1,3,6,1,4,1,9,9,434,1,1,6),_CIpNetworkDiscoverySpinLock_Type())
cIpNetworkDiscoverySpinLock.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpNetworkDiscoverySpinLock.setStatus(_A)
_CIpNetworkGigEIfIndexToDiscover_Type=InterfaceIndexOrZero
_CIpNetworkGigEIfIndexToDiscover_Object=MibScalar
cIpNetworkGigEIfIndexToDiscover=_CIpNetworkGigEIfIndexToDiscover_Object((1,3,6,1,4,1,9,9,434,1,1,7),_CIpNetworkGigEIfIndexToDiscover_Type())
cIpNetworkGigEIfIndexToDiscover.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpNetworkGigEIfIndexToDiscover.setStatus(_A)
class _CIpNetworkInetAddrTypeToDiscover_Type(InetAddressType):defaultValue=1
_CIpNetworkInetAddrTypeToDiscover_Type.__name__=_K
_CIpNetworkInetAddrTypeToDiscover_Object=MibScalar
cIpNetworkInetAddrTypeToDiscover=_CIpNetworkInetAddrTypeToDiscover_Object((1,3,6,1,4,1,9,9,434,1,1,8),_CIpNetworkInetAddrTypeToDiscover_Type())
cIpNetworkInetAddrTypeToDiscover.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpNetworkInetAddrTypeToDiscover.setStatus(_A)
_CIpNetworkGigEInetAddrToDiscover_Type=InetAddress
_CIpNetworkGigEInetAddrToDiscover_Object=MibScalar
cIpNetworkGigEInetAddrToDiscover=_CIpNetworkGigEInetAddrToDiscover_Object((1,3,6,1,4,1,9,9,434,1,1,9),_CIpNetworkGigEInetAddrToDiscover_Type())
cIpNetworkGigEInetAddrToDiscover.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpNetworkGigEInetAddrToDiscover.setStatus(_A)
class _CIpNetworkDiscoveryCommand_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('noOp',2),('interfaceSpecific',3)))
_CIpNetworkDiscoveryCommand_Type.__name__=_D
_CIpNetworkDiscoveryCommand_Object=MibScalar
cIpNetworkDiscoveryCommand=_CIpNetworkDiscoveryCommand_Object((1,3,6,1,4,1,9,9,434,1,1,10),_CIpNetworkDiscoveryCommand_Type())
cIpNetworkDiscoveryCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpNetworkDiscoveryCommand.setStatus(_A)
class _CIpNetworkDiscoveryCmdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('success',1),('none',2),('inProgress',3),('noGigEInterfaceIndexSpecified',4),('noGigEInetAddrSpecified',5),('noGigESwitchWWNSpecified',6),('invalidGigEInterfaceIndex',7),('invalidGigEInetAddrType',8),('invalidGigEInetAddr',9),('generalFailure',10)))
_CIpNetworkDiscoveryCmdStatus_Type.__name__=_D
_CIpNetworkDiscoveryCmdStatus_Object=MibScalar
cIpNetworkDiscoveryCmdStatus=_CIpNetworkDiscoveryCmdStatus_Object((1,3,6,1,4,1,9,9,434,1,1,11),_CIpNetworkDiscoveryCmdStatus_Type())
cIpNetworkDiscoveryCmdStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cIpNetworkDiscoveryCmdStatus.setStatus(_A)
_CIpNetworkDiscoveryInfo_ObjectIdentity=ObjectIdentity
cIpNetworkDiscoveryInfo=_CIpNetworkDiscoveryInfo_ObjectIdentity((1,3,6,1,4,1,9,9,434,1,2))
_CIpNetworkTable_Object=MibTable
cIpNetworkTable=_CIpNetworkTable_Object((1,3,6,1,4,1,9,9,434,1,2,1))
if mibBuilder.loadTexts:cIpNetworkTable.setStatus(_A)
_CIpNetworkEntry_Object=MibTableRow
cIpNetworkEntry=_CIpNetworkEntry_Object((1,3,6,1,4,1,9,9,434,1,2,1,1))
cIpNetworkEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:cIpNetworkEntry.setStatus(_A)
class _CIpNetworkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CIpNetworkIndex_Type.__name__=_D
_CIpNetworkIndex_Object=MibTableColumn
cIpNetworkIndex=_CIpNetworkIndex_Object((1,3,6,1,4,1,9,9,434,1,2,1,1,1),_CIpNetworkIndex_Type())
cIpNetworkIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cIpNetworkIndex.setStatus(_A)
_CIpNetworkSwitchWWN_Type=FcNameId
_CIpNetworkSwitchWWN_Object=MibTableColumn
cIpNetworkSwitchWWN=_CIpNetworkSwitchWWN_Object((1,3,6,1,4,1,9,9,434,1,2,1,1,2),_CIpNetworkSwitchWWN_Type())
cIpNetworkSwitchWWN.setMaxAccess(_E)
if mibBuilder.loadTexts:cIpNetworkSwitchWWN.setStatus(_A)
_CIpNetworkInterfaceTable_Object=MibTable
cIpNetworkInterfaceTable=_CIpNetworkInterfaceTable_Object((1,3,6,1,4,1,9,9,434,1,2,2))
if mibBuilder.loadTexts:cIpNetworkInterfaceTable.setStatus(_A)
_CIpNetworkInterfaceEntry_Object=MibTableRow
cIpNetworkInterfaceEntry=_CIpNetworkInterfaceEntry_Object((1,3,6,1,4,1,9,9,434,1,2,2,1))
cIpNetworkInterfaceEntry.setIndexNames((0,_B,_G),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_H))
if mibBuilder.loadTexts:cIpNetworkInterfaceEntry.setStatus(_A)
class _CIpNetworkGigEPortSwitchWWN_Type(FcNameId):subtypeSpec=FcNameId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CIpNetworkGigEPortSwitchWWN_Type.__name__=_I
_CIpNetworkGigEPortSwitchWWN_Object=MibTableColumn
cIpNetworkGigEPortSwitchWWN=_CIpNetworkGigEPortSwitchWWN_Object((1,3,6,1,4,1,9,9,434,1,2,2,1,1),_CIpNetworkGigEPortSwitchWWN_Type())
cIpNetworkGigEPortSwitchWWN.setMaxAccess(_F)
if mibBuilder.loadTexts:cIpNetworkGigEPortSwitchWWN.setStatus(_A)
_CIpNetworkGigEPortIfIndex_Type=InterfaceIndex
_CIpNetworkGigEPortIfIndex_Object=MibTableColumn
cIpNetworkGigEPortIfIndex=_CIpNetworkGigEPortIfIndex_Object((1,3,6,1,4,1,9,9,434,1,2,2,1,2),_CIpNetworkGigEPortIfIndex_Type())
cIpNetworkGigEPortIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cIpNetworkGigEPortIfIndex.setStatus(_A)
_CIpNetworkGigEPortInetAddrType_Type=InetAddressType
_CIpNetworkGigEPortInetAddrType_Object=MibTableColumn
cIpNetworkGigEPortInetAddrType=_CIpNetworkGigEPortInetAddrType_Object((1,3,6,1,4,1,9,9,434,1,2,2,1,3),_CIpNetworkGigEPortInetAddrType_Type())
cIpNetworkGigEPortInetAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:cIpNetworkGigEPortInetAddrType.setStatus(_A)
class _CIpNetworkGigEPortInetAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CIpNetworkGigEPortInetAddr_Type.__name__=_J
_CIpNetworkGigEPortInetAddr_Object=MibTableColumn
cIpNetworkGigEPortInetAddr=_CIpNetworkGigEPortInetAddr_Object((1,3,6,1,4,1,9,9,434,1,2,2,1,4),_CIpNetworkGigEPortInetAddr_Type())
cIpNetworkGigEPortInetAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cIpNetworkGigEPortInetAddr.setStatus(_A)
_CIpNetworkDiscoveryConform_ObjectIdentity=ObjectIdentity
cIpNetworkDiscoveryConform=_CIpNetworkDiscoveryConform_ObjectIdentity((1,3,6,1,4,1,9,9,434,2))
_CIpNetworkDiscoverCompliance_ObjectIdentity=ObjectIdentity
cIpNetworkDiscoverCompliance=_CIpNetworkDiscoverCompliance_ObjectIdentity((1,3,6,1,4,1,9,9,434,2,1))
_CIpNetworkDiscoveryMIBGroups_ObjectIdentity=ObjectIdentity
cIpNetworkDiscoveryMIBGroups=_CIpNetworkDiscoveryMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,434,2,2))
cIpNetworkDiscoveryInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,434,2,2,1))
cIpNetworkDiscoveryInfoGroup.setObjects(*((_B,_P),(_B,_H)))
if mibBuilder.loadTexts:cIpNetworkDiscoveryInfoGroup.setStatus(_A)
cIpNetworkDiscoveryCfgGroup=ObjectGroup((1,3,6,1,4,1,9,9,434,2,2,2))
cIpNetworkDiscoveryCfgGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cIpNetworkDiscoveryCfgGroup.setStatus(_A)
cIpNetworkDiscoveryMIBComp=ModuleCompliance((1,3,6,1,4,1,9,9,434,2,1,1))
cIpNetworkDiscoveryMIBComp.setObjects(*((_B,_b),(_B,_c)))
if mibBuilder.loadTexts:cIpNetworkDiscoveryMIBComp.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIpNetworkDiscoveryMIB':ciscoIpNetworkDiscoveryMIB,'cIpNetworkDiscoveryMIBNotifs':cIpNetworkDiscoveryMIBNotifs,'cIpNetworkDiscoveryMIBObjs':cIpNetworkDiscoveryMIBObjs,'cIpNetworkDiscoveryConfig':cIpNetworkDiscoveryConfig,_Q:cIpNetworkAutomaticDiscovery,_R:cIpNetworkDiscoveryDelay,_S:cIpNetworkDiscoveryTypeSpinLock,_T:cIpNetworkDiscoveryType,_U:cIpNetworkDiscoveryPort,_V:cIpNetworkDiscoverySpinLock,_W:cIpNetworkGigEIfIndexToDiscover,_X:cIpNetworkInetAddrTypeToDiscover,_Y:cIpNetworkGigEInetAddrToDiscover,_Z:cIpNetworkDiscoveryCommand,_a:cIpNetworkDiscoveryCmdStatus,'cIpNetworkDiscoveryInfo':cIpNetworkDiscoveryInfo,'cIpNetworkTable':cIpNetworkTable,'cIpNetworkEntry':cIpNetworkEntry,_G:cIpNetworkIndex,_P:cIpNetworkSwitchWWN,'cIpNetworkInterfaceTable':cIpNetworkInterfaceTable,'cIpNetworkInterfaceEntry':cIpNetworkInterfaceEntry,_M:cIpNetworkGigEPortSwitchWWN,_N:cIpNetworkGigEPortIfIndex,_O:cIpNetworkGigEPortInetAddrType,_H:cIpNetworkGigEPortInetAddr,'cIpNetworkDiscoveryConform':cIpNetworkDiscoveryConform,'cIpNetworkDiscoverCompliance':cIpNetworkDiscoverCompliance,'cIpNetworkDiscoveryMIBComp':cIpNetworkDiscoveryMIBComp,'cIpNetworkDiscoveryMIBGroups':cIpNetworkDiscoveryMIBGroups,_b:cIpNetworkDiscoveryInfoGroup,_c:cIpNetworkDiscoveryCfgGroup})