_L='rcArpRLPortStatusEntry'
_K='rcArpRLPortRateEntry'
_J='rcArpRLPortEnableEntry'
_I='rcDaiPortTrustEntry'
_H='rcDaiBindIp'
_G='read-create'
_F='SWITCH-DAI-MIB'
_E='read-only'
_D='EnableVar'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
rcPortEntry,=mibBuilder.importSymbols('SWITCH-SYSTEM-MIB','rcPortEntry')
EnableVar,PortList,Vlanset=mibBuilder.importSymbols('SWITCH-TC',_D,'PortList','Vlanset')
rcDai=ModuleIdentity((1,3,6,1,4,1,8886,6,1,38))
_RcDaiConfig_ObjectIdentity=ObjectIdentity
rcDaiConfig=_RcDaiConfig_ObjectIdentity((1,3,6,1,4,1,8886,6,1,38,1))
class _RcDaiStaticEnable_Type(EnableVar):defaultValue=2
_RcDaiStaticEnable_Type.__name__=_D
_RcDaiStaticEnable_Object=MibScalar
rcDaiStaticEnable=_RcDaiStaticEnable_Object((1,3,6,1,4,1,8886,6,1,38,1,1),_RcDaiStaticEnable_Type())
rcDaiStaticEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDaiStaticEnable.setStatus(_A)
class _RcDaiDhcpSnoopEnable_Type(EnableVar):defaultValue=2
_RcDaiDhcpSnoopEnable_Type.__name__=_D
_RcDaiDhcpSnoopEnable_Object=MibScalar
rcDaiDhcpSnoopEnable=_RcDaiDhcpSnoopEnable_Object((1,3,6,1,4,1,8886,6,1,38,1,2),_RcDaiDhcpSnoopEnable_Type())
rcDaiDhcpSnoopEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDaiDhcpSnoopEnable.setStatus(_A)
_RcDaiBindCurrentRules_Type=Integer32
_RcDaiBindCurrentRules_Object=MibScalar
rcDaiBindCurrentRules=_RcDaiBindCurrentRules_Object((1,3,6,1,4,1,8886,6,1,38,1,3),_RcDaiBindCurrentRules_Type())
rcDaiBindCurrentRules.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDaiBindCurrentRules.setStatus(_A)
_RcDaiBindMaxRules_Type=Integer32
_RcDaiBindMaxRules_Object=MibScalar
rcDaiBindMaxRules=_RcDaiBindMaxRules_Object((1,3,6,1,4,1,8886,6,1,38,1,4),_RcDaiBindMaxRules_Type())
rcDaiBindMaxRules.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDaiBindMaxRules.setStatus(_A)
_RcDaiPortTrustTable_Object=MibTable
rcDaiPortTrustTable=_RcDaiPortTrustTable_Object((1,3,6,1,4,1,8886,6,1,38,1,5))
if mibBuilder.loadTexts:rcDaiPortTrustTable.setStatus(_A)
_RcDaiPortTrustEntry_Object=MibTableRow
rcDaiPortTrustEntry=_RcDaiPortTrustEntry_Object((1,3,6,1,4,1,8886,6,1,38,1,5,1))
if mibBuilder.loadTexts:rcDaiPortTrustEntry.setStatus(_A)
class _RcDaiTrust_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trust',1),('untrust',2)))
_RcDaiTrust_Type.__name__=_B
_RcDaiTrust_Object=MibTableColumn
rcDaiTrust=_RcDaiTrust_Object((1,3,6,1,4,1,8886,6,1,38,1,5,1,1),_RcDaiTrust_Type())
rcDaiTrust.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDaiTrust.setStatus(_A)
_RcDaiBindTable_Object=MibTable
rcDaiBindTable=_RcDaiBindTable_Object((1,3,6,1,4,1,8886,6,1,38,1,6))
if mibBuilder.loadTexts:rcDaiBindTable.setStatus(_A)
_RcDaiBindEntry_Object=MibTableRow
rcDaiBindEntry=_RcDaiBindEntry_Object((1,3,6,1,4,1,8886,6,1,38,1,6,1))
rcDaiBindEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:rcDaiBindEntry.setStatus(_A)
_RcDaiBindIp_Type=IpAddress
_RcDaiBindIp_Object=MibTableColumn
rcDaiBindIp=_RcDaiBindIp_Object((1,3,6,1,4,1,8886,6,1,38,1,6,1,1),_RcDaiBindIp_Type())
rcDaiBindIp.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcDaiBindIp.setStatus(_A)
_RcDaiBindPortId_Type=Integer32
_RcDaiBindPortId_Object=MibTableColumn
rcDaiBindPortId=_RcDaiBindPortId_Object((1,3,6,1,4,1,8886,6,1,38,1,6,1,2),_RcDaiBindPortId_Type())
rcDaiBindPortId.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDaiBindPortId.setStatus(_A)
_RcDaiBindMac_Type=MacAddress
_RcDaiBindMac_Object=MibTableColumn
rcDaiBindMac=_RcDaiBindMac_Object((1,3,6,1,4,1,8886,6,1,38,1,6,1,3),_RcDaiBindMac_Type())
rcDaiBindMac.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDaiBindMac.setStatus(_A)
class _RcDaiBindVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcDaiBindVlan_Type.__name__=_B
_RcDaiBindVlan_Object=MibTableColumn
rcDaiBindVlan=_RcDaiBindVlan_Object((1,3,6,1,4,1,8886,6,1,38,1,6,1,4),_RcDaiBindVlan_Type())
rcDaiBindVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDaiBindVlan.setStatus(_A)
class _RcDaiBindMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dhcp-snooping',2)))
_RcDaiBindMode_Type.__name__=_B
_RcDaiBindMode_Object=MibTableColumn
rcDaiBindMode=_RcDaiBindMode_Object((1,3,6,1,4,1,8886,6,1,38,1,6,1,5),_RcDaiBindMode_Type())
rcDaiBindMode.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDaiBindMode.setStatus(_A)
class _RcDaiBindInHw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inHw',1),('notinHw',2)))
_RcDaiBindInHw_Type.__name__=_B
_RcDaiBindInHw_Object=MibTableColumn
rcDaiBindInHw=_RcDaiBindInHw_Object((1,3,6,1,4,1,8886,6,1,38,1,6,1,6),_RcDaiBindInHw_Type())
rcDaiBindInHw.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDaiBindInHw.setStatus(_A)
_RcDaiBindRowStatus_Type=RowStatus
_RcDaiBindRowStatus_Object=MibTableColumn
rcDaiBindRowStatus=_RcDaiBindRowStatus_Object((1,3,6,1,4,1,8886,6,1,38,1,6,1,7),_RcDaiBindRowStatus_Type())
rcDaiBindRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDaiBindRowStatus.setStatus(_A)
_RcArpRLPortEnableTable_Object=MibTable
rcArpRLPortEnableTable=_RcArpRLPortEnableTable_Object((1,3,6,1,4,1,8886,6,1,38,1,7))
if mibBuilder.loadTexts:rcArpRLPortEnableTable.setStatus(_A)
_RcArpRLPortEnableEntry_Object=MibTableRow
rcArpRLPortEnableEntry=_RcArpRLPortEnableEntry_Object((1,3,6,1,4,1,8886,6,1,38,1,7,1))
if mibBuilder.loadTexts:rcArpRLPortEnableEntry.setStatus(_A)
class _RcArpRLEnable_Type(EnableVar):defaultValue=2
_RcArpRLEnable_Type.__name__=_D
_RcArpRLEnable_Object=MibTableColumn
rcArpRLEnable=_RcArpRLEnable_Object((1,3,6,1,4,1,8886,6,1,38,1,7,1,1),_RcArpRLEnable_Type())
rcArpRLEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcArpRLEnable.setStatus(_A)
_RcArpRLPortRateTable_Object=MibTable
rcArpRLPortRateTable=_RcArpRLPortRateTable_Object((1,3,6,1,4,1,8886,6,1,38,1,8))
if mibBuilder.loadTexts:rcArpRLPortRateTable.setStatus(_A)
_RcArpRLPortRateEntry_Object=MibTableRow
rcArpRLPortRateEntry=_RcArpRLPortRateEntry_Object((1,3,6,1,4,1,8886,6,1,38,1,8,1))
if mibBuilder.loadTexts:rcArpRLPortRateEntry.setStatus(_A)
class _RcArpRLRate_Type(Integer32):defaultValue=100
_RcArpRLRate_Type.__name__=_B
_RcArpRLRate_Object=MibTableColumn
rcArpRLRate=_RcArpRLRate_Object((1,3,6,1,4,1,8886,6,1,38,1,8,1,1),_RcArpRLRate_Type())
rcArpRLRate.setMaxAccess(_C)
if mibBuilder.loadTexts:rcArpRLRate.setStatus(_A)
_RcArpRLPortStatusTable_Object=MibTable
rcArpRLPortStatusTable=_RcArpRLPortStatusTable_Object((1,3,6,1,4,1,8886,6,1,38,1,9))
if mibBuilder.loadTexts:rcArpRLPortStatusTable.setStatus(_A)
_RcArpRLPortStatusEntry_Object=MibTableRow
rcArpRLPortStatusEntry=_RcArpRLPortStatusEntry_Object((1,3,6,1,4,1,8886,6,1,38,1,9,1))
if mibBuilder.loadTexts:rcArpRLPortStatusEntry.setStatus(_A)
class _RcArpRLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unoverload',0),('overload',1)))
_RcArpRLStatus_Type.__name__=_B
_RcArpRLStatus_Object=MibTableColumn
rcArpRLStatus=_RcArpRLStatus_Object((1,3,6,1,4,1,8886,6,1,38,1,9,1,1),_RcArpRLStatus_Type())
rcArpRLStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcArpRLStatus.setStatus(_A)
class _RcArpRLRecoverEnable_Type(EnableVar):defaultValue=2
_RcArpRLRecoverEnable_Type.__name__=_D
_RcArpRLRecoverEnable_Object=MibScalar
rcArpRLRecoverEnable=_RcArpRLRecoverEnable_Object((1,3,6,1,4,1,8886,6,1,38,1,10),_RcArpRLRecoverEnable_Type())
rcArpRLRecoverEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcArpRLRecoverEnable.setStatus(_A)
class _RcArpRLRecoverTime_Type(Integer32):defaultValue=30
_RcArpRLRecoverTime_Type.__name__=_B
_RcArpRLRecoverTime_Object=MibScalar
rcArpRLRecoverTime=_RcArpRLRecoverTime_Object((1,3,6,1,4,1,8886,6,1,38,1,11),_RcArpRLRecoverTime_Type())
rcArpRLRecoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rcArpRLRecoverTime.setStatus(_A)
class _RcDaiIsVlanAll_Type(EnableVar):defaultValue=2
_RcDaiIsVlanAll_Type.__name__=_D
_RcDaiIsVlanAll_Object=MibScalar
rcDaiIsVlanAll=_RcDaiIsVlanAll_Object((1,3,6,1,4,1,8886,6,1,38,1,12),_RcDaiIsVlanAll_Type())
rcDaiIsVlanAll.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDaiIsVlanAll.setStatus(_A)
_RcDaiProtectVlanList_Type=Vlanset
_RcDaiProtectVlanList_Object=MibScalar
rcDaiProtectVlanList=_RcDaiProtectVlanList_Object((1,3,6,1,4,1,8886,6,1,38,1,13),_RcDaiProtectVlanList_Type())
rcDaiProtectVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDaiProtectVlanList.setStatus(_A)
rcPortEntry.registerAugmentions((_F,_I))
rcDaiPortTrustEntry.setIndexNames(*rcPortEntry.getIndexNames())
rcPortEntry.registerAugmentions((_F,_J))
rcArpRLPortEnableEntry.setIndexNames(*rcPortEntry.getIndexNames())
rcPortEntry.registerAugmentions((_F,_K))
rcArpRLPortRateEntry.setIndexNames(*rcPortEntry.getIndexNames())
rcPortEntry.registerAugmentions((_F,_L))
rcArpRLPortStatusEntry.setIndexNames(*rcPortEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'rcDai':rcDai,'rcDaiConfig':rcDaiConfig,'rcDaiStaticEnable':rcDaiStaticEnable,'rcDaiDhcpSnoopEnable':rcDaiDhcpSnoopEnable,'rcDaiBindCurrentRules':rcDaiBindCurrentRules,'rcDaiBindMaxRules':rcDaiBindMaxRules,'rcDaiPortTrustTable':rcDaiPortTrustTable,_I:rcDaiPortTrustEntry,'rcDaiTrust':rcDaiTrust,'rcDaiBindTable':rcDaiBindTable,'rcDaiBindEntry':rcDaiBindEntry,_H:rcDaiBindIp,'rcDaiBindPortId':rcDaiBindPortId,'rcDaiBindMac':rcDaiBindMac,'rcDaiBindVlan':rcDaiBindVlan,'rcDaiBindMode':rcDaiBindMode,'rcDaiBindInHw':rcDaiBindInHw,'rcDaiBindRowStatus':rcDaiBindRowStatus,'rcArpRLPortEnableTable':rcArpRLPortEnableTable,_J:rcArpRLPortEnableEntry,'rcArpRLEnable':rcArpRLEnable,'rcArpRLPortRateTable':rcArpRLPortRateTable,_K:rcArpRLPortRateEntry,'rcArpRLRate':rcArpRLRate,'rcArpRLPortStatusTable':rcArpRLPortStatusTable,_L:rcArpRLPortStatusEntry,'rcArpRLStatus':rcArpRLStatus,'rcArpRLRecoverEnable':rcArpRLRecoverEnable,'rcArpRLRecoverTime':rcArpRLRecoverTime,'rcDaiIsVlanAll':rcDaiIsVlanAll,'rcDaiProtectVlanList':rcDaiProtectVlanList})