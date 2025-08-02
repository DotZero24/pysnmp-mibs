_c='firewallSyslogGroupVer1'
_b='firewallSecuritySpoofGroupVer1'
_a='firewallSecurityGroupVer1'
_Z='firewallGroupVer1'
_Y='firewallSyslogEnable'
_X='firewallSecuritySpoofRuleEnable'
_W='firewallSecuritySpoofAddress'
_V='firewallSecuritySpoofLabel'
_U='firewallSecuritySpoofEnable'
_T='firewallSecurityBlockIcmpRedirectionOutRule'
_S='firewallSecurityBlockIcmpRedirectionInRule'
_R='firewallSecurityBlockWanEchoBroadcastRule'
_Q='firewallSecurityBlockLanEchoRequestRule'
_P='firewallSecurityBlockWanEchoRequestRule'
_O='firewallSecurityReversePathFilteringRule'
_N='firewallSecurityIdentRule'
_M='firewallSecurityMulticastPacketRule'
_L='firewallSecuritySourceRoutedPacketRule'
_K='firewallSecurityTcpSynCookiesRule'
_J='firewallSecurityBadTcpPacketRule'
_I='firewallEnable'
_H='firewallSecuritySpoofIndex'
_G='Unsigned32'
_F='read-only'
_E='OctetString'
_D='read-write'
_C='MxEnableState'
_B='MX-FIREWALL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
firewallMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,450))
if mibBuilder.loadTexts:firewallMIB.setRevisions(('2006-03-06 00:00','2005-04-19 00:00'))
_FirewallMIBObjects_ObjectIdentity=ObjectIdentity
firewallMIBObjects=_FirewallMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,450,1))
class _FirewallEnable_Type(MxEnableState):defaultValue=1
_FirewallEnable_Type.__name__=_C
_FirewallEnable_Object=MibScalar
firewallEnable=_FirewallEnable_Object((1,3,6,1,4,1,4935,15,450,1,10),_FirewallEnable_Type())
firewallEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallEnable.setStatus(_A)
_FirewallSecurity_ObjectIdentity=ObjectIdentity
firewallSecurity=_FirewallSecurity_ObjectIdentity((1,3,6,1,4,1,4935,15,450,1,100))
class _FirewallSecurityBadTcpPacketRule_Type(MxEnableState):defaultValue=1
_FirewallSecurityBadTcpPacketRule_Type.__name__=_C
_FirewallSecurityBadTcpPacketRule_Object=MibScalar
firewallSecurityBadTcpPacketRule=_FirewallSecurityBadTcpPacketRule_Object((1,3,6,1,4,1,4935,15,450,1,100,10),_FirewallSecurityBadTcpPacketRule_Type())
firewallSecurityBadTcpPacketRule.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecurityBadTcpPacketRule.setStatus(_A)
class _FirewallSecurityTcpSynCookiesRule_Type(MxEnableState):defaultValue=1
_FirewallSecurityTcpSynCookiesRule_Type.__name__=_C
_FirewallSecurityTcpSynCookiesRule_Object=MibScalar
firewallSecurityTcpSynCookiesRule=_FirewallSecurityTcpSynCookiesRule_Object((1,3,6,1,4,1,4935,15,450,1,100,20),_FirewallSecurityTcpSynCookiesRule_Type())
firewallSecurityTcpSynCookiesRule.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecurityTcpSynCookiesRule.setStatus(_A)
class _FirewallSecuritySourceRoutedPacketRule_Type(MxEnableState):defaultValue=0
_FirewallSecuritySourceRoutedPacketRule_Type.__name__=_C
_FirewallSecuritySourceRoutedPacketRule_Object=MibScalar
firewallSecuritySourceRoutedPacketRule=_FirewallSecuritySourceRoutedPacketRule_Object((1,3,6,1,4,1,4935,15,450,1,100,30),_FirewallSecuritySourceRoutedPacketRule_Type())
firewallSecuritySourceRoutedPacketRule.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecuritySourceRoutedPacketRule.setStatus(_A)
class _FirewallSecurityMulticastPacketRule_Type(MxEnableState):defaultValue=1
_FirewallSecurityMulticastPacketRule_Type.__name__=_C
_FirewallSecurityMulticastPacketRule_Object=MibScalar
firewallSecurityMulticastPacketRule=_FirewallSecurityMulticastPacketRule_Object((1,3,6,1,4,1,4935,15,450,1,100,40),_FirewallSecurityMulticastPacketRule_Type())
firewallSecurityMulticastPacketRule.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecurityMulticastPacketRule.setStatus(_A)
class _FirewallSecurityIdentRule_Type(MxEnableState):defaultValue=1
_FirewallSecurityIdentRule_Type.__name__=_C
_FirewallSecurityIdentRule_Object=MibScalar
firewallSecurityIdentRule=_FirewallSecurityIdentRule_Object((1,3,6,1,4,1,4935,15,450,1,100,50),_FirewallSecurityIdentRule_Type())
firewallSecurityIdentRule.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecurityIdentRule.setStatus(_A)
class _FirewallSecurityReversePathFilteringRule_Type(MxEnableState):defaultValue=0
_FirewallSecurityReversePathFilteringRule_Type.__name__=_C
_FirewallSecurityReversePathFilteringRule_Object=MibScalar
firewallSecurityReversePathFilteringRule=_FirewallSecurityReversePathFilteringRule_Object((1,3,6,1,4,1,4935,15,450,1,100,60),_FirewallSecurityReversePathFilteringRule_Type())
firewallSecurityReversePathFilteringRule.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecurityReversePathFilteringRule.setStatus(_A)
class _FirewallSecurityBlockWanEchoRequestRule_Type(MxEnableState):defaultValue=0
_FirewallSecurityBlockWanEchoRequestRule_Type.__name__=_C
_FirewallSecurityBlockWanEchoRequestRule_Object=MibScalar
firewallSecurityBlockWanEchoRequestRule=_FirewallSecurityBlockWanEchoRequestRule_Object((1,3,6,1,4,1,4935,15,450,1,100,70),_FirewallSecurityBlockWanEchoRequestRule_Type())
firewallSecurityBlockWanEchoRequestRule.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecurityBlockWanEchoRequestRule.setStatus(_A)
class _FirewallSecurityBlockLanEchoRequestRule_Type(MxEnableState):defaultValue=0
_FirewallSecurityBlockLanEchoRequestRule_Type.__name__=_C
_FirewallSecurityBlockLanEchoRequestRule_Object=MibScalar
firewallSecurityBlockLanEchoRequestRule=_FirewallSecurityBlockLanEchoRequestRule_Object((1,3,6,1,4,1,4935,15,450,1,100,80),_FirewallSecurityBlockLanEchoRequestRule_Type())
firewallSecurityBlockLanEchoRequestRule.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecurityBlockLanEchoRequestRule.setStatus(_A)
class _FirewallSecurityBlockWanEchoBroadcastRule_Type(MxEnableState):defaultValue=1
_FirewallSecurityBlockWanEchoBroadcastRule_Type.__name__=_C
_FirewallSecurityBlockWanEchoBroadcastRule_Object=MibScalar
firewallSecurityBlockWanEchoBroadcastRule=_FirewallSecurityBlockWanEchoBroadcastRule_Object((1,3,6,1,4,1,4935,15,450,1,100,90),_FirewallSecurityBlockWanEchoBroadcastRule_Type())
firewallSecurityBlockWanEchoBroadcastRule.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecurityBlockWanEchoBroadcastRule.setStatus(_A)
class _FirewallSecurityBlockIcmpRedirectionInRule_Type(MxEnableState):defaultValue=1
_FirewallSecurityBlockIcmpRedirectionInRule_Type.__name__=_C
_FirewallSecurityBlockIcmpRedirectionInRule_Object=MibScalar
firewallSecurityBlockIcmpRedirectionInRule=_FirewallSecurityBlockIcmpRedirectionInRule_Object((1,3,6,1,4,1,4935,15,450,1,100,100),_FirewallSecurityBlockIcmpRedirectionInRule_Type())
firewallSecurityBlockIcmpRedirectionInRule.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecurityBlockIcmpRedirectionInRule.setStatus(_A)
class _FirewallSecurityBlockIcmpRedirectionOutRule_Type(MxEnableState):defaultValue=1
_FirewallSecurityBlockIcmpRedirectionOutRule_Type.__name__=_C
_FirewallSecurityBlockIcmpRedirectionOutRule_Object=MibScalar
firewallSecurityBlockIcmpRedirectionOutRule=_FirewallSecurityBlockIcmpRedirectionOutRule_Object((1,3,6,1,4,1,4935,15,450,1,100,110),_FirewallSecurityBlockIcmpRedirectionOutRule_Type())
firewallSecurityBlockIcmpRedirectionOutRule.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecurityBlockIcmpRedirectionOutRule.setStatus(_A)
_FirewallSecuritySpoof_ObjectIdentity=ObjectIdentity
firewallSecuritySpoof=_FirewallSecuritySpoof_ObjectIdentity((1,3,6,1,4,1,4935,15,450,1,100,1000))
class _FirewallSecuritySpoofEnable_Type(MxEnableState):defaultValue=1
_FirewallSecuritySpoofEnable_Type.__name__=_C
_FirewallSecuritySpoofEnable_Object=MibScalar
firewallSecuritySpoofEnable=_FirewallSecuritySpoofEnable_Object((1,3,6,1,4,1,4935,15,450,1,100,1000,10),_FirewallSecuritySpoofEnable_Type())
firewallSecuritySpoofEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecuritySpoofEnable.setStatus(_A)
_FirewallSecuritySpoofTable_Object=MibTable
firewallSecuritySpoofTable=_FirewallSecuritySpoofTable_Object((1,3,6,1,4,1,4935,15,450,1,100,1000,100))
if mibBuilder.loadTexts:firewallSecuritySpoofTable.setStatus(_A)
_FirewallSecuritySpoofEntry_Object=MibTableRow
firewallSecuritySpoofEntry=_FirewallSecuritySpoofEntry_Object((1,3,6,1,4,1,4935,15,450,1,100,1000,100,5))
firewallSecuritySpoofEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:firewallSecuritySpoofEntry.setStatus(_A)
class _FirewallSecuritySpoofIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FirewallSecuritySpoofIndex_Type.__name__=_G
_FirewallSecuritySpoofIndex_Object=MibTableColumn
firewallSecuritySpoofIndex=_FirewallSecuritySpoofIndex_Object((1,3,6,1,4,1,4935,15,450,1,100,1000,100,5,10),_FirewallSecuritySpoofIndex_Type())
firewallSecuritySpoofIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:firewallSecuritySpoofIndex.setStatus(_A)
class _FirewallSecuritySpoofLabel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FirewallSecuritySpoofLabel_Type.__name__=_E
_FirewallSecuritySpoofLabel_Object=MibTableColumn
firewallSecuritySpoofLabel=_FirewallSecuritySpoofLabel_Object((1,3,6,1,4,1,4935,15,450,1,100,1000,100,5,20),_FirewallSecuritySpoofLabel_Type())
firewallSecuritySpoofLabel.setMaxAccess(_F)
if mibBuilder.loadTexts:firewallSecuritySpoofLabel.setStatus(_A)
class _FirewallSecuritySpoofAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FirewallSecuritySpoofAddress_Type.__name__=_E
_FirewallSecuritySpoofAddress_Object=MibTableColumn
firewallSecuritySpoofAddress=_FirewallSecuritySpoofAddress_Object((1,3,6,1,4,1,4935,15,450,1,100,1000,100,5,30),_FirewallSecuritySpoofAddress_Type())
firewallSecuritySpoofAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:firewallSecuritySpoofAddress.setStatus(_A)
class _FirewallSecuritySpoofRuleEnable_Type(MxEnableState):defaultValue=0
_FirewallSecuritySpoofRuleEnable_Type.__name__=_C
_FirewallSecuritySpoofRuleEnable_Object=MibTableColumn
firewallSecuritySpoofRuleEnable=_FirewallSecuritySpoofRuleEnable_Object((1,3,6,1,4,1,4935,15,450,1,100,1000,100,5,40),_FirewallSecuritySpoofRuleEnable_Type())
firewallSecuritySpoofRuleEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSecuritySpoofRuleEnable.setStatus(_A)
_FirewallSyslog_ObjectIdentity=ObjectIdentity
firewallSyslog=_FirewallSyslog_ObjectIdentity((1,3,6,1,4,1,4935,15,450,1,200))
class _FirewallSyslogEnable_Type(MxEnableState):defaultValue=0
_FirewallSyslogEnable_Type.__name__=_C
_FirewallSyslogEnable_Object=MibScalar
firewallSyslogEnable=_FirewallSyslogEnable_Object((1,3,6,1,4,1,4935,15,450,1,200,10),_FirewallSyslogEnable_Type())
firewallSyslogEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:firewallSyslogEnable.setStatus(_A)
_FirewallConformance_ObjectIdentity=ObjectIdentity
firewallConformance=_FirewallConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,450,2))
_FirewallCompliances_ObjectIdentity=ObjectIdentity
firewallCompliances=_FirewallCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,450,2,1))
_FirewallGroups_ObjectIdentity=ObjectIdentity
firewallGroups=_FirewallGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,450,2,2))
firewallGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,450,2,2,1))
firewallGroupVer1.setObjects((_B,_I))
if mibBuilder.loadTexts:firewallGroupVer1.setStatus(_A)
firewallSecurityGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,450,2,2,2))
firewallSecurityGroupVer1.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:firewallSecurityGroupVer1.setStatus(_A)
firewallSecuritySpoofGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,450,2,2,3))
firewallSecuritySpoofGroupVer1.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:firewallSecuritySpoofGroupVer1.setStatus(_A)
firewallSyslogGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,450,2,2,4))
firewallSyslogGroupVer1.setObjects((_B,_Y))
if mibBuilder.loadTexts:firewallSyslogGroupVer1.setStatus(_A)
firewallComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,450,2,1,1))
firewallComplVer1.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:firewallComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'firewallMIB':firewallMIB,'firewallMIBObjects':firewallMIBObjects,_I:firewallEnable,'firewallSecurity':firewallSecurity,_J:firewallSecurityBadTcpPacketRule,_K:firewallSecurityTcpSynCookiesRule,_L:firewallSecuritySourceRoutedPacketRule,_M:firewallSecurityMulticastPacketRule,_N:firewallSecurityIdentRule,_O:firewallSecurityReversePathFilteringRule,_P:firewallSecurityBlockWanEchoRequestRule,_Q:firewallSecurityBlockLanEchoRequestRule,_R:firewallSecurityBlockWanEchoBroadcastRule,_S:firewallSecurityBlockIcmpRedirectionInRule,_T:firewallSecurityBlockIcmpRedirectionOutRule,'firewallSecuritySpoof':firewallSecuritySpoof,_U:firewallSecuritySpoofEnable,'firewallSecuritySpoofTable':firewallSecuritySpoofTable,'firewallSecuritySpoofEntry':firewallSecuritySpoofEntry,_H:firewallSecuritySpoofIndex,_V:firewallSecuritySpoofLabel,_W:firewallSecuritySpoofAddress,_X:firewallSecuritySpoofRuleEnable,'firewallSyslog':firewallSyslog,_Y:firewallSyslogEnable,'firewallConformance':firewallConformance,'firewallCompliances':firewallCompliances,'firewallComplVer1':firewallComplVer1,'firewallGroups':firewallGroups,_Z:firewallGroupVer1,_a:firewallSecurityGroupVer1,_b:firewallSecuritySpoofGroupVer1,_c:firewallSyslogGroupVer1})