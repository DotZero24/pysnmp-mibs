_F='zyIpv6SnoopingPolicyIfIndex'
_E='not-accessible'
_D='zyIpv6SnoopingPolicyName'
_C='ZYXEL-IPV6-SNOOPING-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelIpv6Snooping=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,109))
_ZyxelIpv6SnoopingSetup_ObjectIdentity=ObjectIdentity
zyxelIpv6SnoopingSetup=_ZyxelIpv6SnoopingSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,109,1))
_ZyIpv6SnoopingPolicyMaxNumberOfPolicies_Type=Integer32
_ZyIpv6SnoopingPolicyMaxNumberOfPolicies_Object=MibScalar
zyIpv6SnoopingPolicyMaxNumberOfPolicies=_ZyIpv6SnoopingPolicyMaxNumberOfPolicies_Object((1,3,6,1,4,1,890,1,15,3,109,1,1),_ZyIpv6SnoopingPolicyMaxNumberOfPolicies_Type())
zyIpv6SnoopingPolicyMaxNumberOfPolicies.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyIpv6SnoopingPolicyMaxNumberOfPolicies.setStatus(_A)
_ZyxelIpv6SnoopingPolicyTable_Object=MibTable
zyxelIpv6SnoopingPolicyTable=_ZyxelIpv6SnoopingPolicyTable_Object((1,3,6,1,4,1,890,1,15,3,109,1,2))
if mibBuilder.loadTexts:zyxelIpv6SnoopingPolicyTable.setStatus(_A)
_ZyxelIpv6SnoopingPolicyEntry_Object=MibTableRow
zyxelIpv6SnoopingPolicyEntry=_ZyxelIpv6SnoopingPolicyEntry_Object((1,3,6,1,4,1,890,1,15,3,109,1,2,1))
zyxelIpv6SnoopingPolicyEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelIpv6SnoopingPolicyEntry.setStatus(_A)
_ZyIpv6SnoopingPolicyName_Type=DisplayString
_ZyIpv6SnoopingPolicyName_Object=MibTableColumn
zyIpv6SnoopingPolicyName=_ZyIpv6SnoopingPolicyName_Object((1,3,6,1,4,1,890,1,15,3,109,1,2,1,1),_ZyIpv6SnoopingPolicyName_Type())
zyIpv6SnoopingPolicyName.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6SnoopingPolicyName.setStatus(_A)
class _ZyIpv6SnoopingPolicyProtocol_Type(Bits):namedValues=NamedValues(('dhcp',0))
_ZyIpv6SnoopingPolicyProtocol_Type.__name__='Bits'
_ZyIpv6SnoopingPolicyProtocol_Object=MibTableColumn
zyIpv6SnoopingPolicyProtocol=_ZyIpv6SnoopingPolicyProtocol_Object((1,3,6,1,4,1,890,1,15,3,109,1,2,1,2),_ZyIpv6SnoopingPolicyProtocol_Type())
zyIpv6SnoopingPolicyProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6SnoopingPolicyProtocol.setStatus(_A)
_ZyIpv6SnoopingPolicyPrefixGleanState_Type=EnabledStatus
_ZyIpv6SnoopingPolicyPrefixGleanState_Object=MibTableColumn
zyIpv6SnoopingPolicyPrefixGleanState=_ZyIpv6SnoopingPolicyPrefixGleanState_Object((1,3,6,1,4,1,890,1,15,3,109,1,2,1,3),_ZyIpv6SnoopingPolicyPrefixGleanState_Type())
zyIpv6SnoopingPolicyPrefixGleanState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6SnoopingPolicyPrefixGleanState.setStatus(_A)
_ZyIpv6SnoopingPolicyLimitAddressCount_Type=Integer32
_ZyIpv6SnoopingPolicyLimitAddressCount_Object=MibTableColumn
zyIpv6SnoopingPolicyLimitAddressCount=_ZyIpv6SnoopingPolicyLimitAddressCount_Object((1,3,6,1,4,1,890,1,15,3,109,1,2,1,4),_ZyIpv6SnoopingPolicyLimitAddressCount_Type())
zyIpv6SnoopingPolicyLimitAddressCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6SnoopingPolicyLimitAddressCount.setStatus(_A)
_ZyIpv6SnoopingPolicyRowStatus_Type=RowStatus
_ZyIpv6SnoopingPolicyRowStatus_Object=MibTableColumn
zyIpv6SnoopingPolicyRowStatus=_ZyIpv6SnoopingPolicyRowStatus_Object((1,3,6,1,4,1,890,1,15,3,109,1,2,1,100),_ZyIpv6SnoopingPolicyRowStatus_Type())
zyIpv6SnoopingPolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6SnoopingPolicyRowStatus.setStatus(_A)
_ZyxelIpv6SnoopingPolicyIfTable_Object=MibTable
zyxelIpv6SnoopingPolicyIfTable=_ZyxelIpv6SnoopingPolicyIfTable_Object((1,3,6,1,4,1,890,1,15,3,109,1,3))
if mibBuilder.loadTexts:zyxelIpv6SnoopingPolicyIfTable.setStatus(_A)
_ZyxelIpv6SnoopingPolicyIfEntry_Object=MibTableRow
zyxelIpv6SnoopingPolicyIfEntry=_ZyxelIpv6SnoopingPolicyIfEntry_Object((1,3,6,1,4,1,890,1,15,3,109,1,3,1))
zyxelIpv6SnoopingPolicyIfEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:zyxelIpv6SnoopingPolicyIfEntry.setStatus(_A)
_ZyIpv6SnoopingPolicyIfIndex_Type=Integer32
_ZyIpv6SnoopingPolicyIfIndex_Object=MibTableColumn
zyIpv6SnoopingPolicyIfIndex=_ZyIpv6SnoopingPolicyIfIndex_Object((1,3,6,1,4,1,890,1,15,3,109,1,3,1,1),_ZyIpv6SnoopingPolicyIfIndex_Type())
zyIpv6SnoopingPolicyIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6SnoopingPolicyIfIndex.setStatus(_A)
_ZyIpv6SnoopingPolicyIfAttachPolicy_Type=DisplayString
_ZyIpv6SnoopingPolicyIfAttachPolicy_Object=MibTableColumn
zyIpv6SnoopingPolicyIfAttachPolicy=_ZyIpv6SnoopingPolicyIfAttachPolicy_Object((1,3,6,1,4,1,890,1,15,3,109,1,3,1,2),_ZyIpv6SnoopingPolicyIfAttachPolicy_Type())
zyIpv6SnoopingPolicyIfAttachPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6SnoopingPolicyIfAttachPolicy.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelIpv6Snooping':zyxelIpv6Snooping,'zyxelIpv6SnoopingSetup':zyxelIpv6SnoopingSetup,'zyIpv6SnoopingPolicyMaxNumberOfPolicies':zyIpv6SnoopingPolicyMaxNumberOfPolicies,'zyxelIpv6SnoopingPolicyTable':zyxelIpv6SnoopingPolicyTable,'zyxelIpv6SnoopingPolicyEntry':zyxelIpv6SnoopingPolicyEntry,_D:zyIpv6SnoopingPolicyName,'zyIpv6SnoopingPolicyProtocol':zyIpv6SnoopingPolicyProtocol,'zyIpv6SnoopingPolicyPrefixGleanState':zyIpv6SnoopingPolicyPrefixGleanState,'zyIpv6SnoopingPolicyLimitAddressCount':zyIpv6SnoopingPolicyLimitAddressCount,'zyIpv6SnoopingPolicyRowStatus':zyIpv6SnoopingPolicyRowStatus,'zyxelIpv6SnoopingPolicyIfTable':zyxelIpv6SnoopingPolicyIfTable,'zyxelIpv6SnoopingPolicyIfEntry':zyxelIpv6SnoopingPolicyIfEntry,_F:zyIpv6SnoopingPolicyIfIndex,'zyIpv6SnoopingPolicyIfAttachPolicy':zyIpv6SnoopingPolicyIfAttachPolicy})