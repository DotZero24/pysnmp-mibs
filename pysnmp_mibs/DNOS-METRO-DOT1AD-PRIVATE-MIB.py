_O='agentL2ProtocolTunnelingProtocolId'
_N='agentL2ProtocolTunnelingMACAddress'
_M='agentL2ProtocolTunnelingVlanId'
_L='agentDot1adInterfaceIfIndex'
_K='agentDot1adSubscriptionNewCustomerVLanId'
_J='agentDot1adSubscriptionNewServiceVLanId'
_I='agentDot1adSubscriptionInterfaceIfIndex'
_H='agentDot1adServiceVLanId'
_G='DisplayString'
_F='read-only'
_E='read-create'
_D='DNOS-METRO-DOT1AD-PRIVATE-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AgentPortMask,dnOS=mibBuilder.importSymbols('DELL-REF-MIB','AgentPortMask','dnOS')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TruthValue')
fastPathDot1adPrivateMIB=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40))
if mibBuilder.loadTexts:fastPathDot1adPrivateMIB.setRevisions(('2011-01-26 00:00','2008-05-27 00:00'))
_Dot1adDataTunnelingGroup_ObjectIdentity=ObjectIdentity
dot1adDataTunnelingGroup=_Dot1adDataTunnelingGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1))
_AgentDot1adServiceConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1adServiceConfigGroup=_AgentDot1adServiceConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,1))
_AgentDot1adServiceTable_Object=MibTable
agentDot1adServiceTable=_AgentDot1adServiceTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,1,1))
if mibBuilder.loadTexts:agentDot1adServiceTable.setStatus(_A)
_AgentDot1adServiceEntry_Object=MibTableRow
agentDot1adServiceEntry=_AgentDot1adServiceEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,1,1,1))
agentDot1adServiceEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:agentDot1adServiceEntry.setStatus(_A)
class _AgentDot1adServiceVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentDot1adServiceVLanId_Type.__name__=_B
_AgentDot1adServiceVLanId_Object=MibTableColumn
agentDot1adServiceVLanId=_AgentDot1adServiceVLanId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,1,1,1,1),_AgentDot1adServiceVLanId_Type())
agentDot1adServiceVLanId.setMaxAccess(_F)
if mibBuilder.loadTexts:agentDot1adServiceVLanId.setStatus(_A)
_AgentDot1adServiceRowStatus_Type=RowStatus
_AgentDot1adServiceRowStatus_Object=MibTableColumn
agentDot1adServiceRowStatus=_AgentDot1adServiceRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,1,1,1,2),_AgentDot1adServiceRowStatus_Type())
agentDot1adServiceRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1adServiceRowStatus.setStatus(_A)
class _AgentDot1adServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDot1adServiceName_Type.__name__=_G
_AgentDot1adServiceName_Object=MibTableColumn
agentDot1adServiceName=_AgentDot1adServiceName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,1,1,1,3),_AgentDot1adServiceName_Type())
agentDot1adServiceName.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1adServiceName.setStatus(_A)
class _AgentDot1adServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('e-line',1),('e-lan',2),('e-tree',3),('tls',4)))
_AgentDot1adServiceType_Type.__name__=_B
_AgentDot1adServiceType_Object=MibTableColumn
agentDot1adServiceType=_AgentDot1adServiceType_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,1,1,1,4),_AgentDot1adServiceType_Type())
agentDot1adServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adServiceType.setStatus(_A)
_AgentDot1adServiceNNIList_Type=AgentPortMask
_AgentDot1adServiceNNIList_Object=MibTableColumn
agentDot1adServiceNNIList=_AgentDot1adServiceNNIList_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,1,1,1,5),_AgentDot1adServiceNNIList_Type())
agentDot1adServiceNNIList.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adServiceNNIList.setStatus(_A)
_AgentDot1adServiceNNIListCount_Type=Integer32
_AgentDot1adServiceNNIListCount_Object=MibTableColumn
agentDot1adServiceNNIListCount=_AgentDot1adServiceNNIListCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,1,1,1,6),_AgentDot1adServiceNNIListCount_Type())
agentDot1adServiceNNIListCount.setMaxAccess(_F)
if mibBuilder.loadTexts:agentDot1adServiceNNIListCount.setStatus(_A)
_AgentDot1adSubscriptionConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1adSubscriptionConfigGroup=_AgentDot1adSubscriptionConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2))
_AgentDot1adSubscriptionTable_Object=MibTable
agentDot1adSubscriptionTable=_AgentDot1adSubscriptionTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1))
if mibBuilder.loadTexts:agentDot1adSubscriptionTable.setStatus(_A)
_AgentDot1adSubscriptionEntry_Object=MibTableRow
agentDot1adSubscriptionEntry=_AgentDot1adSubscriptionEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1))
agentDot1adSubscriptionEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:agentDot1adSubscriptionEntry.setStatus(_A)
class _AgentDot1adSubscriptionInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentDot1adSubscriptionInterfaceIfIndex_Type.__name__=_B
_AgentDot1adSubscriptionInterfaceIfIndex_Object=MibTableColumn
agentDot1adSubscriptionInterfaceIfIndex=_AgentDot1adSubscriptionInterfaceIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,1),_AgentDot1adSubscriptionInterfaceIfIndex_Type())
agentDot1adSubscriptionInterfaceIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:agentDot1adSubscriptionInterfaceIfIndex.setStatus(_A)
class _AgentDot1adSubscriptionNewServiceVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentDot1adSubscriptionNewServiceVLanId_Type.__name__=_B
_AgentDot1adSubscriptionNewServiceVLanId_Object=MibTableColumn
agentDot1adSubscriptionNewServiceVLanId=_AgentDot1adSubscriptionNewServiceVLanId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,2),_AgentDot1adSubscriptionNewServiceVLanId_Type())
agentDot1adSubscriptionNewServiceVLanId.setMaxAccess(_F)
if mibBuilder.loadTexts:agentDot1adSubscriptionNewServiceVLanId.setStatus(_A)
class _AgentDot1adSubscriptionNewCustomerVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentDot1adSubscriptionNewCustomerVLanId_Type.__name__=_B
_AgentDot1adSubscriptionNewCustomerVLanId_Object=MibTableColumn
agentDot1adSubscriptionNewCustomerVLanId=_AgentDot1adSubscriptionNewCustomerVLanId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,3),_AgentDot1adSubscriptionNewCustomerVLanId_Type())
agentDot1adSubscriptionNewCustomerVLanId.setMaxAccess(_F)
if mibBuilder.loadTexts:agentDot1adSubscriptionNewCustomerVLanId.setStatus(_A)
class _AgentDot1adSubscriptionServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDot1adSubscriptionServiceName_Type.__name__=_G
_AgentDot1adSubscriptionServiceName_Object=MibTableColumn
agentDot1adSubscriptionServiceName=_AgentDot1adSubscriptionServiceName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,4),_AgentDot1adSubscriptionServiceName_Type())
agentDot1adSubscriptionServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adSubscriptionServiceName.setStatus(_A)
class _AgentDot1adSubscriptionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDot1adSubscriptionName_Type.__name__=_G
_AgentDot1adSubscriptionName_Object=MibTableColumn
agentDot1adSubscriptionName=_AgentDot1adSubscriptionName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,5),_AgentDot1adSubscriptionName_Type())
agentDot1adSubscriptionName.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adSubscriptionName.setStatus(_A)
class _AgentDot1adSubscriptionMatchCriteria_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('untagged',1),('priority-tagged',2),('vlan-tagged',3)))
_AgentDot1adSubscriptionMatchCriteria_Type.__name__=_B
_AgentDot1adSubscriptionMatchCriteria_Object=MibTableColumn
agentDot1adSubscriptionMatchCriteria=_AgentDot1adSubscriptionMatchCriteria_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,6),_AgentDot1adSubscriptionMatchCriteria_Type())
agentDot1adSubscriptionMatchCriteria.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adSubscriptionMatchCriteria.setStatus(_A)
_AgentDot1adSubscriptionServiceVLanId_Type=Integer32
_AgentDot1adSubscriptionServiceVLanId_Object=MibTableColumn
agentDot1adSubscriptionServiceVLanId=_AgentDot1adSubscriptionServiceVLanId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,7),_AgentDot1adSubscriptionServiceVLanId_Type())
agentDot1adSubscriptionServiceVLanId.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adSubscriptionServiceVLanId.setStatus(_A)
_AgentDot1adSubscriptionCustomerVLanId_Type=Integer32
_AgentDot1adSubscriptionCustomerVLanId_Object=MibTableColumn
agentDot1adSubscriptionCustomerVLanId=_AgentDot1adSubscriptionCustomerVLanId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,8),_AgentDot1adSubscriptionCustomerVLanId_Type())
agentDot1adSubscriptionCustomerVLanId.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adSubscriptionCustomerVLanId.setStatus(_A)
_AgentDot1adSubscriptionPriority_Type=Integer32
_AgentDot1adSubscriptionPriority_Object=MibTableColumn
agentDot1adSubscriptionPriority=_AgentDot1adSubscriptionPriority_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,9),_AgentDot1adSubscriptionPriority_Type())
agentDot1adSubscriptionPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adSubscriptionPriority.setStatus(_A)
class _AgentDot1adSubscriptionMatchAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('assign-customer-VLANID',1),('re-mark-customer-VLANID',2),('remove-customer-VLANID',3)))
_AgentDot1adSubscriptionMatchAction_Type.__name__=_B
_AgentDot1adSubscriptionMatchAction_Object=MibTableColumn
agentDot1adSubscriptionMatchAction=_AgentDot1adSubscriptionMatchAction_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,10),_AgentDot1adSubscriptionMatchAction_Type())
agentDot1adSubscriptionMatchAction.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adSubscriptionMatchAction.setStatus(_A)
_AgentDot1adSubscriptionNNIList_Type=AgentPortMask
_AgentDot1adSubscriptionNNIList_Object=MibTableColumn
agentDot1adSubscriptionNNIList=_AgentDot1adSubscriptionNNIList_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,11),_AgentDot1adSubscriptionNNIList_Type())
agentDot1adSubscriptionNNIList.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adSubscriptionNNIList.setStatus(_A)
_AgentDot1adSubscriptionNNIListCount_Type=Integer32
_AgentDot1adSubscriptionNNIListCount_Object=MibTableColumn
agentDot1adSubscriptionNNIListCount=_AgentDot1adSubscriptionNNIListCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,12),_AgentDot1adSubscriptionNNIListCount_Type())
agentDot1adSubscriptionNNIListCount.setMaxAccess(_F)
if mibBuilder.loadTexts:agentDot1adSubscriptionNNIListCount.setStatus(_A)
_AgentDot1adSubscriptionRowStatus_Type=RowStatus
_AgentDot1adSubscriptionRowStatus_Object=MibTableColumn
agentDot1adSubscriptionRowStatus=_AgentDot1adSubscriptionRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,1,2,1,1,13),_AgentDot1adSubscriptionRowStatus_Type())
agentDot1adSubscriptionRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1adSubscriptionRowStatus.setStatus(_A)
_Dot1adProtocolTunnelingGroup_ObjectIdentity=ObjectIdentity
dot1adProtocolTunnelingGroup=_Dot1adProtocolTunnelingGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2))
_AgentDot1adInterfaceTypeConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1adInterfaceTypeConfigGroup=_AgentDot1adInterfaceTypeConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,1))
_AgentDot1adInterfaceTypeTable_Object=MibTable
agentDot1adInterfaceTypeTable=_AgentDot1adInterfaceTypeTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,1,1))
if mibBuilder.loadTexts:agentDot1adInterfaceTypeTable.setStatus(_A)
_AgentDot1adInterfaceTypeEntry_Object=MibTableRow
agentDot1adInterfaceTypeEntry=_AgentDot1adInterfaceTypeEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,1,1,1))
agentDot1adInterfaceTypeEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:agentDot1adInterfaceTypeEntry.setStatus(_A)
_AgentDot1adInterfaceIfIndex_Type=InterfaceIndex
_AgentDot1adInterfaceIfIndex_Object=MibTableColumn
agentDot1adInterfaceIfIndex=_AgentDot1adInterfaceIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,1,1,1,1),_AgentDot1adInterfaceIfIndex_Type())
agentDot1adInterfaceIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentDot1adInterfaceIfIndex.setStatus(_A)
class _AgentDot1adInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('uni',0),('uni-p',1),('uni-s',2),('nni',3),('switchport',4)))
_AgentDot1adInterfaceType_Type.__name__=_B
_AgentDot1adInterfaceType_Object=MibTableColumn
agentDot1adInterfaceType=_AgentDot1adInterfaceType_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,1,1,1,2),_AgentDot1adInterfaceType_Type())
agentDot1adInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adInterfaceType.setStatus(_A)
class _AgentDot1adInterfacePreserveCTAGDot1p_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_AgentDot1adInterfacePreserveCTAGDot1p_Type.__name__=_B
_AgentDot1adInterfacePreserveCTAGDot1p_Object=MibTableColumn
agentDot1adInterfacePreserveCTAGDot1p=_AgentDot1adInterfacePreserveCTAGDot1p_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,1,1,1,3),_AgentDot1adInterfacePreserveCTAGDot1p_Type())
agentDot1adInterfacePreserveCTAGDot1p.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1adInterfacePreserveCTAGDot1p.setStatus(_A)
_AgentL2TunnelingConfigGroup_ObjectIdentity=ObjectIdentity
agentL2TunnelingConfigGroup=_AgentL2TunnelingConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,2))
_AgentL2ProtocolTunnelingTable_Object=MibTable
agentL2ProtocolTunnelingTable=_AgentL2ProtocolTunnelingTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,2,1))
if mibBuilder.loadTexts:agentL2ProtocolTunnelingTable.setStatus(_A)
_AgentL2ProtocolTunnelingEntry_Object=MibTableRow
agentL2ProtocolTunnelingEntry=_AgentL2ProtocolTunnelingEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,2,1,1))
agentL2ProtocolTunnelingEntry.setIndexNames((0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:agentL2ProtocolTunnelingEntry.setStatus(_A)
class _AgentL2ProtocolTunnelingVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentL2ProtocolTunnelingVlanId_Type.__name__=_B
_AgentL2ProtocolTunnelingVlanId_Object=MibTableColumn
agentL2ProtocolTunnelingVlanId=_AgentL2ProtocolTunnelingVlanId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,2,1,1,1),_AgentL2ProtocolTunnelingVlanId_Type())
agentL2ProtocolTunnelingVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:agentL2ProtocolTunnelingVlanId.setStatus(_A)
_AgentL2ProtocolTunnelingMACAddress_Type=MacAddress
_AgentL2ProtocolTunnelingMACAddress_Object=MibTableColumn
agentL2ProtocolTunnelingMACAddress=_AgentL2ProtocolTunnelingMACAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,2,1,1,2),_AgentL2ProtocolTunnelingMACAddress_Type())
agentL2ProtocolTunnelingMACAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentL2ProtocolTunnelingMACAddress.setStatus(_A)
class _AgentL2ProtocolTunnelingProtocolId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentL2ProtocolTunnelingProtocolId_Type.__name__=_B
_AgentL2ProtocolTunnelingProtocolId_Object=MibTableColumn
agentL2ProtocolTunnelingProtocolId=_AgentL2ProtocolTunnelingProtocolId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,2,1,1,3),_AgentL2ProtocolTunnelingProtocolId_Type())
agentL2ProtocolTunnelingProtocolId.setMaxAccess(_E)
if mibBuilder.loadTexts:agentL2ProtocolTunnelingProtocolId.setStatus(_A)
class _AgentL2ProtocolTunnelingAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('terminate',0),('tunnel',1),('discard',2),('discard-shutdown',3)))
_AgentL2ProtocolTunnelingAction_Type.__name__=_B
_AgentL2ProtocolTunnelingAction_Object=MibTableColumn
agentL2ProtocolTunnelingAction=_AgentL2ProtocolTunnelingAction_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,2,1,1,4),_AgentL2ProtocolTunnelingAction_Type())
agentL2ProtocolTunnelingAction.setMaxAccess(_E)
if mibBuilder.loadTexts:agentL2ProtocolTunnelingAction.setStatus(_A)
_AgentL2ProtocolTunnelingRowStatus_Type=RowStatus
_AgentL2ProtocolTunnelingRowStatus_Object=MibTableColumn
agentL2ProtocolTunnelingRowStatus=_AgentL2ProtocolTunnelingRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,40,2,2,1,1,5),_AgentL2ProtocolTunnelingRowStatus_Type())
agentL2ProtocolTunnelingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentL2ProtocolTunnelingRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fastPathDot1adPrivateMIB':fastPathDot1adPrivateMIB,'dot1adDataTunnelingGroup':dot1adDataTunnelingGroup,'agentDot1adServiceConfigGroup':agentDot1adServiceConfigGroup,'agentDot1adServiceTable':agentDot1adServiceTable,'agentDot1adServiceEntry':agentDot1adServiceEntry,_H:agentDot1adServiceVLanId,'agentDot1adServiceRowStatus':agentDot1adServiceRowStatus,'agentDot1adServiceName':agentDot1adServiceName,'agentDot1adServiceType':agentDot1adServiceType,'agentDot1adServiceNNIList':agentDot1adServiceNNIList,'agentDot1adServiceNNIListCount':agentDot1adServiceNNIListCount,'agentDot1adSubscriptionConfigGroup':agentDot1adSubscriptionConfigGroup,'agentDot1adSubscriptionTable':agentDot1adSubscriptionTable,'agentDot1adSubscriptionEntry':agentDot1adSubscriptionEntry,_I:agentDot1adSubscriptionInterfaceIfIndex,_J:agentDot1adSubscriptionNewServiceVLanId,_K:agentDot1adSubscriptionNewCustomerVLanId,'agentDot1adSubscriptionServiceName':agentDot1adSubscriptionServiceName,'agentDot1adSubscriptionName':agentDot1adSubscriptionName,'agentDot1adSubscriptionMatchCriteria':agentDot1adSubscriptionMatchCriteria,'agentDot1adSubscriptionServiceVLanId':agentDot1adSubscriptionServiceVLanId,'agentDot1adSubscriptionCustomerVLanId':agentDot1adSubscriptionCustomerVLanId,'agentDot1adSubscriptionPriority':agentDot1adSubscriptionPriority,'agentDot1adSubscriptionMatchAction':agentDot1adSubscriptionMatchAction,'agentDot1adSubscriptionNNIList':agentDot1adSubscriptionNNIList,'agentDot1adSubscriptionNNIListCount':agentDot1adSubscriptionNNIListCount,'agentDot1adSubscriptionRowStatus':agentDot1adSubscriptionRowStatus,'dot1adProtocolTunnelingGroup':dot1adProtocolTunnelingGroup,'agentDot1adInterfaceTypeConfigGroup':agentDot1adInterfaceTypeConfigGroup,'agentDot1adInterfaceTypeTable':agentDot1adInterfaceTypeTable,'agentDot1adInterfaceTypeEntry':agentDot1adInterfaceTypeEntry,_L:agentDot1adInterfaceIfIndex,'agentDot1adInterfaceType':agentDot1adInterfaceType,'agentDot1adInterfacePreserveCTAGDot1p':agentDot1adInterfacePreserveCTAGDot1p,'agentL2TunnelingConfigGroup':agentL2TunnelingConfigGroup,'agentL2ProtocolTunnelingTable':agentL2ProtocolTunnelingTable,'agentL2ProtocolTunnelingEntry':agentL2ProtocolTunnelingEntry,_M:agentL2ProtocolTunnelingVlanId,_N:agentL2ProtocolTunnelingMACAddress,_O:agentL2ProtocolTunnelingProtocolId,'agentL2ProtocolTunnelingAction':agentL2ProtocolTunnelingAction,'agentL2ProtocolTunnelingRowStatus':agentL2ProtocolTunnelingRowStatus})