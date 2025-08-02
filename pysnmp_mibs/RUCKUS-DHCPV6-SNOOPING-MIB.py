_L='ruckusDhcpv6SnoopBindVlanId'
_K='ruckusDhcpv6SnoopBindMacAddr'
_J='ruckusDhcpv6SnoopVlanConfigVLanId'
_I='ifIndex'
_H='IF-MIB'
_G='DisplayString'
_F='not-accessible'
_E='read-write'
_D='TruthValue'
_C='read-only'
_B='RUCKUS-DHCPV6-SNOOPING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayString,=mibBuilder.importSymbols('FOUNDRY-SN-AGENT-MIB',_G)
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
ifIndex,=mibBuilder.importSymbols(_H,_I)
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
NDState,NDType=mibBuilder.importSymbols('RUCKUS-NDI-MIB','NDState','NDType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','TextualConvention',_D)
ruckusDhcpv6SnoopMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,48))
class ClearAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('valid',0),('clear',1)))
_RuckusDhcpv6SnoopNotify_ObjectIdentity=ObjectIdentity
ruckusDhcpv6SnoopNotify=_RuckusDhcpv6SnoopNotify_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,48,0))
_RuckusDhcpv6SnoopObjects_ObjectIdentity=ObjectIdentity
ruckusDhcpv6SnoopObjects=_RuckusDhcpv6SnoopObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,48,1))
_RuckusDhcpv6SnoopGlobalObjects_ObjectIdentity=ObjectIdentity
ruckusDhcpv6SnoopGlobalObjects=_RuckusDhcpv6SnoopGlobalObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,48,1,1))
_RuckusDhcpv6SnoopGlobalClearOper_Type=ClearAction
_RuckusDhcpv6SnoopGlobalClearOper_Object=MibScalar
ruckusDhcpv6SnoopGlobalClearOper=_RuckusDhcpv6SnoopGlobalClearOper_Object((1,3,6,1,4,1,1991,1,1,3,48,1,1,1),_RuckusDhcpv6SnoopGlobalClearOper_Type())
ruckusDhcpv6SnoopGlobalClearOper.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusDhcpv6SnoopGlobalClearOper.setStatus(_A)
_RuckusDhcpv6SnoopVlan_ObjectIdentity=ObjectIdentity
ruckusDhcpv6SnoopVlan=_RuckusDhcpv6SnoopVlan_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,48,1,2))
_RuckusDhcpv6SnoopVlanConfigTable_Object=MibTable
ruckusDhcpv6SnoopVlanConfigTable=_RuckusDhcpv6SnoopVlanConfigTable_Object((1,3,6,1,4,1,1991,1,1,3,48,1,2,1))
if mibBuilder.loadTexts:ruckusDhcpv6SnoopVlanConfigTable.setStatus(_A)
_RuckusDhcpv6SnoopVlanConfigEntry_Object=MibTableRow
ruckusDhcpv6SnoopVlanConfigEntry=_RuckusDhcpv6SnoopVlanConfigEntry_Object((1,3,6,1,4,1,1991,1,1,3,48,1,2,1,1))
ruckusDhcpv6SnoopVlanConfigEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ruckusDhcpv6SnoopVlanConfigEntry.setStatus(_A)
_RuckusDhcpv6SnoopVlanConfigVLanId_Type=VlanIndex
_RuckusDhcpv6SnoopVlanConfigVLanId_Object=MibTableColumn
ruckusDhcpv6SnoopVlanConfigVLanId=_RuckusDhcpv6SnoopVlanConfigVLanId_Object((1,3,6,1,4,1,1991,1,1,3,48,1,2,1,1,1),_RuckusDhcpv6SnoopVlanConfigVLanId_Type())
ruckusDhcpv6SnoopVlanConfigVLanId.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusDhcpv6SnoopVlanConfigVLanId.setStatus(_A)
class _RuckusDhcpv6SnoopVlanConfigDhcpv6SnoopEnable_Type(TruthValue):defaultValue=2
_RuckusDhcpv6SnoopVlanConfigDhcpv6SnoopEnable_Type.__name__=_D
_RuckusDhcpv6SnoopVlanConfigDhcpv6SnoopEnable_Object=MibTableColumn
ruckusDhcpv6SnoopVlanConfigDhcpv6SnoopEnable=_RuckusDhcpv6SnoopVlanConfigDhcpv6SnoopEnable_Object((1,3,6,1,4,1,1991,1,1,3,48,1,2,1,1,2),_RuckusDhcpv6SnoopVlanConfigDhcpv6SnoopEnable_Type())
ruckusDhcpv6SnoopVlanConfigDhcpv6SnoopEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusDhcpv6SnoopVlanConfigDhcpv6SnoopEnable.setStatus(_A)
_RuckusDhcpv6SnoopInterface_ObjectIdentity=ObjectIdentity
ruckusDhcpv6SnoopInterface=_RuckusDhcpv6SnoopInterface_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,48,1,3))
_RuckusDhcpv6SnoopIfConfigTable_Object=MibTable
ruckusDhcpv6SnoopIfConfigTable=_RuckusDhcpv6SnoopIfConfigTable_Object((1,3,6,1,4,1,1991,1,1,3,48,1,3,1))
if mibBuilder.loadTexts:ruckusDhcpv6SnoopIfConfigTable.setStatus(_A)
_RuckusDhcpv6SnoopIfConfigEntry_Object=MibTableRow
ruckusDhcpv6SnoopIfConfigEntry=_RuckusDhcpv6SnoopIfConfigEntry_Object((1,3,6,1,4,1,1991,1,1,3,48,1,3,1,1))
ruckusDhcpv6SnoopIfConfigEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:ruckusDhcpv6SnoopIfConfigEntry.setStatus(_A)
class _RuckusDhcpv6SnoopIfConfigTrustValue_Type(TruthValue):defaultValue=2
_RuckusDhcpv6SnoopIfConfigTrustValue_Type.__name__=_D
_RuckusDhcpv6SnoopIfConfigTrustValue_Object=MibTableColumn
ruckusDhcpv6SnoopIfConfigTrustValue=_RuckusDhcpv6SnoopIfConfigTrustValue_Object((1,3,6,1,4,1,1991,1,1,3,48,1,3,1,1,1),_RuckusDhcpv6SnoopIfConfigTrustValue_Type())
ruckusDhcpv6SnoopIfConfigTrustValue.setMaxAccess('read-create')
if mibBuilder.loadTexts:ruckusDhcpv6SnoopIfConfigTrustValue.setStatus(_A)
_RuckusDhcpv6SnoopBind_ObjectIdentity=ObjectIdentity
ruckusDhcpv6SnoopBind=_RuckusDhcpv6SnoopBind_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,48,1,4))
_RuckusDhcpv6SnoopBindTable_Object=MibTable
ruckusDhcpv6SnoopBindTable=_RuckusDhcpv6SnoopBindTable_Object((1,3,6,1,4,1,1991,1,1,3,48,1,4,1))
if mibBuilder.loadTexts:ruckusDhcpv6SnoopBindTable.setStatus(_A)
_RuckusDhcpv6SnoopBindEntry_Object=MibTableRow
ruckusDhcpv6SnoopBindEntry=_RuckusDhcpv6SnoopBindEntry_Object((1,3,6,1,4,1,1991,1,1,3,48,1,4,1,1))
ruckusDhcpv6SnoopBindEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:ruckusDhcpv6SnoopBindEntry.setStatus(_A)
_RuckusDhcpv6SnoopBindMacAddr_Type=MacAddress
_RuckusDhcpv6SnoopBindMacAddr_Object=MibTableColumn
ruckusDhcpv6SnoopBindMacAddr=_RuckusDhcpv6SnoopBindMacAddr_Object((1,3,6,1,4,1,1991,1,1,3,48,1,4,1,1,1),_RuckusDhcpv6SnoopBindMacAddr_Type())
ruckusDhcpv6SnoopBindMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusDhcpv6SnoopBindMacAddr.setStatus(_A)
_RuckusDhcpv6SnoopBindVlanId_Type=VlanIndex
_RuckusDhcpv6SnoopBindVlanId_Object=MibTableColumn
ruckusDhcpv6SnoopBindVlanId=_RuckusDhcpv6SnoopBindVlanId_Object((1,3,6,1,4,1,1991,1,1,3,48,1,4,1,1,2),_RuckusDhcpv6SnoopBindVlanId_Type())
ruckusDhcpv6SnoopBindVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusDhcpv6SnoopBindVlanId.setStatus(_A)
_RuckusDhcpv6SnoopBindIpAddr_Type=Ipv6Address
_RuckusDhcpv6SnoopBindIpAddr_Object=MibTableColumn
ruckusDhcpv6SnoopBindIpAddr=_RuckusDhcpv6SnoopBindIpAddr_Object((1,3,6,1,4,1,1991,1,1,3,48,1,4,1,1,3),_RuckusDhcpv6SnoopBindIpAddr_Type())
ruckusDhcpv6SnoopBindIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusDhcpv6SnoopBindIpAddr.setStatus(_A)
_RuckusDhcpv6SnoopBindType_Type=NDType
_RuckusDhcpv6SnoopBindType_Object=MibTableColumn
ruckusDhcpv6SnoopBindType=_RuckusDhcpv6SnoopBindType_Object((1,3,6,1,4,1,1991,1,1,3,48,1,4,1,1,4),_RuckusDhcpv6SnoopBindType_Type())
ruckusDhcpv6SnoopBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusDhcpv6SnoopBindType.setStatus(_A)
_RuckusDhcpv6SnoopBindState_Type=NDState
_RuckusDhcpv6SnoopBindState_Object=MibTableColumn
ruckusDhcpv6SnoopBindState=_RuckusDhcpv6SnoopBindState_Object((1,3,6,1,4,1,1991,1,1,3,48,1,4,1,1,5),_RuckusDhcpv6SnoopBindState_Type())
ruckusDhcpv6SnoopBindState.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusDhcpv6SnoopBindState.setStatus(_A)
_RuckusDhcpv6SnoopBindPort_Type=Integer32
_RuckusDhcpv6SnoopBindPort_Object=MibTableColumn
ruckusDhcpv6SnoopBindPort=_RuckusDhcpv6SnoopBindPort_Object((1,3,6,1,4,1,1991,1,1,3,48,1,4,1,1,6),_RuckusDhcpv6SnoopBindPort_Type())
ruckusDhcpv6SnoopBindPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusDhcpv6SnoopBindPort.setStatus(_A)
_RuckusDhcpv6SnoopBindClearOper_Type=ClearAction
_RuckusDhcpv6SnoopBindClearOper_Object=MibTableColumn
ruckusDhcpv6SnoopBindClearOper=_RuckusDhcpv6SnoopBindClearOper_Object((1,3,6,1,4,1,1991,1,1,3,48,1,4,1,1,7),_RuckusDhcpv6SnoopBindClearOper_Type())
ruckusDhcpv6SnoopBindClearOper.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusDhcpv6SnoopBindClearOper.setStatus(_A)
_RuckusDhcpv6SnoopConformance_ObjectIdentity=ObjectIdentity
ruckusDhcpv6SnoopConformance=_RuckusDhcpv6SnoopConformance_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,48,2))
_RuckusDhcpv6SnoopCompliances_ObjectIdentity=ObjectIdentity
ruckusDhcpv6SnoopCompliances=_RuckusDhcpv6SnoopCompliances_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,48,2,1))
ruckusDhcpv6SnoopCompliance=ModuleCompliance((1,3,6,1,4,1,1991,1,1,3,48,2,1))
if mibBuilder.loadTexts:ruckusDhcpv6SnoopCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ClearAction':ClearAction,'ruckusDhcpv6SnoopMIB':ruckusDhcpv6SnoopMIB,'ruckusDhcpv6SnoopNotify':ruckusDhcpv6SnoopNotify,'ruckusDhcpv6SnoopObjects':ruckusDhcpv6SnoopObjects,'ruckusDhcpv6SnoopGlobalObjects':ruckusDhcpv6SnoopGlobalObjects,'ruckusDhcpv6SnoopGlobalClearOper':ruckusDhcpv6SnoopGlobalClearOper,'ruckusDhcpv6SnoopVlan':ruckusDhcpv6SnoopVlan,'ruckusDhcpv6SnoopVlanConfigTable':ruckusDhcpv6SnoopVlanConfigTable,'ruckusDhcpv6SnoopVlanConfigEntry':ruckusDhcpv6SnoopVlanConfigEntry,_J:ruckusDhcpv6SnoopVlanConfigVLanId,'ruckusDhcpv6SnoopVlanConfigDhcpv6SnoopEnable':ruckusDhcpv6SnoopVlanConfigDhcpv6SnoopEnable,'ruckusDhcpv6SnoopInterface':ruckusDhcpv6SnoopInterface,'ruckusDhcpv6SnoopIfConfigTable':ruckusDhcpv6SnoopIfConfigTable,'ruckusDhcpv6SnoopIfConfigEntry':ruckusDhcpv6SnoopIfConfigEntry,'ruckusDhcpv6SnoopIfConfigTrustValue':ruckusDhcpv6SnoopIfConfigTrustValue,'ruckusDhcpv6SnoopBind':ruckusDhcpv6SnoopBind,'ruckusDhcpv6SnoopBindTable':ruckusDhcpv6SnoopBindTable,'ruckusDhcpv6SnoopBindEntry':ruckusDhcpv6SnoopBindEntry,_K:ruckusDhcpv6SnoopBindMacAddr,_L:ruckusDhcpv6SnoopBindVlanId,'ruckusDhcpv6SnoopBindIpAddr':ruckusDhcpv6SnoopBindIpAddr,'ruckusDhcpv6SnoopBindType':ruckusDhcpv6SnoopBindType,'ruckusDhcpv6SnoopBindState':ruckusDhcpv6SnoopBindState,'ruckusDhcpv6SnoopBindPort':ruckusDhcpv6SnoopBindPort,'ruckusDhcpv6SnoopBindClearOper':ruckusDhcpv6SnoopBindClearOper,'ruckusDhcpv6SnoopConformance':ruckusDhcpv6SnoopConformance,'ruckusDhcpv6SnoopCompliances':ruckusDhcpv6SnoopCompliances,'ruckusDhcpv6SnoopCompliance':ruckusDhcpv6SnoopCompliance})