_U='mapMIBSecurityGroup'
_T='mapMIBRuleGroup'
_S='mapSecurityCheckInvalidv6'
_R='mapSecurityCheckInvalidv4'
_Q='mapRuleType'
_P='mapRuleEALen'
_O='mapRuleOffset'
_N='mapRulePSIDLen'
_M='mapRulePSID'
_L='mapRuleBRIPv6Address'
_K='mapRuleIPv4PrefixLen'
_J='mapRuleIPv4Prefix'
_I='mapRuleIPv6PrefixLen'
_H='mapRuleIPv6Prefix'
_G='mapRuleID'
_F='ifIndex'
_E='IF-MIB'
_D='Unsigned32'
_C='read-only'
_B='MAP-E-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddressIPv4,InetAddressIPv6,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6','InetAddressPrefixLength')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mapMIB=ModuleIdentity((1,3,6,1,2,1,242))
if mibBuilder.loadTexts:mapMIB.setRevisions(('2018-11-26 00:00',))
class RulePSID(TextualConvention,OctetString):status=_A;displayHint='0x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class RuleType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bmr',1),('fmr',2),('bmrAndfmr',3)))
_MapMIBObjects_ObjectIdentity=ObjectIdentity
mapMIBObjects=_MapMIBObjects_ObjectIdentity((1,3,6,1,2,1,242,1))
_MapRule_ObjectIdentity=ObjectIdentity
mapRule=_MapRule_ObjectIdentity((1,3,6,1,2,1,242,1,1))
_MapRuleTable_Object=MibTable
mapRuleTable=_MapRuleTable_Object((1,3,6,1,2,1,242,1,1,1))
if mibBuilder.loadTexts:mapRuleTable.setStatus(_A)
_MapRuleEntry_Object=MibTableRow
mapRuleEntry=_MapRuleEntry_Object((1,3,6,1,2,1,242,1,1,1,1))
mapRuleEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:mapRuleEntry.setStatus(_A)
class _MapRuleID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MapRuleID_Type.__name__=_D
_MapRuleID_Object=MibTableColumn
mapRuleID=_MapRuleID_Object((1,3,6,1,2,1,242,1,1,1,1,1),_MapRuleID_Type())
mapRuleID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mapRuleID.setStatus(_A)
_MapRuleIPv6Prefix_Type=InetAddressIPv6
_MapRuleIPv6Prefix_Object=MibTableColumn
mapRuleIPv6Prefix=_MapRuleIPv6Prefix_Object((1,3,6,1,2,1,242,1,1,1,1,2),_MapRuleIPv6Prefix_Type())
mapRuleIPv6Prefix.setMaxAccess(_C)
if mibBuilder.loadTexts:mapRuleIPv6Prefix.setStatus(_A)
_MapRuleIPv6PrefixLen_Type=InetAddressPrefixLength
_MapRuleIPv6PrefixLen_Object=MibTableColumn
mapRuleIPv6PrefixLen=_MapRuleIPv6PrefixLen_Object((1,3,6,1,2,1,242,1,1,1,1,3),_MapRuleIPv6PrefixLen_Type())
mapRuleIPv6PrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:mapRuleIPv6PrefixLen.setStatus(_A)
_MapRuleIPv4Prefix_Type=InetAddressIPv4
_MapRuleIPv4Prefix_Object=MibTableColumn
mapRuleIPv4Prefix=_MapRuleIPv4Prefix_Object((1,3,6,1,2,1,242,1,1,1,1,4),_MapRuleIPv4Prefix_Type())
mapRuleIPv4Prefix.setMaxAccess(_C)
if mibBuilder.loadTexts:mapRuleIPv4Prefix.setStatus(_A)
_MapRuleIPv4PrefixLen_Type=InetAddressPrefixLength
_MapRuleIPv4PrefixLen_Object=MibTableColumn
mapRuleIPv4PrefixLen=_MapRuleIPv4PrefixLen_Object((1,3,6,1,2,1,242,1,1,1,1,5),_MapRuleIPv4PrefixLen_Type())
mapRuleIPv4PrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:mapRuleIPv4PrefixLen.setStatus(_A)
_MapRuleBRIPv6Address_Type=InetAddressIPv6
_MapRuleBRIPv6Address_Object=MibTableColumn
mapRuleBRIPv6Address=_MapRuleBRIPv6Address_Object((1,3,6,1,2,1,242,1,1,1,1,6),_MapRuleBRIPv6Address_Type())
mapRuleBRIPv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:mapRuleBRIPv6Address.setStatus(_A)
_MapRulePSID_Type=RulePSID
_MapRulePSID_Object=MibTableColumn
mapRulePSID=_MapRulePSID_Object((1,3,6,1,2,1,242,1,1,1,1,7),_MapRulePSID_Type())
mapRulePSID.setMaxAccess(_C)
if mibBuilder.loadTexts:mapRulePSID.setStatus(_A)
class _MapRulePSIDLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_MapRulePSIDLen_Type.__name__=_D
_MapRulePSIDLen_Object=MibTableColumn
mapRulePSIDLen=_MapRulePSIDLen_Object((1,3,6,1,2,1,242,1,1,1,1,8),_MapRulePSIDLen_Type())
mapRulePSIDLen.setMaxAccess(_C)
if mibBuilder.loadTexts:mapRulePSIDLen.setStatus(_A)
class _MapRuleOffset_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_MapRuleOffset_Type.__name__=_D
_MapRuleOffset_Object=MibTableColumn
mapRuleOffset=_MapRuleOffset_Object((1,3,6,1,2,1,242,1,1,1,1,9),_MapRuleOffset_Type())
mapRuleOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:mapRuleOffset.setStatus(_A)
class _MapRuleEALen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,48))
_MapRuleEALen_Type.__name__=_D
_MapRuleEALen_Object=MibTableColumn
mapRuleEALen=_MapRuleEALen_Object((1,3,6,1,2,1,242,1,1,1,1,10),_MapRuleEALen_Type())
mapRuleEALen.setMaxAccess(_C)
if mibBuilder.loadTexts:mapRuleEALen.setStatus(_A)
_MapRuleType_Type=RuleType
_MapRuleType_Object=MibTableColumn
mapRuleType=_MapRuleType_Object((1,3,6,1,2,1,242,1,1,1,1,11),_MapRuleType_Type())
mapRuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:mapRuleType.setStatus(_A)
_MapSecurityCheck_ObjectIdentity=ObjectIdentity
mapSecurityCheck=_MapSecurityCheck_ObjectIdentity((1,3,6,1,2,1,242,1,2))
_MapSecurityCheckTable_Object=MibTable
mapSecurityCheckTable=_MapSecurityCheckTable_Object((1,3,6,1,2,1,242,1,2,1))
if mibBuilder.loadTexts:mapSecurityCheckTable.setStatus(_A)
_MapSecurityCheckEntry_Object=MibTableRow
mapSecurityCheckEntry=_MapSecurityCheckEntry_Object((1,3,6,1,2,1,242,1,2,1,1))
mapSecurityCheckEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mapSecurityCheckEntry.setStatus(_A)
_MapSecurityCheckInvalidv4_Type=Counter64
_MapSecurityCheckInvalidv4_Object=MibTableColumn
mapSecurityCheckInvalidv4=_MapSecurityCheckInvalidv4_Object((1,3,6,1,2,1,242,1,2,1,1,1),_MapSecurityCheckInvalidv4_Type())
mapSecurityCheckInvalidv4.setMaxAccess(_C)
if mibBuilder.loadTexts:mapSecurityCheckInvalidv4.setStatus(_A)
_MapSecurityCheckInvalidv6_Type=Counter64
_MapSecurityCheckInvalidv6_Object=MibTableColumn
mapSecurityCheckInvalidv6=_MapSecurityCheckInvalidv6_Object((1,3,6,1,2,1,242,1,2,1,1,2),_MapSecurityCheckInvalidv6_Type())
mapSecurityCheckInvalidv6.setMaxAccess(_C)
if mibBuilder.loadTexts:mapSecurityCheckInvalidv6.setStatus(_A)
_MapMIBConformance_ObjectIdentity=ObjectIdentity
mapMIBConformance=_MapMIBConformance_ObjectIdentity((1,3,6,1,2,1,242,2))
_MapMIBCompliances_ObjectIdentity=ObjectIdentity
mapMIBCompliances=_MapMIBCompliances_ObjectIdentity((1,3,6,1,2,1,242,2,1))
_MapMIBGroups_ObjectIdentity=ObjectIdentity
mapMIBGroups=_MapMIBGroups_ObjectIdentity((1,3,6,1,2,1,242,2,2))
mapMIBRuleGroup=ObjectGroup((1,3,6,1,2,1,242,2,2,1))
mapMIBRuleGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:mapMIBRuleGroup.setStatus(_A)
mapMIBSecurityGroup=ObjectGroup((1,3,6,1,2,1,242,2,2,2))
mapMIBSecurityGroup.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:mapMIBSecurityGroup.setStatus(_A)
mapMIBCompliance=ModuleCompliance((1,3,6,1,2,1,242,2,1,1))
mapMIBCompliance.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:mapMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RulePSID':RulePSID,'RuleType':RuleType,'mapMIB':mapMIB,'mapMIBObjects':mapMIBObjects,'mapRule':mapRule,'mapRuleTable':mapRuleTable,'mapRuleEntry':mapRuleEntry,_G:mapRuleID,_H:mapRuleIPv6Prefix,_I:mapRuleIPv6PrefixLen,_J:mapRuleIPv4Prefix,_K:mapRuleIPv4PrefixLen,_L:mapRuleBRIPv6Address,_M:mapRulePSID,_N:mapRulePSIDLen,_O:mapRuleOffset,_P:mapRuleEALen,_Q:mapRuleType,'mapSecurityCheck':mapSecurityCheck,'mapSecurityCheckTable':mapSecurityCheckTable,'mapSecurityCheckEntry':mapSecurityCheckEntry,_R:mapSecurityCheckInvalidv4,_S:mapSecurityCheckInvalidv6,'mapMIBConformance':mapMIBConformance,'mapMIBCompliances':mapMIBCompliances,'mapMIBCompliance':mapMIBCompliance,'mapMIBGroups':mapMIBGroups,_T:mapMIBRuleGroup,_U:mapMIBSecurityGroup})