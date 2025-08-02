_K='read-create'
_J='ruckusNdiStaticNDInspectIpv6Addr'
_I='read-write'
_H='not-accessible'
_G='ruckusNdiVlanConfigVlanId'
_F='ifIndex'
_E='IF-MIB'
_D='RUCKUS-NDI-MIB'
_C='TruthValue'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_C)
ruckusNdiMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,47))
class NDType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('static',2),('dynamic',3),('inspect',4),('dhcpv6',5),('dynamicDhcpv6',6),('staticDhcpv6',7),('host',8)))
class NDState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('valid',2),('pend',3)))
_RuckusNdiNotify_ObjectIdentity=ObjectIdentity
ruckusNdiNotify=_RuckusNdiNotify_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,47,0))
_RuckusNdiObjects_ObjectIdentity=ObjectIdentity
ruckusNdiObjects=_RuckusNdiObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,47,1))
_RuckusNdiVlan_ObjectIdentity=ObjectIdentity
ruckusNdiVlan=_RuckusNdiVlan_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,47,1,1))
_RuckusNdiVlanConfigTable_Object=MibTable
ruckusNdiVlanConfigTable=_RuckusNdiVlanConfigTable_Object((1,3,6,1,4,1,1991,1,1,3,47,1,1,1))
if mibBuilder.loadTexts:ruckusNdiVlanConfigTable.setStatus(_A)
_RuckusNdiVlanConfigEntry_Object=MibTableRow
ruckusNdiVlanConfigEntry=_RuckusNdiVlanConfigEntry_Object((1,3,6,1,4,1,1991,1,1,3,47,1,1,1,1))
ruckusNdiVlanConfigEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:ruckusNdiVlanConfigEntry.setStatus(_A)
_RuckusNdiVlanConfigVlanId_Type=VlanIndex
_RuckusNdiVlanConfigVlanId_Object=MibTableColumn
ruckusNdiVlanConfigVlanId=_RuckusNdiVlanConfigVlanId_Object((1,3,6,1,4,1,1991,1,1,3,47,1,1,1,1,1),_RuckusNdiVlanConfigVlanId_Type())
ruckusNdiVlanConfigVlanId.setMaxAccess(_H)
if mibBuilder.loadTexts:ruckusNdiVlanConfigVlanId.setStatus(_A)
class _RuckusNdiVlanDynNDInspectionEnable_Type(TruthValue):defaultValue=2
_RuckusNdiVlanDynNDInspectionEnable_Type.__name__=_C
_RuckusNdiVlanDynNDInspectionEnable_Object=MibTableColumn
ruckusNdiVlanDynNDInspectionEnable=_RuckusNdiVlanDynNDInspectionEnable_Object((1,3,6,1,4,1,1991,1,1,3,47,1,1,1,1,2),_RuckusNdiVlanDynNDInspectionEnable_Type())
ruckusNdiVlanDynNDInspectionEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:ruckusNdiVlanDynNDInspectionEnable.setStatus(_A)
_RuckusNdiInterface_ObjectIdentity=ObjectIdentity
ruckusNdiInterface=_RuckusNdiInterface_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,47,1,2))
_RuckusNdInspectIfConfigTable_Object=MibTable
ruckusNdInspectIfConfigTable=_RuckusNdInspectIfConfigTable_Object((1,3,6,1,4,1,1991,1,1,3,47,1,2,1))
if mibBuilder.loadTexts:ruckusNdInspectIfConfigTable.setStatus(_A)
_RuckusNdiIfConfigEntry_Object=MibTableRow
ruckusNdiIfConfigEntry=_RuckusNdiIfConfigEntry_Object((1,3,6,1,4,1,1991,1,1,3,47,1,2,1,1))
ruckusNdiIfConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ruckusNdiIfConfigEntry.setStatus(_A)
class _RuckusNdiIfTrustValue_Type(TruthValue):defaultValue=2
_RuckusNdiIfTrustValue_Type.__name__=_C
_RuckusNdiIfTrustValue_Object=MibTableColumn
ruckusNdiIfTrustValue=_RuckusNdiIfTrustValue_Object((1,3,6,1,4,1,1991,1,1,3,47,1,2,1,1,1),_RuckusNdiIfTrustValue_Type())
ruckusNdiIfTrustValue.setMaxAccess(_I)
if mibBuilder.loadTexts:ruckusNdiIfTrustValue.setStatus(_A)
_RuckusNdiNDInspect_ObjectIdentity=ObjectIdentity
ruckusNdiNDInspect=_RuckusNdiNDInspect_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,47,1,3))
_RuckusNdiStaticNDInspectTable_Object=MibTable
ruckusNdiStaticNDInspectTable=_RuckusNdiStaticNDInspectTable_Object((1,3,6,1,4,1,1991,1,1,3,47,1,3,1))
if mibBuilder.loadTexts:ruckusNdiStaticNDInspectTable.setStatus(_A)
_RuckusNdiStaticNDInspectEntry_Object=MibTableRow
ruckusNdiStaticNDInspectEntry=_RuckusNdiStaticNDInspectEntry_Object((1,3,6,1,4,1,1991,1,1,3,47,1,3,1,1))
ruckusNdiStaticNDInspectEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:ruckusNdiStaticNDInspectEntry.setStatus(_A)
_RuckusNdiStaticNDInspectIpv6Addr_Type=Ipv6Address
_RuckusNdiStaticNDInspectIpv6Addr_Object=MibTableColumn
ruckusNdiStaticNDInspectIpv6Addr=_RuckusNdiStaticNDInspectIpv6Addr_Object((1,3,6,1,4,1,1991,1,1,3,47,1,3,1,1,1),_RuckusNdiStaticNDInspectIpv6Addr_Type())
ruckusNdiStaticNDInspectIpv6Addr.setMaxAccess(_H)
if mibBuilder.loadTexts:ruckusNdiStaticNDInspectIpv6Addr.setStatus(_A)
_RuckusNdiStaticNDInspectMacAddr_Type=MacAddress
_RuckusNdiStaticNDInspectMacAddr_Object=MibTableColumn
ruckusNdiStaticNDInspectMacAddr=_RuckusNdiStaticNDInspectMacAddr_Object((1,3,6,1,4,1,1991,1,1,3,47,1,3,1,1,2),_RuckusNdiStaticNDInspectMacAddr_Type())
ruckusNdiStaticNDInspectMacAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:ruckusNdiStaticNDInspectMacAddr.setStatus(_A)
_RuckusNdiStaticNDInspectType_Type=NDType
_RuckusNdiStaticNDInspectType_Object=MibTableColumn
ruckusNdiStaticNDInspectType=_RuckusNdiStaticNDInspectType_Object((1,3,6,1,4,1,1991,1,1,3,47,1,3,1,1,3),_RuckusNdiStaticNDInspectType_Type())
ruckusNdiStaticNDInspectType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusNdiStaticNDInspectType.setStatus(_A)
_RuckusNdiStaticNDInspectState_Type=NDState
_RuckusNdiStaticNDInspectState_Object=MibTableColumn
ruckusNdiStaticNDInspectState=_RuckusNdiStaticNDInspectState_Object((1,3,6,1,4,1,1991,1,1,3,47,1,3,1,1,4),_RuckusNdiStaticNDInspectState_Type())
ruckusNdiStaticNDInspectState.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusNdiStaticNDInspectState.setStatus(_A)
_RuckusNdiStaticNDInspectAge_Type=Unsigned32
_RuckusNdiStaticNDInspectAge_Object=MibTableColumn
ruckusNdiStaticNDInspectAge=_RuckusNdiStaticNDInspectAge_Object((1,3,6,1,4,1,1991,1,1,3,47,1,3,1,1,5),_RuckusNdiStaticNDInspectAge_Type())
ruckusNdiStaticNDInspectAge.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusNdiStaticNDInspectAge.setStatus(_A)
_RuckusNdiStaticNDInspectPort_Type=InterfaceIndex
_RuckusNdiStaticNDInspectPort_Object=MibTableColumn
ruckusNdiStaticNDInspectPort=_RuckusNdiStaticNDInspectPort_Object((1,3,6,1,4,1,1991,1,1,3,47,1,3,1,1,6),_RuckusNdiStaticNDInspectPort_Type())
ruckusNdiStaticNDInspectPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusNdiStaticNDInspectPort.setStatus(_A)
_RuckusNdiStaticNDInspectRowStatus_Type=RowStatus
_RuckusNdiStaticNDInspectRowStatus_Object=MibTableColumn
ruckusNdiStaticNDInspectRowStatus=_RuckusNdiStaticNDInspectRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,47,1,3,1,1,7),_RuckusNdiStaticNDInspectRowStatus_Type())
ruckusNdiStaticNDInspectRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:ruckusNdiStaticNDInspectRowStatus.setStatus(_A)
_RuckusNdiConformance_ObjectIdentity=ObjectIdentity
ruckusNdiConformance=_RuckusNdiConformance_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,47,2))
_RuckusNdiCompliances_ObjectIdentity=ObjectIdentity
ruckusNdiCompliances=_RuckusNdiCompliances_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,47,2,1))
ruckusNdiCompliance=ModuleCompliance((1,3,6,1,4,1,1991,1,1,3,47,2,1,1))
if mibBuilder.loadTexts:ruckusNdiCompliance.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'NDType':NDType,'NDState':NDState,'ruckusNdiMIB':ruckusNdiMIB,'ruckusNdiNotify':ruckusNdiNotify,'ruckusNdiObjects':ruckusNdiObjects,'ruckusNdiVlan':ruckusNdiVlan,'ruckusNdiVlanConfigTable':ruckusNdiVlanConfigTable,'ruckusNdiVlanConfigEntry':ruckusNdiVlanConfigEntry,_G:ruckusNdiVlanConfigVlanId,'ruckusNdiVlanDynNDInspectionEnable':ruckusNdiVlanDynNDInspectionEnable,'ruckusNdiInterface':ruckusNdiInterface,'ruckusNdInspectIfConfigTable':ruckusNdInspectIfConfigTable,'ruckusNdiIfConfigEntry':ruckusNdiIfConfigEntry,'ruckusNdiIfTrustValue':ruckusNdiIfTrustValue,'ruckusNdiNDInspect':ruckusNdiNDInspect,'ruckusNdiStaticNDInspectTable':ruckusNdiStaticNDInspectTable,'ruckusNdiStaticNDInspectEntry':ruckusNdiStaticNDInspectEntry,_J:ruckusNdiStaticNDInspectIpv6Addr,'ruckusNdiStaticNDInspectMacAddr':ruckusNdiStaticNDInspectMacAddr,'ruckusNdiStaticNDInspectType':ruckusNdiStaticNDInspectType,'ruckusNdiStaticNDInspectState':ruckusNdiStaticNDInspectState,'ruckusNdiStaticNDInspectAge':ruckusNdiStaticNDInspectAge,'ruckusNdiStaticNDInspectPort':ruckusNdiStaticNDInspectPort,'ruckusNdiStaticNDInspectRowStatus':ruckusNdiStaticNDInspectRowStatus,'ruckusNdiConformance':ruckusNdiConformance,'ruckusNdiCompliances':ruckusNdiCompliances,'ruckusNdiCompliance':ruckusNdiCompliance})