_J='TrustState'
_I='cnDaiIfCfgIfIndex'
_H='AdminStatus'
_G='not-accessible'
_F='cnDaiVlanCfgVlanId'
_E='CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,VlanIdOrNone,dot1qStaticUnicastEntry,dot1qTpFdbEntry,dot1qTpFdbPort,dot1qVlanStaticEntry=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIdOrNone','dot1qStaticUnicastEntry','dot1qTpFdbEntry','dot1qTpFdbPort','dot1qVlanStaticEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
cnDaiMib=ModuleIdentity((1,3,6,1,4,1,2076,110))
if mibBuilder.loadTexts:cnDaiMib.setRevisions(('2022-02-17 00:00','2019-03-07 00:00'))
class TrustState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('untrusted',0),('trusted',1)))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class AdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CnDaiGlobal_ObjectIdentity=ObjectIdentity
cnDaiGlobal=_CnDaiGlobal_ObjectIdentity((1,3,6,1,4,1,2076,110,1))
class _CnDaiDebugFlag_Type(Integer32):defaultValue=0
_CnDaiDebugFlag_Type.__name__=_D
_CnDaiDebugFlag_Object=MibScalar
cnDaiDebugFlag=_CnDaiDebugFlag_Object((1,3,6,1,4,1,2076,110,1,1),_CnDaiDebugFlag_Type())
cnDaiDebugFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cnDaiDebugFlag.setStatus(_A)
_CnDaiVlanCfg_ObjectIdentity=ObjectIdentity
cnDaiVlanCfg=_CnDaiVlanCfg_ObjectIdentity((1,3,6,1,4,1,2076,110,2))
_CnDaiVlanCfgTable_Object=MibTable
cnDaiVlanCfgTable=_CnDaiVlanCfgTable_Object((1,3,6,1,4,1,2076,110,2,1))
if mibBuilder.loadTexts:cnDaiVlanCfgTable.setStatus(_A)
_CnDaiVlanCfgEntry_Object=MibTableRow
cnDaiVlanCfgEntry=_CnDaiVlanCfgEntry_Object((1,3,6,1,4,1,2076,110,2,1,1))
cnDaiVlanCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cnDaiVlanCfgEntry.setStatus(_A)
_CnDaiVlanCfgVlanId_Type=VlanId
_CnDaiVlanCfgVlanId_Object=MibTableColumn
cnDaiVlanCfgVlanId=_CnDaiVlanCfgVlanId_Object((1,3,6,1,4,1,2076,110,2,1,1,1),_CnDaiVlanCfgVlanId_Type())
cnDaiVlanCfgVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:cnDaiVlanCfgVlanId.setStatus(_A)
class _CnDaiVlanCfgDaiAdminStatus_Type(AdminStatus):defaultValue=2
_CnDaiVlanCfgDaiAdminStatus_Type.__name__=_H
_CnDaiVlanCfgDaiAdminStatus_Object=MibTableColumn
cnDaiVlanCfgDaiAdminStatus=_CnDaiVlanCfgDaiAdminStatus_Object((1,3,6,1,4,1,2076,110,2,1,1,2),_CnDaiVlanCfgDaiAdminStatus_Type())
cnDaiVlanCfgDaiAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cnDaiVlanCfgDaiAdminStatus.setStatus(_A)
_CnDaiVlanForwarded_Type=Counter32
_CnDaiVlanForwarded_Object=MibTableColumn
cnDaiVlanForwarded=_CnDaiVlanForwarded_Object((1,3,6,1,4,1,2076,110,2,1,1,3),_CnDaiVlanForwarded_Type())
cnDaiVlanForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:cnDaiVlanForwarded.setStatus(_A)
_CnDaiVlanDropped_Type=Counter32
_CnDaiVlanDropped_Object=MibTableColumn
cnDaiVlanDropped=_CnDaiVlanDropped_Object((1,3,6,1,4,1,2076,110,2,1,1,4),_CnDaiVlanDropped_Type())
cnDaiVlanDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:cnDaiVlanDropped.setStatus(_A)
_CnDaiVlanInvalidProtocolData_Type=Counter32
_CnDaiVlanInvalidProtocolData_Object=MibTableColumn
cnDaiVlanInvalidProtocolData=_CnDaiVlanInvalidProtocolData_Object((1,3,6,1,4,1,2076,110,2,1,1,5),_CnDaiVlanInvalidProtocolData_Type())
cnDaiVlanInvalidProtocolData.setMaxAccess(_B)
if mibBuilder.loadTexts:cnDaiVlanInvalidProtocolData.setStatus(_A)
_CnDaiVlanSrcMacValidationFailures_Type=Counter32
_CnDaiVlanSrcMacValidationFailures_Object=MibTableColumn
cnDaiVlanSrcMacValidationFailures=_CnDaiVlanSrcMacValidationFailures_Object((1,3,6,1,4,1,2076,110,2,1,1,6),_CnDaiVlanSrcMacValidationFailures_Type())
cnDaiVlanSrcMacValidationFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:cnDaiVlanSrcMacValidationFailures.setStatus(_A)
_CnDaiVlanIpValidationFailures_Type=Counter32
_CnDaiVlanIpValidationFailures_Object=MibTableColumn
cnDaiVlanIpValidationFailures=_CnDaiVlanIpValidationFailures_Object((1,3,6,1,4,1,2076,110,2,1,1,7),_CnDaiVlanIpValidationFailures_Type())
cnDaiVlanIpValidationFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:cnDaiVlanIpValidationFailures.setStatus(_A)
_CnDaiVlanDhcpBindingsPermitted_Type=Counter32
_CnDaiVlanDhcpBindingsPermitted_Object=MibTableColumn
cnDaiVlanDhcpBindingsPermitted=_CnDaiVlanDhcpBindingsPermitted_Object((1,3,6,1,4,1,2076,110,2,1,1,8),_CnDaiVlanDhcpBindingsPermitted_Type())
cnDaiVlanDhcpBindingsPermitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cnDaiVlanDhcpBindingsPermitted.setStatus(_A)
_CnDaiVlanDhcpBindingsDenied_Type=Counter32
_CnDaiVlanDhcpBindingsDenied_Object=MibTableColumn
cnDaiVlanDhcpBindingsDenied=_CnDaiVlanDhcpBindingsDenied_Object((1,3,6,1,4,1,2076,110,2,1,1,9),_CnDaiVlanDhcpBindingsDenied_Type())
cnDaiVlanDhcpBindingsDenied.setMaxAccess(_B)
if mibBuilder.loadTexts:cnDaiVlanDhcpBindingsDenied.setStatus(_A)
_CnDaiVlanStaticBindingsPermitted_Type=Counter32
_CnDaiVlanStaticBindingsPermitted_Object=MibTableColumn
cnDaiVlanStaticBindingsPermitted=_CnDaiVlanStaticBindingsPermitted_Object((1,3,6,1,4,1,2076,110,2,1,1,10),_CnDaiVlanStaticBindingsPermitted_Type())
cnDaiVlanStaticBindingsPermitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cnDaiVlanStaticBindingsPermitted.setStatus(_A)
_CnDaiVlanStaticBindingsDenied_Type=Counter32
_CnDaiVlanStaticBindingsDenied_Object=MibTableColumn
cnDaiVlanStaticBindingsDenied=_CnDaiVlanStaticBindingsDenied_Object((1,3,6,1,4,1,2076,110,2,1,1,11),_CnDaiVlanStaticBindingsDenied_Type())
cnDaiVlanStaticBindingsDenied.setMaxAccess(_B)
if mibBuilder.loadTexts:cnDaiVlanStaticBindingsDenied.setStatus(_A)
_CnDaiVlanCfgRowStatus_Type=RowStatus
_CnDaiVlanCfgRowStatus_Object=MibTableColumn
cnDaiVlanCfgRowStatus=_CnDaiVlanCfgRowStatus_Object((1,3,6,1,4,1,2076,110,2,1,1,12),_CnDaiVlanCfgRowStatus_Type())
cnDaiVlanCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cnDaiVlanCfgRowStatus.setStatus(_A)
_CnDaiIfCfg_ObjectIdentity=ObjectIdentity
cnDaiIfCfg=_CnDaiIfCfg_ObjectIdentity((1,3,6,1,4,1,2076,110,3))
_CnDaiIfCfgTable_Object=MibTable
cnDaiIfCfgTable=_CnDaiIfCfgTable_Object((1,3,6,1,4,1,2076,110,3,1))
if mibBuilder.loadTexts:cnDaiIfCfgTable.setStatus(_A)
_CnDaiIfCfgEntry_Object=MibTableRow
cnDaiIfCfgEntry=_CnDaiIfCfgEntry_Object((1,3,6,1,4,1,2076,110,3,1,1))
cnDaiIfCfgEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:cnDaiIfCfgEntry.setStatus(_A)
class _CnDaiIfCfgIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CnDaiIfCfgIfIndex_Type.__name__=_D
_CnDaiIfCfgIfIndex_Object=MibTableColumn
cnDaiIfCfgIfIndex=_CnDaiIfCfgIfIndex_Object((1,3,6,1,4,1,2076,110,3,1,1,1),_CnDaiIfCfgIfIndex_Type())
cnDaiIfCfgIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cnDaiIfCfgIfIndex.setStatus(_A)
class _CnDaiIfCfgTrustState_Type(TrustState):defaultValue=0
_CnDaiIfCfgTrustState_Type.__name__=_J
_CnDaiIfCfgTrustState_Object=MibTableColumn
cnDaiIfCfgTrustState=_CnDaiIfCfgTrustState_Object((1,3,6,1,4,1,2076,110,3,1,1,2),_CnDaiIfCfgTrustState_Type())
cnDaiIfCfgTrustState.setMaxAccess(_C)
if mibBuilder.loadTexts:cnDaiIfCfgTrustState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_J:TrustState,'VlanId':VlanId,_H:AdminStatus,'cnDaiMib':cnDaiMib,'cnDaiGlobal':cnDaiGlobal,'cnDaiDebugFlag':cnDaiDebugFlag,'cnDaiVlanCfg':cnDaiVlanCfg,'cnDaiVlanCfgTable':cnDaiVlanCfgTable,'cnDaiVlanCfgEntry':cnDaiVlanCfgEntry,_F:cnDaiVlanCfgVlanId,'cnDaiVlanCfgDaiAdminStatus':cnDaiVlanCfgDaiAdminStatus,'cnDaiVlanForwarded':cnDaiVlanForwarded,'cnDaiVlanDropped':cnDaiVlanDropped,'cnDaiVlanInvalidProtocolData':cnDaiVlanInvalidProtocolData,'cnDaiVlanSrcMacValidationFailures':cnDaiVlanSrcMacValidationFailures,'cnDaiVlanIpValidationFailures':cnDaiVlanIpValidationFailures,'cnDaiVlanDhcpBindingsPermitted':cnDaiVlanDhcpBindingsPermitted,'cnDaiVlanDhcpBindingsDenied':cnDaiVlanDhcpBindingsDenied,'cnDaiVlanStaticBindingsPermitted':cnDaiVlanStaticBindingsPermitted,'cnDaiVlanStaticBindingsDenied':cnDaiVlanStaticBindingsDenied,'cnDaiVlanCfgRowStatus':cnDaiVlanCfgRowStatus,'cnDaiIfCfg':cnDaiIfCfg,'cnDaiIfCfgTable':cnDaiIfCfgTable,'cnDaiIfCfgEntry':cnDaiIfCfgEntry,_I:cnDaiIfCfgIfIndex,'cnDaiIfCfgTrustState':cnDaiIfCfgTrustState})