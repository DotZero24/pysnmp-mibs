_Y='arubaWiredCiptTrackedClientsGroup'
_X='arubaWiredCiptPortConfigGroup'
_W='arubaWiredCiptVlanConfigGroup'
_V='arubaWiredCiptConfigGlobalGroup'
_U='arubaWiredCiptClientPortIfIndex'
_T='arubaWiredCiptClientIpAddress'
_S='arubaWiredCiptClientIpAddrType'
_R='arubaWiredCiptPortClientLimit'
_Q='arubaWiredCiptPortUpdateInterval'
_P='arubaWiredCiptPortEnable'
_O='arubaWiredCiptVidList'
_N='arubaWiredCiptProbeEnable'
_M='arubaWiredCiptEnable'
_L='arubaWiredCiptClientIpIndex'
_K='arubaWiredCiptClientVlanId'
_J='arubaWiredCiptClientMacAddress'
_I='arubaWiredCiptPortIfIndex'
_H='Integer32'
_G='read-only'
_F='TruthValue'
_E='not-accessible'
_D='Unsigned32'
_C='read-write'
_B='ARUBAWIRED-CIPT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_F)
arubaWiredCiptMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,12))
if mibBuilder.loadTexts:arubaWiredCiptMIB.setRevisions(('2020-02-07 00:00',))
class VidList(TextualConvention,OctetString):status=_A;displayHint='512x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_ArubaWiredCiptConfig_ObjectIdentity=ObjectIdentity
arubaWiredCiptConfig=_ArubaWiredCiptConfig_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,12,1))
_ArubaWiredCiptGlobalConfig_ObjectIdentity=ObjectIdentity
arubaWiredCiptGlobalConfig=_ArubaWiredCiptGlobalConfig_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,12,1,1))
class _ArubaWiredCiptEnable_Type(TruthValue):defaultValue=2
_ArubaWiredCiptEnable_Type.__name__=_F
_ArubaWiredCiptEnable_Object=MibScalar
arubaWiredCiptEnable=_ArubaWiredCiptEnable_Object((1,3,6,1,4,1,47196,4,1,1,3,12,1,1,1),_ArubaWiredCiptEnable_Type())
arubaWiredCiptEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredCiptEnable.setStatus(_A)
class _ArubaWiredCiptProbeEnable_Type(TruthValue):defaultValue=1
_ArubaWiredCiptProbeEnable_Type.__name__=_F
_ArubaWiredCiptProbeEnable_Object=MibScalar
arubaWiredCiptProbeEnable=_ArubaWiredCiptProbeEnable_Object((1,3,6,1,4,1,47196,4,1,1,3,12,1,1,2),_ArubaWiredCiptProbeEnable_Type())
arubaWiredCiptProbeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredCiptProbeEnable.setStatus(_A)
_ArubaWiredCiptVlanConfig_ObjectIdentity=ObjectIdentity
arubaWiredCiptVlanConfig=_ArubaWiredCiptVlanConfig_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,12,1,2))
_ArubaWiredCiptVidList_Type=VidList
_ArubaWiredCiptVidList_Object=MibScalar
arubaWiredCiptVidList=_ArubaWiredCiptVidList_Object((1,3,6,1,4,1,47196,4,1,1,3,12,1,2,1),_ArubaWiredCiptVidList_Type())
arubaWiredCiptVidList.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredCiptVidList.setStatus(_A)
_ArubaWiredCiptPortConfig_ObjectIdentity=ObjectIdentity
arubaWiredCiptPortConfig=_ArubaWiredCiptPortConfig_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,12,1,3))
_ArubaWiredCiptPortTable_Object=MibTable
arubaWiredCiptPortTable=_ArubaWiredCiptPortTable_Object((1,3,6,1,4,1,47196,4,1,1,3,12,1,3,1))
if mibBuilder.loadTexts:arubaWiredCiptPortTable.setStatus(_A)
_ArubaWiredCiptPortEntry_Object=MibTableRow
arubaWiredCiptPortEntry=_ArubaWiredCiptPortEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,12,1,3,1,1))
arubaWiredCiptPortEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:arubaWiredCiptPortEntry.setStatus(_A)
_ArubaWiredCiptPortIfIndex_Type=InterfaceIndex
_ArubaWiredCiptPortIfIndex_Object=MibTableColumn
arubaWiredCiptPortIfIndex=_ArubaWiredCiptPortIfIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,12,1,3,1,1,1),_ArubaWiredCiptPortIfIndex_Type())
arubaWiredCiptPortIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredCiptPortIfIndex.setStatus(_A)
class _ArubaWiredCiptPortEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disable',0),('enable',1),('auto',2)))
_ArubaWiredCiptPortEnable_Type.__name__=_H
_ArubaWiredCiptPortEnable_Object=MibTableColumn
arubaWiredCiptPortEnable=_ArubaWiredCiptPortEnable_Object((1,3,6,1,4,1,47196,4,1,1,3,12,1,3,1,1,2),_ArubaWiredCiptPortEnable_Type())
arubaWiredCiptPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredCiptPortEnable.setStatus(_A)
class _ArubaWiredCiptPortUpdateInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,28800))
_ArubaWiredCiptPortUpdateInterval_Type.__name__=_D
_ArubaWiredCiptPortUpdateInterval_Object=MibTableColumn
arubaWiredCiptPortUpdateInterval=_ArubaWiredCiptPortUpdateInterval_Object((1,3,6,1,4,1,47196,4,1,1,3,12,1,3,1,1,3),_ArubaWiredCiptPortUpdateInterval_Type())
arubaWiredCiptPortUpdateInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredCiptPortUpdateInterval.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredCiptPortUpdateInterval.setUnits('seconds')
class _ArubaWiredCiptPortClientLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_ArubaWiredCiptPortClientLimit_Type.__name__=_D
_ArubaWiredCiptPortClientLimit_Object=MibTableColumn
arubaWiredCiptPortClientLimit=_ArubaWiredCiptPortClientLimit_Object((1,3,6,1,4,1,47196,4,1,1,3,12,1,3,1,1,4),_ArubaWiredCiptPortClientLimit_Type())
arubaWiredCiptPortClientLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredCiptPortClientLimit.setStatus(_A)
_ArubaWiredCiptClients_ObjectIdentity=ObjectIdentity
arubaWiredCiptClients=_ArubaWiredCiptClients_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,12,2))
_ArubaWiredCiptTrackedClients_ObjectIdentity=ObjectIdentity
arubaWiredCiptTrackedClients=_ArubaWiredCiptTrackedClients_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,12,2,1))
_ArubaWiredCiptClientTable_Object=MibTable
arubaWiredCiptClientTable=_ArubaWiredCiptClientTable_Object((1,3,6,1,4,1,47196,4,1,1,3,12,2,1,1))
if mibBuilder.loadTexts:arubaWiredCiptClientTable.setStatus(_A)
_ArubaWiredCiptClientEntry_Object=MibTableRow
arubaWiredCiptClientEntry=_ArubaWiredCiptClientEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,12,2,1,1,1))
arubaWiredCiptClientEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:arubaWiredCiptClientEntry.setStatus(_A)
_ArubaWiredCiptClientMacAddress_Type=MacAddress
_ArubaWiredCiptClientMacAddress_Object=MibTableColumn
arubaWiredCiptClientMacAddress=_ArubaWiredCiptClientMacAddress_Object((1,3,6,1,4,1,47196,4,1,1,3,12,2,1,1,1,1),_ArubaWiredCiptClientMacAddress_Type())
arubaWiredCiptClientMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredCiptClientMacAddress.setStatus(_A)
_ArubaWiredCiptClientVlanId_Type=VlanIndex
_ArubaWiredCiptClientVlanId_Object=MibTableColumn
arubaWiredCiptClientVlanId=_ArubaWiredCiptClientVlanId_Object((1,3,6,1,4,1,47196,4,1,1,3,12,2,1,1,1,2),_ArubaWiredCiptClientVlanId_Type())
arubaWiredCiptClientVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredCiptClientVlanId.setStatus(_A)
class _ArubaWiredCiptClientIpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ArubaWiredCiptClientIpIndex_Type.__name__=_D
_ArubaWiredCiptClientIpIndex_Object=MibTableColumn
arubaWiredCiptClientIpIndex=_ArubaWiredCiptClientIpIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,12,2,1,1,1,3),_ArubaWiredCiptClientIpIndex_Type())
arubaWiredCiptClientIpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredCiptClientIpIndex.setStatus(_A)
_ArubaWiredCiptClientIpAddrType_Type=InetAddressType
_ArubaWiredCiptClientIpAddrType_Object=MibTableColumn
arubaWiredCiptClientIpAddrType=_ArubaWiredCiptClientIpAddrType_Object((1,3,6,1,4,1,47196,4,1,1,3,12,2,1,1,1,4),_ArubaWiredCiptClientIpAddrType_Type())
arubaWiredCiptClientIpAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredCiptClientIpAddrType.setStatus(_A)
_ArubaWiredCiptClientIpAddress_Type=InetAddress
_ArubaWiredCiptClientIpAddress_Object=MibTableColumn
arubaWiredCiptClientIpAddress=_ArubaWiredCiptClientIpAddress_Object((1,3,6,1,4,1,47196,4,1,1,3,12,2,1,1,1,5),_ArubaWiredCiptClientIpAddress_Type())
arubaWiredCiptClientIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredCiptClientIpAddress.setStatus(_A)
_ArubaWiredCiptClientPortIfIndex_Type=InterfaceIndex
_ArubaWiredCiptClientPortIfIndex_Object=MibTableColumn
arubaWiredCiptClientPortIfIndex=_ArubaWiredCiptClientPortIfIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,12,2,1,1,1,6),_ArubaWiredCiptClientPortIfIndex_Type())
arubaWiredCiptClientPortIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredCiptClientPortIfIndex.setStatus(_A)
_ArubaWiredCiptConformance_ObjectIdentity=ObjectIdentity
arubaWiredCiptConformance=_ArubaWiredCiptConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,12,3))
_ArubaWiredCiptGroups_ObjectIdentity=ObjectIdentity
arubaWiredCiptGroups=_ArubaWiredCiptGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,12,3,1))
_ArubaWiredCiptCompliances_ObjectIdentity=ObjectIdentity
arubaWiredCiptCompliances=_ArubaWiredCiptCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,12,3,2))
arubaWiredCiptConfigGlobalGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,12,3,1,1))
arubaWiredCiptConfigGlobalGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:arubaWiredCiptConfigGlobalGroup.setStatus(_A)
arubaWiredCiptVlanConfigGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,12,3,1,2))
arubaWiredCiptVlanConfigGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:arubaWiredCiptVlanConfigGroup.setStatus(_A)
arubaWiredCiptPortConfigGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,12,3,1,3))
arubaWiredCiptPortConfigGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:arubaWiredCiptPortConfigGroup.setStatus(_A)
arubaWiredCiptTrackedClientsGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,12,3,1,4))
arubaWiredCiptTrackedClientsGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:arubaWiredCiptTrackedClientsGroup.setStatus(_A)
arubaWiredCiptCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,12,3,2,1))
arubaWiredCiptCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:arubaWiredCiptCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VidList':VidList,'arubaWiredCiptMIB':arubaWiredCiptMIB,'arubaWiredCiptConfig':arubaWiredCiptConfig,'arubaWiredCiptGlobalConfig':arubaWiredCiptGlobalConfig,_M:arubaWiredCiptEnable,_N:arubaWiredCiptProbeEnable,'arubaWiredCiptVlanConfig':arubaWiredCiptVlanConfig,_O:arubaWiredCiptVidList,'arubaWiredCiptPortConfig':arubaWiredCiptPortConfig,'arubaWiredCiptPortTable':arubaWiredCiptPortTable,'arubaWiredCiptPortEntry':arubaWiredCiptPortEntry,_I:arubaWiredCiptPortIfIndex,_P:arubaWiredCiptPortEnable,_Q:arubaWiredCiptPortUpdateInterval,_R:arubaWiredCiptPortClientLimit,'arubaWiredCiptClients':arubaWiredCiptClients,'arubaWiredCiptTrackedClients':arubaWiredCiptTrackedClients,'arubaWiredCiptClientTable':arubaWiredCiptClientTable,'arubaWiredCiptClientEntry':arubaWiredCiptClientEntry,_J:arubaWiredCiptClientMacAddress,_K:arubaWiredCiptClientVlanId,_L:arubaWiredCiptClientIpIndex,_S:arubaWiredCiptClientIpAddrType,_T:arubaWiredCiptClientIpAddress,_U:arubaWiredCiptClientPortIfIndex,'arubaWiredCiptConformance':arubaWiredCiptConformance,'arubaWiredCiptGroups':arubaWiredCiptGroups,_V:arubaWiredCiptConfigGlobalGroup,_W:arubaWiredCiptVlanConfigGroup,_X:arubaWiredCiptPortConfigGroup,_Y:arubaWiredCiptTrackedClientsGroup,'arubaWiredCiptCompliances':arubaWiredCiptCompliances,'arubaWiredCiptCompliance':arubaWiredCiptCompliance})