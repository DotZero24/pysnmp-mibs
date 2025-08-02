_p='arubaWiredMdnsServiceProviderGroup'
_o='arubaWiredMdnsPortGroup'
_n='arubaWiredMdnsProfileFilterRuleGroup'
_m='arubaWiredMdnsProfileGroup'
_l='arubaWiredMdnsServiceGroup'
_k='arubaWiredMdnsScalarGroup'
_j='arubaWiredMdnsServiceProviderExpireTime'
_i='arubaWiredMdnsServiceProviderTtl'
_h='arubaWiredMdnsServiceProviderIpAddress'
_g='arubaWiredMdnsServiceProviderHostname'
_f='arubaWiredMdnsServiceProviderMacAddress'
_e='arubaWiredMdnsServiceProviderVlanId'
_d='arubaWiredMdnsServiceProviderServiceInstanceName'
_c='arubaWiredMdnsPortRxProfileName'
_b='arubaWiredMdnsPortTxProfileName'
_a='arubaWiredMdnsPortMdnsEnabled'
_Z='arubaWiredMdnsProfileFilterRuleAction'
_Y='arubaWiredMdnsProfileFilterRuleInstanceName'
_X='arubaWiredMdnsProfileFilterRuleServiceName'
_W='arubaWiredMdnsProfileDenyCount'
_V='arubaWiredMdnsProfilePermitCount'
_U='arubaWiredMdnsProfileVIDList'
_T='arubaWiredMdnsServiceId'
_S='arubaWiredMdnsAdminState'
_R='arubaWiredMdnsServiceProviderServiceIdIndex'
_Q='arubaWiredMdnsServiceProviderServiceId'
_P='arubaWiredMdnsPortVlanId'
_O='arubaWiredMdnsProfileFilterRuleIndex'
_N='arubaWiredMdnsProfileFilterRuleProfileName'
_M='arubaWiredMdnsProfileName'
_L='arubaWiredMdnsServiceIdIndex'
_K='arubaWiredMdnsServiceName'
_J='enable'
_I='disable'
_H='Unsigned32'
_G='OctetString'
_F='Integer32'
_E='DisplayString'
_D='not-accessible'
_C='read-only'
_B='ARUBAWIRED-MDNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','TextualConvention')
arubaWiredMdnsMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,14))
if mibBuilder.loadTexts:arubaWiredMdnsMIB.setRevisions(('2020-04-17 00:00',))
class VidList(TextualConvention,OctetString):status=_A;displayHint='512x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_ArubaWiredMdnsNotifications_ObjectIdentity=ObjectIdentity
arubaWiredMdnsNotifications=_ArubaWiredMdnsNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,14,0))
_ArubaWiredMdnsObjects_ObjectIdentity=ObjectIdentity
arubaWiredMdnsObjects=_ArubaWiredMdnsObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,14,1))
class _ArubaWiredMdnsAdminState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_ArubaWiredMdnsAdminState_Type.__name__=_F
_ArubaWiredMdnsAdminState_Object=MibScalar
arubaWiredMdnsAdminState=_ArubaWiredMdnsAdminState_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,1),_ArubaWiredMdnsAdminState_Type())
arubaWiredMdnsAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsAdminState.setStatus(_A)
_ArubaWiredMdnsServiceTable_Object=MibTable
arubaWiredMdnsServiceTable=_ArubaWiredMdnsServiceTable_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,2))
if mibBuilder.loadTexts:arubaWiredMdnsServiceTable.setStatus(_A)
_ArubaWiredMdnsServiceEntry_Object=MibTableRow
arubaWiredMdnsServiceEntry=_ArubaWiredMdnsServiceEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,2,1))
arubaWiredMdnsServiceEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:arubaWiredMdnsServiceEntry.setStatus(_A)
class _ArubaWiredMdnsServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ArubaWiredMdnsServiceName_Type.__name__=_E
_ArubaWiredMdnsServiceName_Object=MibTableColumn
arubaWiredMdnsServiceName=_ArubaWiredMdnsServiceName_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,2,1,1),_ArubaWiredMdnsServiceName_Type())
arubaWiredMdnsServiceName.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMdnsServiceName.setStatus(_A)
_ArubaWiredMdnsServiceIdIndex_Type=Unsigned32
_ArubaWiredMdnsServiceIdIndex_Object=MibTableColumn
arubaWiredMdnsServiceIdIndex=_ArubaWiredMdnsServiceIdIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,2,1,2),_ArubaWiredMdnsServiceIdIndex_Type())
arubaWiredMdnsServiceIdIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMdnsServiceIdIndex.setStatus(_A)
_ArubaWiredMdnsServiceId_Type=DisplayString
_ArubaWiredMdnsServiceId_Object=MibTableColumn
arubaWiredMdnsServiceId=_ArubaWiredMdnsServiceId_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,2,1,3),_ArubaWiredMdnsServiceId_Type())
arubaWiredMdnsServiceId.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsServiceId.setStatus(_A)
_ArubaWiredMdnsProfileTable_Object=MibTable
arubaWiredMdnsProfileTable=_ArubaWiredMdnsProfileTable_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,3))
if mibBuilder.loadTexts:arubaWiredMdnsProfileTable.setStatus(_A)
_ArubaWiredMdnsProfileEntry_Object=MibTableRow
arubaWiredMdnsProfileEntry=_ArubaWiredMdnsProfileEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,3,1))
arubaWiredMdnsProfileEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:arubaWiredMdnsProfileEntry.setStatus(_A)
class _ArubaWiredMdnsProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ArubaWiredMdnsProfileName_Type.__name__=_E
_ArubaWiredMdnsProfileName_Object=MibTableColumn
arubaWiredMdnsProfileName=_ArubaWiredMdnsProfileName_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,3,1,1),_ArubaWiredMdnsProfileName_Type())
arubaWiredMdnsProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMdnsProfileName.setStatus(_A)
_ArubaWiredMdnsProfileVIDList_Type=VidList
_ArubaWiredMdnsProfileVIDList_Object=MibTableColumn
arubaWiredMdnsProfileVIDList=_ArubaWiredMdnsProfileVIDList_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,3,1,2),_ArubaWiredMdnsProfileVIDList_Type())
arubaWiredMdnsProfileVIDList.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsProfileVIDList.setStatus(_A)
class _ArubaWiredMdnsProfilePermitCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ArubaWiredMdnsProfilePermitCount_Type.__name__=_H
_ArubaWiredMdnsProfilePermitCount_Object=MibTableColumn
arubaWiredMdnsProfilePermitCount=_ArubaWiredMdnsProfilePermitCount_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,3,1,3),_ArubaWiredMdnsProfilePermitCount_Type())
arubaWiredMdnsProfilePermitCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsProfilePermitCount.setStatus(_A)
class _ArubaWiredMdnsProfileDenyCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ArubaWiredMdnsProfileDenyCount_Type.__name__=_H
_ArubaWiredMdnsProfileDenyCount_Object=MibTableColumn
arubaWiredMdnsProfileDenyCount=_ArubaWiredMdnsProfileDenyCount_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,3,1,4),_ArubaWiredMdnsProfileDenyCount_Type())
arubaWiredMdnsProfileDenyCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsProfileDenyCount.setStatus(_A)
_ArubaWiredMdnsProfileFilterRuleTable_Object=MibTable
arubaWiredMdnsProfileFilterRuleTable=_ArubaWiredMdnsProfileFilterRuleTable_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,4))
if mibBuilder.loadTexts:arubaWiredMdnsProfileFilterRuleTable.setStatus(_A)
_ArubaWiredMdnsProfileFilterRuleEntry_Object=MibTableRow
arubaWiredMdnsProfileFilterRuleEntry=_ArubaWiredMdnsProfileFilterRuleEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,4,1))
arubaWiredMdnsProfileFilterRuleEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:arubaWiredMdnsProfileFilterRuleEntry.setStatus(_A)
class _ArubaWiredMdnsProfileFilterRuleProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ArubaWiredMdnsProfileFilterRuleProfileName_Type.__name__=_E
_ArubaWiredMdnsProfileFilterRuleProfileName_Object=MibTableColumn
arubaWiredMdnsProfileFilterRuleProfileName=_ArubaWiredMdnsProfileFilterRuleProfileName_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,4,1,1),_ArubaWiredMdnsProfileFilterRuleProfileName_Type())
arubaWiredMdnsProfileFilterRuleProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMdnsProfileFilterRuleProfileName.setStatus(_A)
class _ArubaWiredMdnsProfileFilterRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ArubaWiredMdnsProfileFilterRuleIndex_Type.__name__=_F
_ArubaWiredMdnsProfileFilterRuleIndex_Object=MibTableColumn
arubaWiredMdnsProfileFilterRuleIndex=_ArubaWiredMdnsProfileFilterRuleIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,4,1,2),_ArubaWiredMdnsProfileFilterRuleIndex_Type())
arubaWiredMdnsProfileFilterRuleIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMdnsProfileFilterRuleIndex.setStatus(_A)
class _ArubaWiredMdnsProfileFilterRuleServiceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArubaWiredMdnsProfileFilterRuleServiceName_Type.__name__=_G
_ArubaWiredMdnsProfileFilterRuleServiceName_Object=MibTableColumn
arubaWiredMdnsProfileFilterRuleServiceName=_ArubaWiredMdnsProfileFilterRuleServiceName_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,4,1,3),_ArubaWiredMdnsProfileFilterRuleServiceName_Type())
arubaWiredMdnsProfileFilterRuleServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsProfileFilterRuleServiceName.setStatus(_A)
class _ArubaWiredMdnsProfileFilterRuleInstanceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArubaWiredMdnsProfileFilterRuleInstanceName_Type.__name__=_G
_ArubaWiredMdnsProfileFilterRuleInstanceName_Object=MibTableColumn
arubaWiredMdnsProfileFilterRuleInstanceName=_ArubaWiredMdnsProfileFilterRuleInstanceName_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,4,1,4),_ArubaWiredMdnsProfileFilterRuleInstanceName_Type())
arubaWiredMdnsProfileFilterRuleInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsProfileFilterRuleInstanceName.setStatus(_A)
class _ArubaWiredMdnsProfileFilterRuleAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deny',0),('permit',1)))
_ArubaWiredMdnsProfileFilterRuleAction_Type.__name__=_F
_ArubaWiredMdnsProfileFilterRuleAction_Object=MibTableColumn
arubaWiredMdnsProfileFilterRuleAction=_ArubaWiredMdnsProfileFilterRuleAction_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,4,1,5),_ArubaWiredMdnsProfileFilterRuleAction_Type())
arubaWiredMdnsProfileFilterRuleAction.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsProfileFilterRuleAction.setStatus(_A)
_ArubaWiredMdnsPortTable_Object=MibTable
arubaWiredMdnsPortTable=_ArubaWiredMdnsPortTable_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,5))
if mibBuilder.loadTexts:arubaWiredMdnsPortTable.setStatus(_A)
_ArubaWiredMdnsPortEntry_Object=MibTableRow
arubaWiredMdnsPortEntry=_ArubaWiredMdnsPortEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,5,1))
arubaWiredMdnsPortEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:arubaWiredMdnsPortEntry.setStatus(_A)
_ArubaWiredMdnsPortVlanId_Type=VlanIndex
_ArubaWiredMdnsPortVlanId_Object=MibTableColumn
arubaWiredMdnsPortVlanId=_ArubaWiredMdnsPortVlanId_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,5,1,1),_ArubaWiredMdnsPortVlanId_Type())
arubaWiredMdnsPortVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMdnsPortVlanId.setStatus(_A)
class _ArubaWiredMdnsPortMdnsEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_ArubaWiredMdnsPortMdnsEnabled_Type.__name__=_F
_ArubaWiredMdnsPortMdnsEnabled_Object=MibTableColumn
arubaWiredMdnsPortMdnsEnabled=_ArubaWiredMdnsPortMdnsEnabled_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,5,1,2),_ArubaWiredMdnsPortMdnsEnabled_Type())
arubaWiredMdnsPortMdnsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsPortMdnsEnabled.setStatus(_A)
class _ArubaWiredMdnsPortTxProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ArubaWiredMdnsPortTxProfileName_Type.__name__=_E
_ArubaWiredMdnsPortTxProfileName_Object=MibTableColumn
arubaWiredMdnsPortTxProfileName=_ArubaWiredMdnsPortTxProfileName_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,5,1,3),_ArubaWiredMdnsPortTxProfileName_Type())
arubaWiredMdnsPortTxProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsPortTxProfileName.setStatus(_A)
class _ArubaWiredMdnsPortRxProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ArubaWiredMdnsPortRxProfileName_Type.__name__=_E
_ArubaWiredMdnsPortRxProfileName_Object=MibTableColumn
arubaWiredMdnsPortRxProfileName=_ArubaWiredMdnsPortRxProfileName_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,5,1,4),_ArubaWiredMdnsPortRxProfileName_Type())
arubaWiredMdnsPortRxProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsPortRxProfileName.setStatus(_A)
_ArubaWiredMdnsServiceProviderTable_Object=MibTable
arubaWiredMdnsServiceProviderTable=_ArubaWiredMdnsServiceProviderTable_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,6))
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderTable.setStatus(_A)
_ArubaWiredMdnsServiceProviderEntry_Object=MibTableRow
arubaWiredMdnsServiceProviderEntry=_ArubaWiredMdnsServiceProviderEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,6,1))
arubaWiredMdnsServiceProviderEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderEntry.setStatus(_A)
class _ArubaWiredMdnsServiceProviderServiceId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_ArubaWiredMdnsServiceProviderServiceId_Type.__name__=_E
_ArubaWiredMdnsServiceProviderServiceId_Object=MibTableColumn
arubaWiredMdnsServiceProviderServiceId=_ArubaWiredMdnsServiceProviderServiceId_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,6,1,1),_ArubaWiredMdnsServiceProviderServiceId_Type())
arubaWiredMdnsServiceProviderServiceId.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderServiceId.setStatus(_A)
_ArubaWiredMdnsServiceProviderServiceIdIndex_Type=Unsigned32
_ArubaWiredMdnsServiceProviderServiceIdIndex_Object=MibTableColumn
arubaWiredMdnsServiceProviderServiceIdIndex=_ArubaWiredMdnsServiceProviderServiceIdIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,6,1,2),_ArubaWiredMdnsServiceProviderServiceIdIndex_Type())
arubaWiredMdnsServiceProviderServiceIdIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderServiceIdIndex.setStatus(_A)
_ArubaWiredMdnsServiceProviderServiceInstanceName_Type=DisplayString
_ArubaWiredMdnsServiceProviderServiceInstanceName_Object=MibTableColumn
arubaWiredMdnsServiceProviderServiceInstanceName=_ArubaWiredMdnsServiceProviderServiceInstanceName_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,6,1,3),_ArubaWiredMdnsServiceProviderServiceInstanceName_Type())
arubaWiredMdnsServiceProviderServiceInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderServiceInstanceName.setStatus(_A)
_ArubaWiredMdnsServiceProviderVlanId_Type=VlanIndex
_ArubaWiredMdnsServiceProviderVlanId_Object=MibTableColumn
arubaWiredMdnsServiceProviderVlanId=_ArubaWiredMdnsServiceProviderVlanId_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,6,1,4),_ArubaWiredMdnsServiceProviderVlanId_Type())
arubaWiredMdnsServiceProviderVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderVlanId.setStatus(_A)
_ArubaWiredMdnsServiceProviderMacAddress_Type=MacAddress
_ArubaWiredMdnsServiceProviderMacAddress_Object=MibTableColumn
arubaWiredMdnsServiceProviderMacAddress=_ArubaWiredMdnsServiceProviderMacAddress_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,6,1,5),_ArubaWiredMdnsServiceProviderMacAddress_Type())
arubaWiredMdnsServiceProviderMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderMacAddress.setStatus(_A)
_ArubaWiredMdnsServiceProviderHostname_Type=DisplayString
_ArubaWiredMdnsServiceProviderHostname_Object=MibTableColumn
arubaWiredMdnsServiceProviderHostname=_ArubaWiredMdnsServiceProviderHostname_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,6,1,6),_ArubaWiredMdnsServiceProviderHostname_Type())
arubaWiredMdnsServiceProviderHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderHostname.setStatus(_A)
_ArubaWiredMdnsServiceProviderIpAddress_Type=IpAddress
_ArubaWiredMdnsServiceProviderIpAddress_Object=MibTableColumn
arubaWiredMdnsServiceProviderIpAddress=_ArubaWiredMdnsServiceProviderIpAddress_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,6,1,7),_ArubaWiredMdnsServiceProviderIpAddress_Type())
arubaWiredMdnsServiceProviderIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderIpAddress.setStatus(_A)
_ArubaWiredMdnsServiceProviderTtl_Type=Unsigned32
_ArubaWiredMdnsServiceProviderTtl_Object=MibTableColumn
arubaWiredMdnsServiceProviderTtl=_ArubaWiredMdnsServiceProviderTtl_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,6,1,8),_ArubaWiredMdnsServiceProviderTtl_Type())
arubaWiredMdnsServiceProviderTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderTtl.setStatus(_A)
_ArubaWiredMdnsServiceProviderExpireTime_Type=Unsigned32
_ArubaWiredMdnsServiceProviderExpireTime_Object=MibTableColumn
arubaWiredMdnsServiceProviderExpireTime=_ArubaWiredMdnsServiceProviderExpireTime_Object((1,3,6,1,4,1,47196,4,1,1,3,14,1,6,1,9),_ArubaWiredMdnsServiceProviderExpireTime_Type())
arubaWiredMdnsServiceProviderExpireTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderExpireTime.setStatus(_A)
_ArubaWiredMdnsConformance_ObjectIdentity=ObjectIdentity
arubaWiredMdnsConformance=_ArubaWiredMdnsConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,14,2))
_ArubaWiredMdnsCompliances_ObjectIdentity=ObjectIdentity
arubaWiredMdnsCompliances=_ArubaWiredMdnsCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,14,2,1))
_ArubaWiredMdnsGroups_ObjectIdentity=ObjectIdentity
arubaWiredMdnsGroups=_ArubaWiredMdnsGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,14,2,2))
arubaWiredMdnsScalarGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,14,2,2,1))
arubaWiredMdnsScalarGroup.setObjects((_B,_S))
if mibBuilder.loadTexts:arubaWiredMdnsScalarGroup.setStatus(_A)
arubaWiredMdnsServiceGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,14,2,2,2))
arubaWiredMdnsServiceGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:arubaWiredMdnsServiceGroup.setStatus(_A)
arubaWiredMdnsProfileGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,14,2,2,3))
arubaWiredMdnsProfileGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:arubaWiredMdnsProfileGroup.setStatus(_A)
arubaWiredMdnsProfileFilterRuleGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,14,2,2,4))
arubaWiredMdnsProfileFilterRuleGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:arubaWiredMdnsProfileFilterRuleGroup.setStatus(_A)
arubaWiredMdnsPortGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,14,2,2,5))
arubaWiredMdnsPortGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:arubaWiredMdnsPortGroup.setStatus(_A)
arubaWiredMdnsServiceProviderGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,14,2,2,6))
arubaWiredMdnsServiceProviderGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:arubaWiredMdnsServiceProviderGroup.setStatus(_A)
arubaWiredMdnsCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,14,2,1,1))
arubaWiredMdnsCompliance.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:arubaWiredMdnsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VidList':VidList,'arubaWiredMdnsMIB':arubaWiredMdnsMIB,'arubaWiredMdnsNotifications':arubaWiredMdnsNotifications,'arubaWiredMdnsObjects':arubaWiredMdnsObjects,_S:arubaWiredMdnsAdminState,'arubaWiredMdnsServiceTable':arubaWiredMdnsServiceTable,'arubaWiredMdnsServiceEntry':arubaWiredMdnsServiceEntry,_K:arubaWiredMdnsServiceName,_L:arubaWiredMdnsServiceIdIndex,_T:arubaWiredMdnsServiceId,'arubaWiredMdnsProfileTable':arubaWiredMdnsProfileTable,'arubaWiredMdnsProfileEntry':arubaWiredMdnsProfileEntry,_M:arubaWiredMdnsProfileName,_U:arubaWiredMdnsProfileVIDList,_V:arubaWiredMdnsProfilePermitCount,_W:arubaWiredMdnsProfileDenyCount,'arubaWiredMdnsProfileFilterRuleTable':arubaWiredMdnsProfileFilterRuleTable,'arubaWiredMdnsProfileFilterRuleEntry':arubaWiredMdnsProfileFilterRuleEntry,_N:arubaWiredMdnsProfileFilterRuleProfileName,_O:arubaWiredMdnsProfileFilterRuleIndex,_X:arubaWiredMdnsProfileFilterRuleServiceName,_Y:arubaWiredMdnsProfileFilterRuleInstanceName,_Z:arubaWiredMdnsProfileFilterRuleAction,'arubaWiredMdnsPortTable':arubaWiredMdnsPortTable,'arubaWiredMdnsPortEntry':arubaWiredMdnsPortEntry,_P:arubaWiredMdnsPortVlanId,_a:arubaWiredMdnsPortMdnsEnabled,_b:arubaWiredMdnsPortTxProfileName,_c:arubaWiredMdnsPortRxProfileName,'arubaWiredMdnsServiceProviderTable':arubaWiredMdnsServiceProviderTable,'arubaWiredMdnsServiceProviderEntry':arubaWiredMdnsServiceProviderEntry,_Q:arubaWiredMdnsServiceProviderServiceId,_R:arubaWiredMdnsServiceProviderServiceIdIndex,_d:arubaWiredMdnsServiceProviderServiceInstanceName,_e:arubaWiredMdnsServiceProviderVlanId,_f:arubaWiredMdnsServiceProviderMacAddress,_g:arubaWiredMdnsServiceProviderHostname,_h:arubaWiredMdnsServiceProviderIpAddress,_i:arubaWiredMdnsServiceProviderTtl,_j:arubaWiredMdnsServiceProviderExpireTime,'arubaWiredMdnsConformance':arubaWiredMdnsConformance,'arubaWiredMdnsCompliances':arubaWiredMdnsCompliances,'arubaWiredMdnsCompliance':arubaWiredMdnsCompliance,'arubaWiredMdnsGroups':arubaWiredMdnsGroups,_k:arubaWiredMdnsScalarGroup,_l:arubaWiredMdnsServiceGroup,_m:arubaWiredMdnsProfileGroup,_n:arubaWiredMdnsProfileFilterRuleGroup,_o:arubaWiredMdnsPortGroup,_p:arubaWiredMdnsServiceProviderGroup})